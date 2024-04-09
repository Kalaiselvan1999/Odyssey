from django.urls import path
from account_app.views import SignupView, VerifyEmail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('sign-up/', SignupView.as_view(), name='sign-up'),
    path('log-in/', TokenObtainPairView.as_view(), name='log-in'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('email-verify/', VerifyEmail.as_view(), name='verify-email'),
]
