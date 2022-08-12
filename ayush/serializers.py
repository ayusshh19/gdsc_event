from rest_framework import serializers
from .models import Eventmanage

class Eventserializer(serializers.ModelSerializer):
    class Meta:
        model = Eventmanage
        fields='__all__'

