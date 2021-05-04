from django.db import models

# Create your models here.
#################TRUCK OWNER#######################################################
class TruckOwnerModel(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    alternate_mobile_number = models.CharField(max_length=50)
    email_id  = models.EmailField(max_length=254)
    address  = models.CharField(max_length=50)
    aadhar_number = models.IntegerField()
    pan_number = models.CharField(max_length=50)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    aadhar_xerox = models.FileField(upload_to='media', max_length=100)
    pan_card_xerox = models.FileField(upload_to='media', max_length=100)
    cancelled_cheque_xerox = models.FileField(upload_to='media', max_length=100)
    photo = models.FileField(upload_to='media', max_length=100)
    sign = models.FileField(upload_to='media', max_length=100)

class TruckOwnerVehicleRegistraionModel(models.Model):
    truck_owner = models.ForeignKey(TruckOwnerModel,on_delete=models.CASCADE)
    vehicle_registration_number = models.CharField(max_length=50)
    owner_name  =models.CharField(max_length=50)
    owner_contact_number = models.IntegerField()
    vehicle_model_number = models.CharField(max_length=50)
    vehicle_type = models.CharField( max_length=50)
    wheel_type  =models.CharField(max_length=50)
    maximum_load_capacity = models.CharField(max_length=50)
    insurance_expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    preference_product = models.CharField(max_length=50)
    preferred_location = models.CharField(max_length=50)
    vehicle_front_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_back_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_left_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_right_photo= models.FileField( upload_to='media', max_length=100)
    registration_certificate= models.FileField( upload_to='media', max_length=100)
    fitness_certificate = models.FileField( upload_to='media', max_length=100)
    pollution_certificate= models.FileField( upload_to='media', max_length=100)
    permit_certificate= models.FileField( upload_to='media', max_length=100)
    insurance_certificate= models.FileField( upload_to='media', max_length=100)

class TruckOwnerDriverRegistration(models.Model):
    truck_owner = models.ForeignKey(TruckOwnerModel,on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    alternate_number = models.IntegerField()
    father_mobile_number = models.IntegerField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField( max_length=254)
    address = models.CharField(max_length=200)
    aadhar_number = models.IntegerField()
    pan_number = models.CharField( max_length=50)
    dl_number = models.CharField(max_length=50)
    dl_type = models.CharField( max_length=50)
    dl_expiry_date = models.DateField( auto_now=False, auto_now_add=False)
    experience =models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='media', max_length=100)
    aadhar_front = models.FileField(upload_to='media', max_length=100)
    aadhar_back = models.FileField(upload_to='media', max_length=100)
    pan_xerox = models.FileField(upload_to='media', max_length=100)
    dl_front = models.FileField(upload_to='media', max_length=100)
    dl_back = models.FileField(upload_to='media', max_length=100)
    passbook_or_cheque = models.FileField(upload_to=None, max_length=100)




#################TRANSPORTER#######################################################
class TransporterModel(models.Model):
    business_name = models.CharField(max_length=500)
    contact_person = models.CharField(max_length=500)
    mobile = models.IntegerField()
    alternarte_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=500)
    gstin = models.CharField(max_length=50)
    pan_number = models.CharField(max_length=50)
    bank_account_name = models.CharField(max_length=100)
    bank_account_number = models.IntegerField()
    ifsc_code = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=100)
    branch_name = models.CharField(max_length=100)
    gstin_certificate = models.FileField(upload_to='media', max_length=100)
    pan_card_xerox = models.FileField(upload_to='media', max_length=100)
    cancelled_cheque = models.FileField(upload_to='media', max_length=100)

class TransporterVehicleRegistraionModel(models.Model):
    transporter = models.ForeignKey(TransporterModel,on_delete=models.CASCADE)
    vehicle_registration_number = models.CharField(max_length=50)
    owner_name  =models.CharField(max_length=50)
    owner_contact_number = models.IntegerField()
    vehicle_model_number = models.CharField(max_length=50)
    vehicle_type = models.CharField( max_length=50)
    wheel_type  =models.CharField(max_length=50)
    maximum_load_capacity = models.CharField(max_length=50)
    insurance_expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    preference_product = models.CharField(max_length=50)
    preferred_location = models.CharField(max_length=50)
    vehicle_front_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_back_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_left_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_right_photo= models.FileField( upload_to='media', max_length=100)
    registration_certificate= models.FileField( upload_to='media', max_length=100)
    fitness_certificate = models.FileField( upload_to='media', max_length=100)
    pollution_certificate= models.FileField( upload_to='media', max_length=100)
    permit_certificate= models.FileField( upload_to='media', max_length=100)
    insurance_certificate= models.FileField( upload_to='media', max_length=100)

