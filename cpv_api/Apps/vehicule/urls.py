from rest_framework import routers
from Apps.vehicule import views
from django.urls import path, include

router = routers.SimpleRouter()
router.register(r'vehicules', views.VehiculeViewSet, basename='vehicule')

urlpatterns = router.urls
