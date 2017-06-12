# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Class1(models.Model):
    classnumber = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    fiscal_year = models.CharField(db_column='fiscal year', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    period = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    time = models.CharField(max_length=50, blank=True, null=True)
    instructor = models.CharField(max_length=50, blank=True, null=True)
    maxsize = models.CharField(max_length=50, blank=True, null=True)
    openstatus = models.CharField(max_length=50, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    enterdate = models.DateTimeField(db_column='EnterDate', blank=True, null=True)  # Field name made lowercase.
    room_location = models.CharField(db_column='Room Location', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    autofill = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = 'Classe'
        managed = False
        db_table = 'class1'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Mem(models.Model):
    mem_id = models.IntegerField(primary_key=True)
    mem_name = models.CharField(max_length=45)
    address = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'mem'


class Registration(models.Model):
    registrationnumber = models.AutoField(primary_key=True)
    mem_id = models.ForeignKey('Tblmain', models.DO_NOTHING, blank=True,db_column='mem_id', null=True,verbose_name='Member')
    #phone = models.CharField(max_length=50, blank=True, null=True)
    classnumber = models.ForeignKey(Class1, models.DO_NOTHING, db_column='classnumber', blank=True, null=True, verbose_name='Class')
    attendance = models.CharField(max_length=50, blank=True, null=True)
    #memberid = models.IntegerField(db_column='memberID', blank=True, null=True)  # Field name made lowercase.
    receipt = models.CharField(max_length=50, blank=True, null=True)
    fee = models.FloatField(db_column='Fee', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(blank=True, null=True)
    description = models.CharField(db_column='Description', max_length=45, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.registrationnumber)
    class Meta:

        managed = False
        db_table = 'registration'


class ServersServer(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=39)
    order = models.IntegerField()
    mem = models.ForeignKey(Mem, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'servers_server'


class Tblmain(models.Model):
    mem_id = models.AutoField(primary_key=True)
    #date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cellnumber = models.CharField(db_column='CellNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True, verbose_name='Date Of Birth')  # Field name made lowercase.
    #emergency_phone_3 = models.CharField(db_column='Emergency_Phone_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    #invalidaddress = models.IntegerField(db_column='InvalidAddress', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return str(self.firstname)
    class Meta:
        verbose_name = 'Member'
        managed = False
        db_table = 'tblMain'


class Tblmain1(models.Model):
    memberid = models.IntegerField(db_column='memberID', blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cellnumber = models.CharField(db_column='CellNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    mbusiness_phone = models.CharField(db_column='mBusiness_Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    mcell_phone = models.CharField(db_column='mCell_Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fathers_name = models.CharField(db_column='Fathers_Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fbusiness_phone = models.CharField(db_column='fBusiness_Phone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    membership_status = models.CharField(db_column='Membership_status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    expdate = models.DateTimeField(db_column='ExpDate', blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    combo = models.CharField(db_column='Combo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mem_id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'tblMain_1'


class TblmainDuplicate(models.Model):
    mem_id = models.AutoField(primary_key=True)
    memberid = models.IntegerField(db_column='MemberID', unique=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=30, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=255, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=50, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='PhoneNumber', max_length=30, blank=True, null=True)  # Field name made lowercase.
    cellnumber = models.CharField(db_column='CellNumber', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    eth = models.CharField(db_column='Eth', max_length=50, blank=True, null=True)  # Field name made lowercase.
    school = models.CharField(db_column='School', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grade = models.CharField(db_column='Grade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    emergency_phone_3 = models.CharField(db_column='Emergency_Phone_3', max_length=50, blank=True, null=True)  # Field name made lowercase.
    regdate = models.DateTimeField(db_column='RegDate', blank=True, null=True)  # Field name made lowercase.
    expdate = models.DateTimeField(db_column='ExpDate', blank=True, null=True)  # Field name made lowercase.
    year_2006_07 = models.IntegerField(db_column='Year_2006_07', blank=True, null=True)  # Field name made lowercase.
    ost_elementry_osa_field = models.IntegerField(db_column='OST Elementry (OSA)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    clientcode = models.CharField(max_length=50, blank=True, null=True)
    fund_ez_code = models.CharField(db_column='Fund_EZ_Code', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='Lon', blank=True, null=True)  # Field name made lowercase.
    donotmail = models.IntegerField(db_column='DoNotMail', blank=True, null=True)  # Field name made lowercase.
    wrongaddress = models.IntegerField(db_column='WrongAddress', blank=True, null=True)  # Field name made lowercase.
    lastactivity = models.DateTimeField(db_column='LastActivity', blank=True, null=True)  # Field name made lowercase.
    combo = models.CharField(db_column='Combo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    invalidaddress = models.IntegerField(db_column='InvalidAddress', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tblMain_duplicate'


class Tblmembers(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    memberid = models.IntegerField(db_column='MemberID', blank=True, null=True)  # Field name made lowercase.
    marital_st = models.CharField(db_column='Marital_St', max_length=10, blank=True, null=True)  # Field name made lowercase.
    member_cat = models.CharField(db_column='Member_Cat', max_length=27, blank=True, null=True)  # Field name made lowercase.
    year = models.CharField(db_column='Year', max_length=50, blank=True, null=True)  # Field name made lowercase.
    scholarship = models.CharField(db_column='Scholarship', max_length=50, blank=True, null=True)  # Field name made lowercase.
    m_notes = models.TextField(db_column='M_Notes', blank=True, null=True)  # Field name made lowercase.
    splastname = models.CharField(db_column='SpLastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    spfirstname = models.CharField(db_column='SpFirstName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    spdob = models.DateTimeField(db_column='SpDOB', blank=True, null=True)  # Field name made lowercase.
    spsex = models.CharField(db_column='SpSex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ch1lastname = models.CharField(db_column='ch1LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ch1firstname = models.CharField(db_column='ch1FirstName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ch1dob = models.DateTimeField(db_column='ch1DOB', blank=True, null=True)  # Field name made lowercase.
    ch1sex = models.CharField(db_column='ch1Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ch2lastname = models.CharField(db_column='ch2LastName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ch2firstname = models.CharField(db_column='ch2FirstName', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ch2dob = models.DateTimeField(db_column='ch2DOB', blank=True, null=True)  # Field name made lowercase.
    ch2sex = models.CharField(db_column='ch2Sex', max_length=1, blank=True, null=True)  # Field name made lowercase.
    russian_client = models.IntegerField(db_column='Russian Client', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tblMembers'
