from django.db import models


class ProductManager(models.Manager):
    def products_by_user(self, user):
        return self.filter(user_created=user)

    def products_with_stock(self):
        return self.filter(stock__gt=0).order_by("-sales_count")

    def products_by_gender(self, gender):
        if gender.lower() == "male":
            woman = False
            man = True
        elif gender.lower() == "female":
            woman = True
            man = False
        else:
            woman = True
            man = True
        return self.filter(woman=woman, man=man).order_by("created")

    def product_filter(self, **filters):
        return self.filter(
            woman=filters["woman"], man=filters["man"], name__icontains=filters["name"]
        )
