# Django
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Django Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny

# Models
from applications.product.models import Product
from .models import Sale, SaleDetail

# Serializers
from .serializers import SaleProcessSerializer1, SaleReportSerializer


class SalesViewSet(viewsets.ViewSet):
    authentication_classes = (TokenAuthentication,)
    queryset = Sale.objects.all()

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        serializer = SaleReportSerializer(Sale.objects.all(), many=True)
        return Response(serializer.data)

    def create(self, request):
        # Deserializamos la data contenida en la request
        serializer = SaleProcessSerializer1(data=request.data)

        # Validamos la data
        serializer.is_valid(raise_exception=True)

        sale = Sale.objects.create(
            sale_date=timezone.now(),
            amount=0,
            quantity=0,
            invoice_type=serializer.validated_data["invoice_type"],
            payment_type=serializer.validated_data["payment_type"],
            address=serializer.validated_data["address"],
            user=self.request.user,
        )
        # Variables para la venta
        quantity = 0
        amount = 0
        # Obtenemos los productos de la venta
        products = Product.objects.filter(id__in=serializer.validated_data["products"])
        quantities = serializer.validated_data["quantity"]

        sales_details = []
        for product, quantity in zip(products, quantities):
            sale_detail = SaleDetail(
                sale=sale,
                product=product,
                quantity=quantity,
                purchase_price=product.purchase_price,
                sale_price=product.sale_price,
            )
            amount += product.sale_price * quantity
            quantity += quantity
            sales_details.append(sale_detail)

        # Actualizamos la venta
        sale.amount = amount
        sale.quantity = quantity
        sale.save()

        # Creamos el detalle de venta
        SaleDetail.objects.bulk_create(sales_details)

        return Response(
            {"message": "Sale successfully created", "data": f"{serializer.data}"}
        )

    def retrieve(self, request, pk=None):
        sale = get_object_or_404(Sale.objects.all(), id=pk)
        serializer = SaleReportSerializer(sale)
        return Response({"message": "success", "data": serializer.data})
