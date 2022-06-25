from rest_framework import serializers
from .models import Doctor, Direction


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = "__all__"
