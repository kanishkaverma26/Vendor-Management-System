from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import VendorSerializer, VendorPerformanceSerializer, PurchaseOrderSerializer
from .models import Vendor, VendorPerformance, PurchaseOrder
from django.db.models import Avg, Count
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .utils import calculate_vendor_performance_metrics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import *
from django.utils import timezone
# Create your views here.


class SuperuserTokenAPIView(ObtainAuthToken):
    """
    API endpoint to generate a JWT access token for a superuser.

    Authentication:
    - Requires a valid superuser username and password.

    HTTP Methods:
    - POST: Generate a new JWT access token for the superuser.

    Request Payload:
    - Requires a JSON payload with the superuser's username and password.

    Response:
    - Returns a JSON response containing the access token if successful.
    - Returns an error response if the superuser is not found or not authorized.

    Example Request:
    ```
    POST /api/superuser/token/
    Content-Type: application/json

    {
      "username": "your_superuser_username",
      "password": "your_superuser_password"
    }
    ```
    """
    def post(self, request):
        print(request.data,"[[[]]]")
        superuser = User.objects.filter(username=request.data['username']).first()

        if superuser and superuser.is_superuser:
            refresh_token = RefreshToken.for_user(superuser)
            access_token = str(refresh_token.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Superuser not found or not authorized'}, status=status.HTTP_401_UNAUTHORIZED)
class VendorListCreateView(generics.ListCreateAPIView):
    """
    List and create vendors.

    Authentication: Requires token authentication.

    HTTP Methods:
    - GET: List all vendors.
    - POST: Create a new vendor.

    GET Response: JSON list of vendors.
    POST Response: JSON details of the created vendor if successful.

    Example POST Request:
    POST /api/vendors/
    Content-Type: application/json

    {
      "name": "New Vendor",
      "contact_details": "New Contact",
      "address": "New Address",
      "vendor_code": "V003"
    }
    """
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a vendor.

    Authentication: Requires token authentication.

    HTTP Methods:
    - GET: Retrieve details of a specific vendor.
    - PUT/PATCH: Update details of a specific vendor.
    - DELETE: Delete a specific vendor.

    Example GET Response:
    HTTP 200 OK
    {
      "id": 1,
      "name": "Vendor1",
      "contact_details": "Contact1",
      "address": "Address1",
      "vendor_code": "V001"
    }
    """
    permission_classes = [IsAuthenticated]
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to list and create purchase orders.

    Authentication:
    - Requires token authentication.

    HTTP Methods:
    - GET: List all purchase orders.
    - POST: Create a new purchase order.

    """
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        """
        Perform creation of a new purchase order.

        Triggers the recalculation of vendor performance metrics.

        """
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            purchase_order = PurchaseOrder.objects.get(pk=response.data['id'])
            calculate_vendor_performance_metrics(purchase_order.vendor)
        return response

class PurchaseOrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a purchase order.

    Authentication:
    - Requires token authentication.

    HTTP Methods:
    - GET: Retrieve details of a specific purchase order.
    - PUT/PATCH: Update a purchase order.
    - DELETE: Delete a purchase order.

    """
    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def update(self, request, *args, **kwargs):
        """
        Perform updating of a purchase order.

        Triggers the recalculation of vendor performance metrics if the status is 'Completed'.

        """
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            purchase_order = PurchaseOrder.objects.get(pk=response.data['id'])
            print(purchase_order.status,"lllllll")
            calculate_vendor_performance_metrics(purchase_order.vendor)
        return response


class VendorPerformanceView(APIView):
    """
    Retrieve performance metrics for a specific vendor.

    Authentication:
    - Requires token authentication.

    HTTP Method:
    - GET: Retrieve on-time delivery rate, quality rating average,
           average response time, and fulfillment rate.

    Parameters:
    - vendor_id: Identifier for the specific vendor.

    Example Response:
    HTTP 200 OK
    {
      "on_time_delivery_rate": 95.0,
      "quality_rating_avg": 4.2,
      "average_response_time": 2.5,
      "fulfillment_rate": 90.0
    }

    Example Error Response:
    HTTP 404 Not Found
    {
      "error": "Vendor with id {vendor_id} does not exist"
    }
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"error": f"Vendor with id {vendor_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)

        performance_metrics = {
            "on_time_delivery_rate": vendor.on_time_delivery_rate,
            "quality_rating_avg": vendor.quality_rating_avg,
            "average_response_time": vendor.average_response_time,
            "fulfillment_rate": vendor.fulfillment_rate,
        }

        return Response(performance_metrics, status=status.HTTP_200_OK)
    
class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
    """
    Acknowledge the receipt of a purchase order.

    Authentication:
    - Requires token authentication.

    HTTP Method:
    - PUT/PATCH: Update the acknowledgment status of a specific purchase order.

    Parameters:
    - pk: Identifier for the specific purchase order.

    Example Response:
    HTTP 200 OK
    {
      "id": 1,
      "acknowledgment_date": "2023-12-01T12:34:56Z",
      ...
    }

    Note:
    - If the acknowledgment_date is present, vendor performance metrics are recalculated.
    """

    permission_classes = [IsAuthenticated]
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def post(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            purchase_order = self.get_object()
            print(timezone.now())
            # Assuming acknowledgment_date is a DateTimeField in your PurchaseOrder model
            purchase_order.acknowledgment_date = timezone.now()
            purchase_order.save()

            # Recalculate average_response_time
            calculate_vendor_performance_metrics(purchase_order.vendor)

        return response