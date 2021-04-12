from .models import TRP
from rest_framework import serializers

class TRPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRP
        fields = '__all__'
        