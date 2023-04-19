"""Persona views."""

from django.views.generic import ListView
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
)

from .models import Person, Hobby, Meet
from .serializers import (
    PersonSerializer,
    PersonaSerializer2,
    HobbySerializer,
    MeetSerializer,
    MeetSerializerLink,
    CountMeetSerializer,
)


class ListaPersonas(ListView):
    """ListaPersonas."""

    template_name = "persona/personas.html"
    context_object_name = "person_list"

    def get_queryset(self):
        return Person.objects.all()


class PersonListApiView(ListAPIView):
    """PersonListApiView."""

    serializer_class = PersonSerializer
    pagination_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()


class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        kword = self.kwargs["kword"]
        return Person.objects.filter(full_name__icontains=kword)


class PersonCreateView(CreateAPIView):
    """PersonCreateView."""

    serializer_class = PersonSerializer


class PersonDetailView(RetrieveAPIView):
    """PersonDetailView."""

    serializer_class = PersonSerializer
    queryset = Person.objects.filter()


class PersonDeleteView(DestroyAPIView):
    """
    PersonDeleteView.
    """

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonUpdateView(UpdateAPIView):
    """PersonUpdateView."""

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonRetrieveUpdateView(RetrieveUpdateAPIView):
    """PersonRetrieveUpdateView."""

    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class PersonaListApiView(ListAPIView):
    """List all persons."""

    serializer_class = PersonaSerializer2

    def get_queryset(self):
        """Return all persons."""
        return Person.objects.all()


class HobbyListApiView(ListAPIView):
    """List all hobbies."""

    serializer_class = HobbySerializer

    def get_queryset(self):
        """Return all hobbies."""
        return Hobby.objects.all()


class CreateHobbyView(CreateAPIView):
    """Create a new hobby."""

    serializer_class = HobbySerializer


class MeetListApiView(ListAPIView):
    """List all meets."""

    serializer_class = MeetSerializer

    def get_queryset(self):
        """Return all meets."""
        return Meet.objects.all()


class MeetListApiViewLink(ListAPIView):
    """List all meets."""

    serializer_class = MeetSerializerLink

    def get_queryset(self):
        """Return all meets."""
        return Meet.objects.all()


class MeetsByPersonJob(ListAPIView):
    """List all meets."""

    serializer_class = CountMeetSerializer

    def get_queryset(self):
        """Return all meets."""
        return Meet.objects.meet_quantity_by_job()


class CreateMeetView(CreateAPIView):
    """Create a new meet."""

    serializer_class = MeetSerializer
