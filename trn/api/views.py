from django.shortcuts import render
from .models import TRP
from .serializers import TRPSerializer
from rest_framework import viewsets

# Create your views here.
class TRPModelViewSet(viewsets.ModelViewSet):
    queryset = TRP.objects.all()
    serializer_class = TRPSerializer


