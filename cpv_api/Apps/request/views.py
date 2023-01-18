from rest_framework import viewsets
from rest_framework.renderers import JsonRender
from rest_framework.response import Response
from Apps.request.models import Request

# Create your views here.
class RequestViewSet(viewsets.ModelViewSet):
    """
    Simple Viewset for viewwing and editing requests
    """

    def get_queryset(self):
        user = self.request.user
        try:
            group = user.groups.all()[0].name
            if group == "admin":
                return Request.objects.all()
            elif group == "normal_user":
                return Request.objects.filter(user=user)
        except:
            return Response({"detail:" : "User does not belong to admin nor normal group user"})

    def get_serializer_class(self):
        user = self.request.user
        group = user.groups.all()[0].name
        if group == "admin":
            return VehiculeAdminSerializer
        elif group == "normal_user":
            return VehiculeUserSerializer
    
    def list(self):
        user = self.request.user
        group = user.groups.all()[0].name

