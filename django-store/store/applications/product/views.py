# REST framework
from rest_framework.generics import ListAPIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Serializers
from .serializers import ProductSerializer

# Models
from .models import Product


class ProductByUser(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.products_by_user(user)


class ProductStockView(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Product.objects.products_with_stock()


class ProductByGender(ListAPIView):
    serializer_class = ProductSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [
    #     IsAuthenticated,
    # ]

    def get_queryset(self):
        gender = self.kwargs["gender"]
        return Product.objects.products_by_gender(gender)


class ProductFilter(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        man = self.request.query_params.get("man", None)
        woman = self.request.query_params.get("woman", None)
        name = self.request.query_params.get("name", None)
        return Product.objects.product_filter(man=man, woman=woman, name=name)
