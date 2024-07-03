from rest_framework import serializers
from .models import Hudud,Organization,Building

class HududSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = '__all__'

class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class BuildingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'

