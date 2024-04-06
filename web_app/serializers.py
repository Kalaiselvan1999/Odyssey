from rest_framework import serializers
from web_app.models import User, Odyssey, Requests

class RequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requests
        fields = '__all__'

class OdysseySerializer(serializers.ModelSerializer):

    requests = RequestsSerializer(many=True, read_only=True)

    class Meta:
        model = Odyssey
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    odyssies = serializers.SerializerMethodField()
    requested_odyssey = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ("created_at", "modified_on",)

    def get_odyssies(self, obj):
        return [
            {
                'id': odyssey.id,
                'start_date': odyssey.start_date,
                'end_date': odyssey.end_date,
                'from_place': odyssey.from_place.name,
                'destination_place': odyssey.destination_place.name,
                'is_private': odyssey.is_private,
                'users': [{"id": user.id, "user": user.user_name} for user in odyssey.user.all()]
            }
            for odyssey in obj.odysseies_organiser.all()
        ]



    def get_requested_odyssey(self, obj):
        data = obj.requests.all().values("odyssey__organiser__user_name")
        odysseys = [{"odyssies": item["odyssey__organiser__user_name"]} for item in data]
        return odysseys
