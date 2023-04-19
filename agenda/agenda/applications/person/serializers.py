from rest_framework import serializers, pagination

from .models import Person, Hobby, Meet


class PersonaSerializer2(serializers.ModelSerializer):
    active = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = "__all__"


class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ("id", "hobby")
        read_only_fields = ["id"]


class PersonSerializer(serializers.ModelSerializer, pagination.PageNumberPagination):
    hobbies = HobbySerializer(many=True)
    active = serializers.BooleanField(required=False)
    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100

    class Meta:
        model = Person
        fields = ("id", "full_name", "job", "email", "phone", "hobbies", "active")


class MeetSerializerLink(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meet
        fields = ("id", "person", "date", "time", "description")
        extra_kwargs = {
            "person": {"view_name": "person_app:person-detail", "lookup_field": "pk"}
        }


class MeetSerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    datetime = serializers.SerializerMethodField()

    class Meta:
        model = Meet
        fields = ("id", "person", "date", "time", "description", "datetime")

    def get_datetime(self, obj):
        return f"{str(obj.date)} - {str(obj.time)}"


class CountMeetSerializer(serializers.Serializer):
    person__job = serializers.CharField()
    quantity = serializers.IntegerField()
