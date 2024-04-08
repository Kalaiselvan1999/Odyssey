from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError

from web_app.models import User

# Create your views here.


class SignupView(APIView):

    def post(self, request):
        user_name = request.data.get('username')
        email = request.data.get('email')
        password_1 = request.data.get('password_1')
        password_2 = request.data.get('password_2')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")

        if password_1 != password_2:
            raise ValidationError("Password does not match")

        user = User.objects.create(email=email, user_name=user_name, password=make_password(password_1))
        refresh = RefreshToken.for_user(user)
        data = {'refresh': str(refresh),
                'access': str(refresh.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)



class LoginView(APIView):

    def post(self, request):
        pass