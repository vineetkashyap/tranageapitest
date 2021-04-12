from django.contrib import admin
from .models import TRP
# Register your models here.
@admin.register(TRP)
class TRPAdmin(admin.ModelAdmin):
    list_display=['business_name','mobile','email','aadhar','address','pan','company_name','gstin','bank_account_no','upload']
