# Django
from django.utils import timezone

# Django Rest Framework
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Models
from applications.product.models import Product
from .models import Sale, SaleDetail


# Serializers
from .serializers import (
    SaleReportSerializer,
    SaleProcessSerializer,
    SaleProcessSerializer1,
)


class SaleReportList(ListAPIView):
    serializer_class = SaleReportSerializer

    def get_queryset(self):
        return Sale.objects.all()


class RegisterSale(CreateAPIView):
    serializer_class = SaleProcessSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        # Deserializamos la data contenida en la request
        serializer = SaleProcessSerializer(data=request.data)

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
        products = serializer.validated_data["products"]
        sales_details = []
        for product in products:
            prod = Product.objects.get(id=product["id"])
            sale_detail = SaleDetail(
                sale=sale,
                product=prod,
                quantity=product["quantity"],
                purchase_price=prod.purchase_price,
                sale_price=prod.sale_price,
            )
            amount += prod.sale_price * product["quantity"]
            quantity += product["quantity"]
            sales_details.append(sale_detail)

        # Actualizamos la venta
        sale.amount = amount
        sale.quantity = quantity
        sale.save()

        # Creamos el detalle de venta
        SaleDetail.objects.bulk_create(sales_details)

        return Response({"message": "Sale successfully created"})


class RegisterSale1(CreateAPIView):
    serializer_class = SaleProcessSerializer1
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
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

        return Response({"message": "Sale successfully created", "data": f"{serializer.data}"})
