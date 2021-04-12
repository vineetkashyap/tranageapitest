from django.db import models

# Create your models here.
class TRP(models.Model):
    business_name=models.CharField(max_length=500)
    mobile=models.IntegerField(max_length=500)
    email=models.EmailField(max_length=254)
    aadhar=models.IntegerField()
    address=models.CharField(max_length=500)
    pan=models.CharField(max_length=50)
    company_name= models.CharField(max_length=500)
    gstin=models.CharField(max_length=50)
    bank_account_no=models.IntegerField()
    upload=models.FileField(upload_to='docu', max_length=100)