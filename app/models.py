from django.db import models

# Create your models here.


class Meetdb(models.Model):
    meet_id = models.AutoField(primary_key=True)
    open_id = models.CharField(max_length=50,null=False)
    date = models.CharField(max_length=20, null=False)
    date2 = models.CharField(max_length=20, null=False)
    depart = models.CharField(max_length=20, null=False)
    flag = models.CharField(max_length=10, null=False)
    area = models.CharField(max_length=30,null=False)
    meet = models.CharField(max_length=20, null=False)
    year = models.IntegerField()
    day = models.IntegerField()
    month = models.IntegerField()
    time = models.CharField(max_length=50, null=False)
    user = models.CharField(max_length=20, null=False)
    style = models.CharField(max_length=20,null=False)
    sysdate = models.DateTimeField(auto_now=True)



class DayStyle(models.Model):
    style_id = models.AutoField(primary_key=True)
    meet_id  = models.IntegerField()
    background = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=20, null=False)
    day = models.IntegerField()
    meet = models.CharField(max_length=20, null=False)
    style = models.CharField(max_length=20, null=False)
    month = models.IntegerField(null=False)

class Departs(models.Model):
    depart_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=10,null=False)
    depart = models.CharField(max_length=50,null=False)
    var1 = models.CharField(max_length=20, null=False)

class Domain(models.Model):
    order = models.AutoField(primary_key=True)
    area = models.CharField(max_length=30,null=False)



class User(models.Model):
    user_id =models.AutoField(primary_key=True)
    open_id = models.TextField()
    depart = models.CharField(max_length=30,null=False)
    password = models.CharField(max_length=20)
    user_code = models.CharField(max_length=20,null=False)
    user_name = models.CharField(max_length=50,null=False)

class Times(models.Model):
    time_id = models.AutoField(primary_key=True)
    open_id = models.TextField()
    flag = models.CharField(max_length=10,null=False)
    stime = models.CharField(max_length=20,null=False)



class Meet(models.Model):
    id = models.AutoField(primary_key=True)
    open_id = models.TextField()
    area = models.CharField(max_length=30,null=False)
    counters = models.CharField(max_length=10)
    meet = models.CharField(max_length=30,null=False)

