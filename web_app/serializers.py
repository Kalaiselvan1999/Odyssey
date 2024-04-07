from rest_framework import serializers
from web_app.models import User, Odyssey, Requests, State

class ActiveRequestSerializer(serializers.ListSerializer):

    def to_representation(self, instance):
        return super(ActiveRequestSerializer, self).to_representation(instance.filter(is_active=True))

class RequestsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Requests
        list_serializer_class = ActiveRequestSerializer
        exclude = ("created_at", "modified_on")

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        exclude = ("created_at", "modified_on")

class OdysseySerializer(serializers.ModelSerializer):

    odyssies = RequestsSerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()
    from_place = serializers.PrimaryKeyRelatedField(source="from_place.name", read_only=True)
    destination_place = serializers.PrimaryKeyRelatedField(source="destination_place.name", read_only=True)


    class Meta:
        model = Odyssey
        exclude = ("created_at", "modified_on")

    def get_user(self, obj):
        return obj.user.all().values("id", "user_name", "first_name", "last_name")

class UserSerializer(serializers.ModelSerializer):

    odysseies_organiser = OdysseySerializer(many=True, read_only=True)
    requests = RequestsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        exclude = ("created_at", "modified_on",)

