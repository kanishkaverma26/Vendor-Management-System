from django.db.models import Avg, Count, ExpressionWrapper, F, fields
from datetime import timedelta
from django.db import models
from django.utils import timezone
from .models import PurchaseOrder, Vendor, VendorPerformance

def calculate_vendor_performance_metrics(vendor):
    completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='Completed')
    on_time_delivered = completed_orders.filter(delivery_date__lte=timezone.now())
    vendor.on_time_delivery_rate = on_time_delivered.count() / completed_orders.count() if completed_orders.count() else 0.0

    vendor.quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0
    
    acknowledged_orders = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    response_times = [(order.acknowledgment_date - order.issue_date).days for order in acknowledged_orders]
    vendor.average_response_time = sum(response_times) / len(response_times) if len(response_times) else 0.0
    total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
    successful_fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor, status='Completed', delivery_date__lte=timezone.now(), quality_rating__isnull=False, acknowledgment_date__isnull=False).count()
    vendor.fulfillment_rate = successful_fulfilled_orders / total_orders if total_orders else 0.0
    vendor.save()
    update_historical_performance(vendor)


def update_historical_performance(vendor):

    historical_performance = VendorPerformance(
        vendor=vendor,
        date=timezone.now(),
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate
    )
    historical_performance.save()