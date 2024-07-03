from django.shortcuts import render
from .models import Hudud,Organization,Building
from .serializers import HududSerializers,OrganizationSerializers,BuildingSerializers
from .permissions import CustomPermission

from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

class HududAPIView(ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializers
    permission_classes = [CustomPermission]

class OrganizationAPIView(ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializers
    permission_classes = [CustomPermission]

class BuildingAPIView(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializers
    permission_classes = [CustomPermission]

