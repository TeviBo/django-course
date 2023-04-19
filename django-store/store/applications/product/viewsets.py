# Django Rest Framework
from rest_framework import viewsets
from rest_framework.response import Response

# Models
from .models import Colors, Product

# Serializers
from .serializers import (
    ColorsSerializer,
    ProductSerializer,
    PaginationSerializer,
    ProductSerializerViewSet,
)


class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorsSerializer
    queryset = Colors.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializerViewSet
    queryset = Product.objects.all()
    pagination_class = PaginationSerializer

    def perform_create(self, serializer):
        serializer.save(video="https://www.youtube.com/watch?v=sn88gRoTamI")

    def list(self, request, *args, **kwargs):
        queryset = Product.objects.products_by_user(self.request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
