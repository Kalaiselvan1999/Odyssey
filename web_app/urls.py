from django.urls import path
from .views import Test, UserDetail

urlpatterns = [
    path('test', Test.as_view(), name='test'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
