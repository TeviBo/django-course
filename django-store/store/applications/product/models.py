from django.db import models
from django.conf import settings

#
from model_utils.models import TimeStampedModel

# Managers
from .managers import ProductManager


class Colors(models.Model):
    """Representa color de un producto"""

    id = models.AutoField(primary_key=True)
    color = models.CharField("Tag", max_length=120, unique=True)
    #

    class Meta:
        verbose_name = "Product Color"
        verbose_name_plural = "Colors"

    def __str__(self):
        return str(self.id) + " - " + str(self.color)


class Product(TimeStampedModel):
    """Modelo que representa a un producto de tienda"""

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    man = models.BooleanField(default=True)
    woman = models.BooleanField(default=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=1)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=3)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to="product")
    image1 = models.ImageField(
        blank=True,
        null=True,
        upload_to="product",
    )
    image2 = models.ImageField(
        blank=True,
        null=True,
        upload_to="product",
    )
    image3 = models.ImageField(
        blank=True,
        null=True,
        upload_to="product",
    )
    image4 = models.ImageField(
        blank=True,
        null=True,
        upload_to="product",
    )
    colors = models.ManyToManyField(Colors)
    video = models.URLField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    sales_count = models.PositiveIntegerField(default=0)
    user_created = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="prod_created",
    )

    objects = ProductManager()

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return str(self.id) + " " + str(self.name)
