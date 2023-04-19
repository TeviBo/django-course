# Rest Framework
from rest_framework import serializers

# Models
from .models import Sale, SaleDetail


class SaleReportSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        model = Sale
        fields = (
            "sale_date",
            "amount",
            "quantity",
            "invoice_type",
            "canceled",
            "payment_type",
            "state",
            "address",
            "anulate",
            "user",
            "products",
        )

    def get_products(self, obj):
        return SaleDetailProductSerializer(
            SaleDetail.objects.products_by_sale(obj.pk), many=True
        ).data


class SaleDetailProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = (
            "id",
            "sale",
            "product",
            "quantity",
            "purchase_price",
            "sale_price",
        )


class ProductSaleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class ArrayIntegerSerializer(serializers.ListField):
    child = serializers.IntegerField()


class SaleProcessSerializer(serializers.Serializer):
    invoice_type = serializers.CharField()
    payment_type = serializers.CharField()
    address = serializers.CharField()
    products = ProductSaleSerializer(many=True)


# ListFile serializer
class SaleProcessSerializer1(serializers.Serializer):
    invoice_type = serializers.CharField()
    payment_type = serializers.CharField()
    address = serializers.CharField()
    products = ArrayIntegerSerializer()
    quantity = ArrayIntegerSerializer()

    def validate(self, attrs):
        if attrs["payment_type"] not in dict(Sale.PAYMENT_TYPE):
            raise serializers.ValidationError("El tipo de pago es incorrecto")
        if attrs["invoice_type"] not in dict(Sale.INVOICE_TYPE):
            raise serializers.ValidationError("El tipo de factura es incorrecto")
        return attrs
