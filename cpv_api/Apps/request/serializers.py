from rest_framework import serializers
from Apps.request.models import Request

class RequestListSerializer(serializers.ModelSerializer):
    """
        Serializer for Request Model, for listing all fields
    """

    class Meta:
        model = Request
        fields = "__all__"

class RequestStateSerializer(serializers.ModelSerializer):
    """
        Serializer for Request Model, for editing state field
        used by AdminUsers
    """

    class Meta:
        model = Request
        fields = "state"

class RequestUserSerializer(serializers.ModelSerializer):
    """
        Serializer for Request Model, for editing certain fields
        used by Users
    """

    class Meta:
        model = Vehicule
        fields = [
             #     'url',
                  'id',
                  'user',
                  'vehicule',
                  'license_plate',
                  'short_name',
                  'photo',
                  #'state',
                  ]


