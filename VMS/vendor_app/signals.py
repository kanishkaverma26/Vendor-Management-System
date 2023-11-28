from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrder
from .utils import calculate_vendor_performance_metrics

@receiver(post_save, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == 'Completed' or instance.quality_rating is not None or instance.acknowledgment_date is not None:
        calculate_vendor_performance_metrics(instance.vendor)
