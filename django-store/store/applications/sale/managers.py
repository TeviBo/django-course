from django.db import models

class SaleDetailManager(models.Manager):

    def products_by_sale(self, pk):
        return self.filter(sale__pk=pk).order_by('quantity', 'product__name')
