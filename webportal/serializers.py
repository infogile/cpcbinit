from rest_framework import serializers
from .models import *
from inspections.models import *

class SomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factories
        fields = "__all__"

# SomeModelSerializer(instance).data