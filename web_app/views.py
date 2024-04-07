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

    def put(self, request, pk):
        data = request.data
        user_request: Requests = Requests.objects.get(pk=pk)
        if user_request.is_active == True:
            if data['is_accepted'] == True:
                user_request.is_active = False
                user_request.save()
                user_request.odyssey.user.add(user_request.user)
                return Response({"message": "Accepted"}, status=status.HTTP_200_OK)
            elif data['is_accepted'] == False:
                user_request.is_active = False
                user_request.save()
                return Response({"message": "Request has been rejected"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "No records found"}, status=status.HTTP_200_OK)


    def delete(self):
        pass
