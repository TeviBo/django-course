#
#
from django.db import models
from model_utils.models import TimeStampedModel
from .managers import MeetManager


#
class Hobby(TimeStampedModel):
    """
    Modelo para registrar hobbies de una persona.

    TimeStapmedModel: agrega campos de fecha de creacion y actualizacion
    """

    id = models.AutoField(primary_key=True)
    hobby = models.CharField(
        max_length=50,
    )

    class Meta:
        verbose_name = "Hobby"
        verbose_name_plural = "Hobbies"

    def __str__(self):
        """Retorna el nombre del hobby."""
        return str(str(self.id) + self.hobby)


class Person(TimeStampedModel):
    """Modelo para registrar personas de una agenda."""

    full_name = models.CharField(
        max_length=50,
    )
    job = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(
        max_length=15,
        blank=True,
    )
    hobbies = models.ManyToManyField(Hobby)

    class Meta:
        """Meta."""

        verbose_name = "Person"
        verbose_name_plural = "People"

    def __str__(self):
        """Retorna el nombre de la persona."""
        return str(self.full_name)


class Meet(TimeStampedModel):
    """Modelo para registrar reuniones de una persona."""

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="meet",
    )
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True, null=True)

    objects = MeetManager()

    class Meta:
        """Meta."""

        verbose_name = "Meet"
        verbose_name_plural = "Meets"

    def __str__(self):
        """Retorna la descripcion de la reunion."""
        return str(self.description)
