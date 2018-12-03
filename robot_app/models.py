# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    bname = models.CharField(max_length=255, blank=True, null=True)
    athor = models.CharField(max_length=255, blank=True, null=True)
    cla = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    num = models.CharField(max_length=255, blank=True, null=True)
    newword = models.CharField(max_length=255, blank=True, null=True)
    updatetime = models.CharField(max_length=255, blank=True, null=True)
    pic = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class Creditlost(models.Model):
    serialnum = models.CharField(primary_key=True, max_length=255)
    iname = models.CharField(max_length=255, blank=True, null=True)
    businessentity = models.CharField(db_column='businessEntity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardnum = models.CharField(db_column='cardNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(max_length=255, blank=True, null=True)
    sexy = models.CharField(max_length=255, blank=True, null=True)
    types = models.CharField(max_length=255, blank=True, null=True)
    casecode = models.CharField(db_column='caseCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disrupttypename = models.CharField(db_column='disruptTypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='regDate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    performance = models.CharField(max_length=255, blank=True, null=True)
    areaname = models.CharField(db_column='areaName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    duty = models.CharField(max_length=255, blank=True, null=True)
    gistunit = models.CharField(db_column='gistUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='publishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'creditlost'


class Creditlost1(models.Model):
    serialnum = models.CharField(primary_key=True, max_length=255)
    iname = models.CharField(max_length=255, blank=True, null=True ,db_index=True)
    businessentity = models.CharField(db_column='businessEntity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cardnum = models.CharField(db_column='cardNum', max_length=255, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(max_length=255, blank=True, null=True ,db_index=True)
    sexy = models.CharField(max_length=255, blank=True, null=True)
    types = models.CharField(max_length=255, blank=True, null=True)
    casecode = models.CharField(db_column='caseCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    disrupttypename = models.CharField(db_column='disruptTypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='regDate', max_length=255, blank=True, null=True, db_index=True)  # Field name made lowercase.
    performance = models.CharField(max_length=255, blank=True, null=True)
    areaname = models.CharField(db_column='areaName', max_length=255, blank=True, null=True ,db_index=True)  # Field name made lowercase.
    duty = models.CharField(max_length=255, blank=True, null=True)
    gistunit = models.CharField(db_column='gistUnit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='publishDate', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'creditlost1'


class Creditpeople(models.Model):
    serialnum = models.CharField(primary_key=True, max_length=255)
    iname = models.CharField(max_length=50, blank=True, null=True)
    cardnum = models.CharField(db_column='cardNum', max_length=50, blank=True, null=True)  # Field name made lowercase.
    age = models.CharField(max_length=50, blank=True, null=True)
    sexy = models.CharField(max_length=50, blank=True, null=True)
    types = models.CharField(max_length=50, blank=True, null=True)
    casecode = models.CharField(db_column='caseCode', max_length=50, blank=True, null=True)  # Field name made lowercase.
    disrupttypename = models.CharField(db_column='disruptTypeName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    regdate = models.CharField(db_column='regDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    performance = models.CharField(max_length=255, blank=True, null=True)
    areaname = models.CharField(db_column='areaName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    duty = models.CharField(max_length=5000, blank=True, null=True)
    gistunit = models.CharField(db_column='gistUnit', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    publishdate = models.CharField(db_column='publishDate', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'creditpeople'


class Jokes(models.Model):
    tname = models.CharField(max_length=255, blank=True, null=True)
    matter = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jokes'


class Zhilian(models.Model):
    zw = models.CharField(max_length=1000, blank=True, null=True)
    salary = models.CharField(max_length=1000, blank=True, null=True)
    company = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    worktime = models.CharField(max_length=1000, blank=True, null=True)
    edu = models.CharField(max_length=1000, blank=True, null=True)
    num = models.CharField(max_length=1000, blank=True, null=True)
    pso = models.CharField(max_length=3000, blank=True, null=True)
    industry = models.CharField(max_length=1000, blank=True, null=True)
    promulgator = models.CharField(max_length=1000, blank=True, null=True)
    numpeople = models.CharField(max_length=1000, blank=True, null=True)
    netadress = models.CharField(max_length=1000, blank=True, null=True)
    adress = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zhilian'


class Zhilian1(models.Model):
    zw = models.CharField(max_length=1000, blank=True, null=True)
    salary = models.CharField(max_length=1000, blank=True, null=True)
    company = models.CharField(max_length=1000, blank=True, null=True)
    city = models.CharField(max_length=1000, blank=True, null=True)
    worktime = models.CharField(max_length=1000, blank=True, null=True)
    edu = models.CharField(max_length=1000, blank=True, null=True)
    num = models.CharField(max_length=1000, blank=True, null=True)
    pso = models.CharField(max_length=3000, blank=True, null=True)
    industry = models.CharField(max_length=1000, blank=True, null=True)
    promulgator = models.CharField(max_length=1000, blank=True, null=True)
    numpeople = models.CharField(max_length=1000, blank=True, null=True)
    netadress = models.CharField(max_length=1000, blank=True, null=True)
    adress = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zhilian1'



class Users(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    hashi = models.CharField(max_length=30)
    regtime=models.CharField(max_length=30)
    other = models.CharField(max_length=50)

    class Meta:
        db_table = "t_user"


