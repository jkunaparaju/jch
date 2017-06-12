# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classnumber', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('fiscal_year', models.CharField(blank=True, db_column='fiscal year', max_length=50, null=True)),
                ('period', models.CharField(blank=True, max_length=50, null=True)),
                ('memo', models.TextField(blank=True, null=True)),
                ('prices', models.TextField(blank=True, null=True)),
                ('dates', models.TextField(blank=True, null=True)),
                ('age_grade', models.TextField(blank=True, db_column='age/grade', null=True)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('semester', models.CharField(blank=True, max_length=50, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('instructor', models.CharField(blank=True, max_length=50, null=True)),
                ('maxsize', models.CharField(blank=True, max_length=50, null=True)),
                ('openstatus', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('enterdate', models.DateTimeField(blank=True, db_column='EnterDate', null=True)),
                ('room_location', models.CharField(blank=True, db_column='Room Location', max_length=50, null=True)),
                ('autofill', models.IntegerField(blank=True, null=True)),
                ('order', models.FloatField(blank=True, db_column='Order', null=True)),
                ('user', models.CharField(blank=True, db_column='User', max_length=50, null=True)),
            ],
            options={
                'db_table': 'class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registrationnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='first name', max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, db_column='last Name', max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('emergencyphone', models.CharField(blank=True, max_length=50, null=True)),
                ('street_address', models.CharField(blank=True, db_column='street address', max_length=50, null=True)),
                ('citystatezip', models.CharField(blank=True, max_length=50, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('classnumber', models.IntegerField(blank=True, null=True)),
                ('attendance', models.CharField(blank=True, max_length=50, null=True)),
                ('memberid', models.IntegerField(blank=True, db_column='memberID', null=True)),
                ('receipt_field', models.CharField(blank=True, db_column='receipt #', max_length=50, null=True)),
                ('fee', models.FloatField(blank=True, db_column='Fee', null=True)),
                ('memo', models.TextField(blank=True, db_column='Memo', null=True)),
                ('applicationpath', models.TextField(blank=True, db_column='ApplicationPath', null=True)),
                ('applicationpath2', models.TextField(blank=True, db_column='ApplicationPath2', null=True)),
                ('date', models.DateTimeField(blank=True, db_column='Date', null=True)),
                ('user', models.CharField(blank=True, db_column='User', max_length=50, null=True)),
                ('cid1', models.IntegerField(blank=True, db_column='CID1', null=True)),
                ('ca', models.CharField(blank=True, db_column='Ca', max_length=50, null=True)),
                ('cid2', models.IntegerField(blank=True, db_column='CID2', null=True)),
                ('cb', models.CharField(blank=True, db_column='Cb', max_length=50, null=True)),
                ('cid3', models.IntegerField(blank=True, db_column='CID3', null=True)),
                ('cc', models.CharField(blank=True, db_column='Cc', max_length=50, null=True)),
                ('cid4', models.IntegerField(blank=True, db_column='CID4', null=True)),
                ('cd', models.CharField(blank=True, db_column='Cd', max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=50, null=True)),
                ('zip', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'registration',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tblmembers',
            fields=[
                ('id', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('memberid', models.IntegerField(blank=True, db_column='MemberID', null=True)),
                ('marital_st', models.CharField(blank=True, db_column='Marital_St', max_length=10, null=True)),
                ('member_cat', models.CharField(blank=True, db_column='Member_Cat', max_length=27, null=True)),
                ('year', models.CharField(blank=True, db_column='Year', max_length=50, null=True)),
                ('scholarship', models.CharField(blank=True, db_column='Scholarship', max_length=50, null=True)),
                ('m_notes', models.TextField(blank=True, db_column='M_Notes', null=True)),
                ('splastname', models.CharField(blank=True, db_column='SpLastName', max_length=20, null=True)),
                ('spfirstname', models.CharField(blank=True, db_column='SpFirstName', max_length=15, null=True)),
                ('spdob', models.DateTimeField(blank=True, db_column='SpDOB', null=True)),
                ('spsex', models.CharField(blank=True, db_column='SpSex', max_length=1, null=True)),
                ('ch1lastname', models.CharField(blank=True, db_column='ch1LastName', max_length=20, null=True)),
                ('ch1firstname', models.CharField(blank=True, db_column='ch1FirstName', max_length=15, null=True)),
                ('ch1dob', models.DateTimeField(blank=True, db_column='ch1DOB', null=True)),
                ('ch1sex', models.CharField(blank=True, db_column='ch1Sex', max_length=1, null=True)),
                ('ch2lastname', models.CharField(blank=True, db_column='ch2LastName', max_length=20, null=True)),
                ('ch2firstname', models.CharField(blank=True, db_column='ch2FirstName', max_length=15, null=True)),
                ('ch2dob', models.DateTimeField(blank=True, db_column='ch2DOB', null=True)),
                ('ch2sex', models.CharField(blank=True, db_column='ch2Sex', max_length=1, null=True)),
                ('russian_client', models.IntegerField(blank=True, db_column='Russian Client', null=True)),
            ],
            options={
                'db_table': 'tblMembers',
                'managed': False,
            },
        ),
    ]
