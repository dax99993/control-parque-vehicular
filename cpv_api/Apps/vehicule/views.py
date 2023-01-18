#from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import get_object_or_404

from Apps.vehicule.models import Vehicule 
from Apps.vehicule.serializers import VehiculeAdminSerializer, VehiculeUserSerializer, VehiculeGPSSerializer

# Create your views here.

class VehiculeViewSet(viewsets.ModelViewSet):
    """
        List and create Vehicules
    """
    model = Vehicule

    permission_classes = [IsAuthenticated]

    #def get_object(self, pk):
    #    return get_object_or_404(self.model, pk)



    def get_serializer_class(self):
        user = self.request.user
        if user.is_admin:
            return VehiculeAdminSerializer
        elif user.is_gps:
            return VehiculeGPSSerializer
        elif user.is_regular:
            return VehiculeUserSerializer
        else:
            return Response({
                "detail": "User does not belong to neither admin, gps nor regular group"
                },
                status=status.HTTP_403_FORBIDDEN
                )


    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Vehicule.objects.all()
        elif user.is_gps:
            return Vehicule.objects.filter(is_active=True, state="occupied")
        elif user.is_regular:
            return Vehicule.objects.filter(is_active=True, state="available")
        else:
            return Response({
                "detail": "User does not belong to neither admin, gps nor normal group"
                },
                status=status.HTTP_403_FORBIDDEN
                )

    @action(detail=True, methods=['patch'])
    def set_as_inactive(self, request, pk):
        """
            Set vehicule as inactive in the database
        """
        pass
