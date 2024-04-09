import random
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import ValidationError

from web_app.models import User
from account_app.tasks import send_mail

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

        otp = random.randint(100000, 999999)
        user = User.objects.create(email=email, user_name=user_name, password=make_password(password_1), otp=otp)
        send_mail.delay(user.email, f"Welcome to odyssey. This is your OTP {otp}")
        refresh = RefreshToken.for_user(user)
        data = {'refresh': str(refresh),
                'access': str(refresh.access_token)}
        return Response(data, status=status.HTTP_201_CREATED)



class LoginView(APIView):

    def post(self, request):
        pass


class VerifyEmail(APIView):

    def post(self, request):
        user = User.objects.get(id=request.data.get('user_id'))
        if user.otp == request.data.get('otp'):
            user.is_email_verified = True
            user.save()
            return Response({"data":  "OTP Verified"})
        return Response({"message": "OTP does not match"})
