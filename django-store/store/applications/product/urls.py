from django.urls import path
from . import views

app_name = "product_app"
urlpatterns = [
    path(
        "api/products/by-user",
        views.ProductByUser.as_view(),
        name="product-product-by_user",
    ),
    path(
        "api/products/stock",
        views.ProductByUser.as_view(),
        name="product-product-stock",
    ),
    path(
        "api/products/by-gender/<gender>",
        views.ProductByGender.as_view(),
        name="product-product-by-gender",
    ),
    path(
        "api/products/filter/",
        views.ProductFilter.as_view(),
        name="product-product-filter",
    ),
]
