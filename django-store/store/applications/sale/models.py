from django.db import models
from django.conf import settings

#
from model_utils.models import TimeStampedModel

# local apps
from applications.product.models import Product

# Managers
from .managers import SaleDetailManager


class Sale(TimeStampedModel):
    """Modelo que representa a una Venta Global"""

    INVOICE_TYPE = (
        ("0", "BOLETA"),
        ("3", "FACTURA"),
        ("4", "OTRO"),
    )

    PAYMENT_TYPE = (
        ("0", "TARJETA"),
        ("1", "DEPOSITO"),
        ("2", "CONTRAENTREGA"),
    )

    FLAT_STATE = (
        ("0", "En Proceso"),
        ("1", "En Envio"),
        ("2", "En Tienda"),
        ("3", "Entregado"),
    )
    id = models.AutoField(primary_key=True)
    sale_date = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    invoice_type = models.CharField(max_length=2, choices=INVOICE_TYPE)
    canceled = models.BooleanField(default=False)
    payment_type = models.CharField(max_length=2, choices=PAYMENT_TYPE)
    state = models.CharField(max_length=2, choices=FLAT_STATE, blank=True)
    address = models.TextField(
        blank=True,
    )
    anulate = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="customer",
        # editable=False
    )

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def __str__(self):
        return "Nº [" + str(self.id) + "] - " + str(self.sale_date)


class SaleDetail(TimeStampedModel):
    """Modelo que representa a una venta en detalle"""

    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Sale Code")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=3)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    anulate = models.BooleanField(default=False)
    #

    objects = SaleDetailManager()

    class Meta:
        verbose_name = "Sale Detail"
        verbose_name_plural = "Sales Details"

    def __str__(self):
        return str(self.sale.id) + " - " + str(self.product.name)
