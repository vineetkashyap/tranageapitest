# Generated by Django 3.0.5 on 2021-05-11 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TruckOwnerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('father_name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=50, unique=True)),
                ('alternate_mobile_number', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254, unique=True)),
                ('address', models.CharField(max_length=50)),
                ('aadhar_number', models.CharField(max_length=50, unique=True)),
                ('pan_number', models.CharField(max_length=50, unique=True)),
                ('bank_account_name', models.CharField(max_length=50)),
                ('bank_account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=50)),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('aadhar_front', models.FileField(upload_to='media')),
                ('aadhar_back', models.FileField(upload_to='media')),
                ('pan_card_front', models.FileField(upload_to='media')),
                ('cancelled_cheque', models.FileField(upload_to='media')),
                ('owner_image', models.FileField(upload_to='media')),
                ('sign', models.FileField(upload_to='media')),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('registered_by', models.CharField(max_length=50)),
                ('user_type', models.CharField(max_length=50)),
            ],
        ),
    ]
