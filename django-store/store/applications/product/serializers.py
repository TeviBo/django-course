from rest_framework import serializers, pagination

from .models import Product, Colors


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colors
        fields = (
            "id",
            "color",
        )


class ProductSerializer(serializers.ModelSerializer):
    colors = ColorsSerializer(many=True)

    class Meta:
        model = Product
        fields = (
            "name",
            "description",
            "man",
            "woman",
            "weight",
            "purchase_price",
            "sale_price",
            "main_image",
            "image1",
            "image2",
            "image3",
            "image4",
            "colors",
            "video",
            "stock",
            "sales_count",
            "user_created",
        )


class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class ProductSerializerViewSet(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
