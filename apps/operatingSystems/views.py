from rest_framework import serializers, viewsets

from .models import OperatingSystem

class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = ('id', 'name', 'description', 'created_at', 'updated_at',)

class ModelViewSet(viewsets.ModelViewSet):
    queryset = OperatingSystem.objects.all()
    serializer_class = OperatingSystemSerializer
