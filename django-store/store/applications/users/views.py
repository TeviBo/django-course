from django.views.generic import TemplateView

# Las aplicaciones de terceros siempre se importan arriba
# Firebase
from firebase_admin import auth

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Serializers
from .serializers import SocialLoginSerializer

# Models
from .models import User


class LoginUser(TemplateView):
    template_name = "users/login.html"


class GoogleLoginView(APIView):
    serializer_class = SocialLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        # Verificar que los datos sean correctos
        serializer.is_valid(raise_exception=True)
        # Recuperar la informacion
        id_token = serializer.validated_data["id_token"]
        # Decodificar el token
        decoded_token = auth.verify_id_token(id_token)
        # Recuperar la informacion del usuario
        email = decoded_token["email"]
        name = decoded_token["name"]
        verified_email = decoded_token["email_verified"]

        # Obtenemos o creamos el usuario
        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                "full_name": name,
                "email": email,
                "is_active": True,
            },
        )

        # Creamos nuestro token interno del proyecto
        if created:
            token = Token.objects.create(user=user)
        else:
            token = Token.objects.get(user=user)

        user = {
            'id': user.pk,
            'email': user.email,
            'full_name': user.full_name,
        }
        return Response({'user': user, 'session': token.key})
