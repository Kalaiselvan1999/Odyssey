from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from web_app.models import User, Odyssey, Requests
from web_app.serializers import UserSerializer
# Create your views here.
class Test(APIView):

    def get(self, request):
        return Response({"message": "Successs"}, status=status.HTTP_200_OK)

class UserList(APIView):

    def post(self, request):
        pass

class UserDetail(APIView):

    def get(self, request, pk):
        user = User.objects.prefetch_related('odysseies_organiser').get(pk=pk)
        serializer = UserSerializer(user)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

class OdysseyList(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass

class OdysseyDetail(APIView):

    def get(self, request, pk):
        pass

    def put(self, request, pk):
        pass

    def delete(self, request, pk):
        pass

class RequestList(APIView):

    def get(self, request):
        pass

    def post(self, request):
        pass

class RequestDetail(APIView):

    def delete(self):
        pass
