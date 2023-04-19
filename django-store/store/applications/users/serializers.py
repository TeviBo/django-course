from rest_framework import serializers


class SocialLoginSerializer(serializers.Serializer):
    id_token = serializers.CharField(required=True)
