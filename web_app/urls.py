from django.urls import path
from .views import Test, UserDetail, RequestDetail

urlpatterns = [
    path('test', Test.as_view(), name='test'),
    path('user/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('request/<int:pk>/', RequestDetail.as_view(), name='reqquest-detail')
]
