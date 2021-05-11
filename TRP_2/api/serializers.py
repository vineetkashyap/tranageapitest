from .models import *
from rest_framework import serializers
class TruckOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TruckOwnerModel
        fields  = '__all__'