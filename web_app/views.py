from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import date

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

    def post(self, request):
        data = request.data
        user = User.objects.get(pk=data.get('user'))
        odyssey = Odyssey.objects.get(pk=data.get('odyssey'))
        Requests.objects.create(user=user, odyssey=odyssey, requested_date=date.today())
        return Response({"message": "Request successfully sent"}, status=status.HTTP_201_CREATED)

class RequestDetail(APIView):

    def put(self, request, pk):
        user_request: Requests = Requests.objects.get(pk=pk)
        if user_request.is_active == True:
            if request.query_params.get('is_accepted'):
                user_request.is_active = False
                user_request.is_accepted = True
                user_request.save()
                user_request.odyssey.user.add(user_request.user)
                return Response({"message": "Accepted"}, status=status.HTTP_200_OK)
            else:
                user_request.is_active = False
                user_request.is_accepted = False
                user_request.save()
                return Response({"message": "Request has been rejected"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No records found"}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user_request: Requests = Requests.objects.get(pk=pk)
        user_request.is_active = False
        user_request.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
