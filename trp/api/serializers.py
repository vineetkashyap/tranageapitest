from .models import *
from rest_framework import serializers
class TruckOwnerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TruckOwnerModel
        fields  = '__all__'
class TruckOwnerVehicleRegistraionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TruckOwnerVehicleRegistraionModel
        fields  = '__all__'
class TruckOwnerDriverRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model =TruckOwnerDriverRegistration
        fields  = '__all__'
class TransporterModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TransporterModel
        fields  = '__all__'
class TransporterVehicleRegistraionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model =TransporterVehicleRegistraionModel
        fields  = '__all__'
class TranspoterDriverRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model =TranspoterDriverRegistration
        fields  = '__all__'
class Tranage_AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Tranage_Agent
        fields  = '__all__'
        
