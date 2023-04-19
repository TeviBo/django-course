from django.db import models
from django.db.models import Count


class MeetManager(models.Manager):
    def meet_quantity_by_job(self):
        result = self.values("person__job").annotate(quantity=Count("id"))
        return result
