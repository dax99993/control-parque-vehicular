from rest_framework import serializers
#from cpv_api.vehicule.models import Vehicule
from Apps.vehicule.models import Vehicule


#class VehiculeAdminSerializer(serializers.HyperlinkedModelSerializer):
class VehiculeAdminSerializer(serializers.ModelSerializer):
    """
        Serializer for Vehicule Model, for editing all fields
        used by AdminUsers
    """
   # url = serializers.HyperlinkedIdentityField(view_name="vehicule-detail",
   #                                            format='html')

    class Meta:
        model = Vehicule
        fields = "__all__"

#class VehiculeUserSerializer(serializers.HyperlinkedModelSerializer):
class VehiculeUserSerializer(serializers.ModelSerializer):
    """
        Serializer for Vehicule Model, for editing certain fields
        used by Users
    """
    #url = serializers.HyperlinkedIdentityField(view_name="vehicule-detail",
    #                                           format='html')

    class Meta:
        model = Vehicule
        fields = [
             #     'url',
                  'branch',
                  'model',
                  'year',
                  'license_plate',
                  'short_name',
                  'photo',
                  #'state',
                  ]

class VehiculeGPSSerializer(serializers.ModelSerializer):
    """
        Serializer for Vehicule Model, for editing GPS location
        used by GPS
    """

    class Meta:
        model = Vehicule
        fields = ['id',
                  'latitude',
                  'longitude',
                  #'state',
                  ]
