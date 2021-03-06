# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tblmain',
            fields=[
                ('memberid', models.IntegerField(db_column='MemberID', primary_key=True, serialize=False)),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('firstname', models.CharField(blank=True, db_column='FirstName', max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, db_column='LastName', max_length=50, null=True)),
                ('address', models.CharField(blank=True, db_column='Address', max_length=255, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=50, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=20, null=True)),
                ('postalcode', models.CharField(blank=True, db_column='PostalCode', max_length=20, null=True)),
                ('phonenumber', models.CharField(blank=True, db_column='PhoneNumber', max_length=30, null=True)),
                ('cellnumber', models.CharField(blank=True, db_column='CellNumber', max_length=50, null=True)),
                ('emailaddress', models.CharField(blank=True, db_column='EmailAddress', max_length=50, null=True)),
                ('sex', models.CharField(blank=True, db_column='Sex', max_length=1, null=True)),
                ('dob', models.DateTimeField(blank=True, db_column='DOB', null=True)),
                ('eth', models.CharField(blank=True, db_column='Eth', max_length=50, null=True)),
                ('school', models.CharField(blank=True, db_column='School', max_length=20, null=True)),
                ('grade', models.CharField(blank=True, db_column='Grade', max_length=50, null=True)),
                ('class_field', models.CharField(blank=True, db_column='Class', max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, db_column='Age', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('emergency_contact', models.CharField(blank=True, db_column='Emergency_Contact', max_length=30, null=True)),
                ('emergency_phone', models.CharField(blank=True, db_column='Emergency_Phone', max_length=30, null=True)),
                ('emergency_contact_2', models.CharField(blank=True, db_column='Emergency_Contact_2', max_length=50, null=True)),
                ('emergency_phone_2', models.CharField(blank=True, db_column='Emergency_Phone_2', max_length=50, null=True)),
                ('emergency_contact_3', models.CharField(blank=True, db_column='Emergency_Contact_3', max_length=50, null=True)),
                ('emergency_phone_3', models.CharField(blank=True, db_column='Emergency_Phone_3', max_length=50, null=True)),
                ('emergency_contact_4', models.CharField(blank=True, db_column='Emergency_Contact_4', max_length=50, null=True)),
                ('emergency_phone_4', models.CharField(blank=True, db_column='Emergency_Phone_4', max_length=50, null=True)),
                ('medical', models.TextField(blank=True, db_column='Medical', null=True)),
                ('doctor_name', models.CharField(blank=True, db_column='Doctor_Name', max_length=50, null=True)),
                ('doctor_phone', models.CharField(blank=True, db_column='Doctor_Phone', max_length=50, null=True)),
                ('mothers_name', models.CharField(blank=True, db_column='Mothers_Name', max_length=30, null=True)),
                ('mbusiness_phone', models.CharField(blank=True, db_column='mBusiness_Phone', max_length=30, null=True)),
                ('mcell_phone', models.CharField(blank=True, db_column='mCell_Phone', max_length=30, null=True)),
                ('fathers_name', models.CharField(blank=True, db_column='Fathers_Name', max_length=30, null=True)),
                ('fbusiness_phone', models.CharField(blank=True, db_column='fBusiness_Phone', max_length=30, null=True)),
                ('fcell_phone', models.CharField(blank=True, db_column='fCell_Phone', max_length=30, null=True)),
                ('membership_status', models.CharField(blank=True, db_column='Membership_status', max_length=15, null=True)),
                ('regdate', models.DateTimeField(blank=True, db_column='RegDate', null=True)),
                ('expdate', models.DateTimeField(blank=True, db_column='ExpDate', null=True)),
                ('year_2000_01', models.IntegerField(blank=True, db_column='Year_2000_01', null=True)),
                ('year_2001_02', models.IntegerField(blank=True, db_column='Year_2001_02', null=True)),
                ('year_2002_03', models.IntegerField(blank=True, db_column='Year_2002_03', null=True)),
                ('year_2003_04', models.IntegerField(blank=True, db_column='Year_2003_04', null=True)),
                ('year_2004_05', models.IntegerField(blank=True, db_column='Year_2004_05', null=True)),
                ('year_2005_06', models.IntegerField(blank=True, db_column='Year_2005_06', null=True)),
                ('year_2006_07', models.IntegerField(blank=True, db_column='Year_2006_07', null=True)),
                ('year_2007_08', models.IntegerField(blank=True, db_column='Year_2007_08', null=True)),
                ('year_2008_09', models.IntegerField(blank=True, db_column='Year_2008_09', null=True)),
                ('year_2009_10', models.IntegerField(blank=True, db_column='Year_2009_10', null=True)),
                ('year_2010_11', models.IntegerField(blank=True, db_column='Year_2010_11', null=True)),
                ('year_2011_12', models.IntegerField(blank=True, db_column='Year_2011_12', null=True)),
                ('year_2012_13', models.IntegerField(blank=True, db_column='Year_2012_13', null=True)),
                ('year_2013_14', models.IntegerField(blank=True, db_column='Year_2013_14', null=True)),
                ('year_2014_15', models.IntegerField(blank=True, db_column='Year_2014_15', null=True)),
                ('year_2015_16', models.IntegerField(blank=True, db_column='Year_2015_16', null=True)),
                ('year_2016_17', models.IntegerField(blank=True, db_column='Year_2016_17', null=True)),
                ('year_2017_18', models.IntegerField(blank=True, db_column='Year_2017_18', null=True)),
                ('year_2018_19', models.IntegerField(blank=True, db_column='Year_2018_19', null=True)),
                ('afterschool', models.IntegerField(blank=True, db_column='Afterschool', null=True)),
                ('ost_elementry_osa_field', models.IntegerField(blank=True, db_column='OST Elementry (OSA)', null=True)),
                ('clientcode', models.CharField(blank=True, max_length=50, null=True)),
                ('fund_ez_code', models.CharField(blank=True, db_column='Fund_EZ_Code', max_length=50, null=True)),
                ('user', models.CharField(blank=True, db_column='User', max_length=50, null=True)),
                ('lat', models.FloatField(blank=True, db_column='Lat', null=True)),
                ('lon', models.FloatField(blank=True, db_column='Lon', null=True)),
                ('donotmail', models.IntegerField(blank=True, db_column='DoNotMail', null=True)),
                ('wrongaddress', models.IntegerField(blank=True, db_column='WrongAddress', null=True)),
                ('lastactivity', models.DateTimeField(blank=True, db_column='LastActivity', null=True)),
                ('combo', models.CharField(blank=True, db_column='Combo', max_length=255, null=True)),
                ('invalidaddress', models.IntegerField(blank=True, db_column='InvalidAddress', null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tblMain',
            },
        ),
    ]