class TranspoterDriverRegistration(models.Model):
    transporter = models.ForeignKey(TransporterModel,on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    alternate_number = models.IntegerField()
    father_mobile_number = models.IntegerField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField( max_length=254)
    address = models.CharField(max_length=200)
    aadhar_number = models.IntegerField()
    pan_number = models.CharField( max_length=50)
    dl_number = models.CharField(max_length=50)
    dl_type = models.CharField( max_length=50)
    dl_expiry_date = models.DateField( auto_now=False, auto_now_add=False)
    experience =models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='media', max_length=100)
    aadhar_front = models.FileField(upload_to='media', max_length=100)
    aadhar_back = models.FileField(upload_to='media', max_length=100)
    pan_xerox = models.FileField(upload_to='media', max_length=100)
    dl_front = models.FileField(upload_to='media', max_length=100)
    dl_back = models.FileField(upload_to='media', max_length=100)
    passbook_or_cheque = models.FileField(upload_to=None, max_length=100)


#################AGENT #######################################################
class Tranage_Agent(models.Model):
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    alternate_mobile_number = models.CharField(max_length=50)
    email_id  = models.EmailField(max_length=254)
    address  = models.CharField(max_length=50)
    aadhar_number = models.IntegerField()
    pan_number = models.CharField(max_length=50)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    aadhar_xerox = models.FileField(upload_to='media', max_length=100)
    pan_card_xerox = models.FileField(upload_to='media', max_length=100)
    cancelled_cheque_xerox = models.FileField(upload_to='media', max_length=100)
    photo = models.FileField(upload_to='media', max_length=100)
    sign = models.FileField(upload_to='media', max_length=100)


class Tranage_Agent_VehicleRegistraionModel(models.Model):
    agent = models.ForeignKey(Tranage_Agent,on_delete=models.CASCADE)
    vehicle_registration_number = models.CharField(max_length=50)
    owner_name  =models.CharField(max_length=50)
    owner_contact_number = models.IntegerField()
    vehicle_model_number = models.CharField(max_length=50)
    vehicle_type = models.CharField( max_length=50)
    wheel_type  =models.CharField(max_length=50)
    maximum_load_capacity = models.CharField(max_length=50)
    insurance_expiry_date = models.DateField(auto_now=False, auto_now_add=False)
    preference_product = models.CharField(max_length=50)
    preferred_location = models.CharField(max_length=50)
    vehicle_front_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_back_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_left_photo= models.FileField( upload_to='media', max_length=100)
    vehicle_right_photo= models.FileField( upload_to='media', max_length=100)
    registration_certificate= models.FileField( upload_to='media', max_length=100)
    fitness_certificate = models.FileField( upload_to='media', max_length=100)
    pollution_certificate= models.FileField( upload_to='media', max_length=100)
    permit_certificate= models.FileField( upload_to='media', max_length=100)
    insurance_certificate= models.FileField( upload_to='media', max_length=100)

class Tranage_Agent_DriverRegistration(models.Model):
    agent = models.ForeignKey(Tranage_Agent,on_delete=models.CASCADE)
    driver_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mobile_number = models.IntegerField()
    alternate_number = models.IntegerField()
    father_mobile_number = models.IntegerField()
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField( max_length=254)
    address = models.CharField(max_length=200)
    aadhar_number = models.IntegerField()
    pan_number = models.CharField( max_length=50)
    dl_number = models.CharField(max_length=50)
    dl_type = models.CharField( max_length=50)
    dl_expiry_date = models.DateField( auto_now=False, auto_now_add=False)
    experience =models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    bank_account_name = models.CharField( max_length=50)
    bank_account_number = models.IntegerField()
    ifsc_code  = models.CharField(max_length=50)
    bank_name = models.CharField( max_length=50)
    branch_name = models.CharField(max_length=50)
    photo = models.FileField(upload_to='media', max_length=100)
    aadhar_front = models.FileField(upload_to='media', max_length=100)
    aadhar_back = models.FileField(upload_to='media', max_length=100)
    pan_xerox = models.FileField(upload_to='media', max_length=100)
    dl_front = models.FileField(upload_to='media', max_length=100)
    dl_back = models.FileField(upload_to='media', max_length=100)
    passbook_or_cheque = models.FileField(upload_to=None, max_length=100)