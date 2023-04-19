from django.urls import path

from . import views

app_name = "sale_app"
urlpatterns = [
    path(
        "api/sales/reports/",
        views.SaleReportList.as_view(),
        name="sale-sale-reports",
    ),
    path(
        "api/sales/create/",
        views.RegisterSale.as_view(),
        name="sale-sale-register",
    ),
    path(
        "api/sales/add/",
        views.RegisterSale1.as_view(),
        name="sale-sale-register",
    ),
]
