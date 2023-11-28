from django.urls import path
from .views import VendorListCreateView, VendorDetailView, PurchaseOrderListCreateView, PurchaseOrderDetailView, VendorPerformanceView, AcknowledgePurchaseOrderView, SuperuserTokenAPIView

urlpatterns = [
    path('token/', SuperuserTokenAPIView.as_view(), name='token_obtain'),
    path('vendors/', VendorListCreateView.as_view(), name='vendor-list-create'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    path('purchase_orders/', PurchaseOrderListCreateView.as_view(), name='purchase-order-list-create'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetailView.as_view(), name='purchase-order-detail'),
    path('purchase_orders/<int:pk>/acknowledge/', AcknowledgePurchaseOrderView.as_view(), name='acknowledge-purchase-order'),

]