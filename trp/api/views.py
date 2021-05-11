from django.shortcuts import render
from .models import *
from .serializers import  *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# # Create your views here.
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# @api_view(['GET'])
# def student_data(request):
#     if request.method =='GET':
#         id = request.data.get('id',None)
#         if id is not None:
#             stu = TruckOwnerModel.objects.get(email_id=id)
#             serializer = TruckOwnerModelSerializer(stu)
#             return  Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             stu =TruckOwnerModel.objects.all()
#             serializer = TruckOwnerModelSerializer(stu,many=True)
#             return  Response(serializer.data,status=status.HTTP_200_OK)
# class TruckOwnerModel_View(ModelViewSet):
#     queryset  = TruckOwnerModel.objects.all()
#     serializer_class = TruckOwnerModelSerializer
#     authetication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
# class TruckOwnerVehicleRegistraionModel_View(ModelViewSet):
#     queryset  = TruckOwnerVehicleRegistraionModel.objects.all()
#     serializer_class = TruckOwnerVehicleRegistraionModelSerializer
#     authetication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
# class TruckOwnerDriverRegistration_View(ModelViewSet):
#     queryset  = TruckOwnerDriverRegistration.objects.all()
#     serializer_class = TruckOwnerDriverRegistrationSerializer
#     authetication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]

# ############Transporter Views################
# class TransporterModel_View(ModelViewSet):
#     queryset  = TransporterModel.objects.all()
#     serializer_class = TransporterModelSerializer
#     authetication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
# class TransporterVehicleRegistraionModel_View(ModelViewSet):
#     queryset  = TransporterVehicleRegistraionModel.objects.all()
#     serializer_class = TransporterVehicleRegistraionModelSerializer
#     authetication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]
# class TranspoterDriverRegistration_View(ModelViewSet):
#     queryset  = TruckOwnerDriverRegistration.objects.all()
#     serializer_class = TruckOwnerDriverRegistrationSerializer
#     authetication_classes = [SessionAuthentication]
#     permission_classes = [IsAuthenticated]




from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class TruckOwnerModel_View(viewsets.ViewSet):
    def list(self,request):
        stu=TruckOwnerModel.objects.all()
        serializers = TruckOwnerModelSerializer(stu,many=True)
        return Response(serializers.data)
    def retrieve(self,request,pk=None):
        id =pk
        if id is not  None:
            stu = TruckOwnerModel.objects.get(id=id)
            serializers= TruckOwnerModelSerializer(stu)
            return Response(serializers.data)
    def  create(self,request):
        serializers = TruckOwnerModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            res ={'msg':'data inserted successfully'}
            return Response(res,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    def  partial_update(self,request,pk):
        id=pk
        stu=TruckOwnerModel.objects.get(id=id)
        serializer= TruckOwnerModelSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res ={"msg":"data updated successfully"}
            return Response(res,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def  update(self,request,pk):
        id=pk
        stu=TruckOwnerModel.objects.get(id=id)
        serializer= TruckOwnerModelSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            res ={"msg":"data updated successfully"}
            return Response(res,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        id=pk
        stu=TruckOwnerModel.objects.get(id=id)
        stu.delete()
        res={"msg":"data deleted"}
        return Response(res,status=status.HTTP_200_OK)