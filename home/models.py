from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    sno = models.AutoField(primary_key=True)
    shopname = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    i1 = models.FloatField()
    i2 = models.FloatField()
    i3 = models.FloatField()
    i4 = models.FloatField()
    i5 = models.FloatField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Party(models.Model):
    sno = models.AutoField(primary_key=True)
    id = models.CharField(max_length=40)
    name = models.CharField(max_length=60)
    area = models.CharField(max_length=12)
    contact = models.CharField(max_length=12)
    address = models.CharField(max_length=100)
    img = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Sheet(models.Model):
    sno = models.AutoField(primary_key=True)
    date = models.DateField()
    area = models.CharField(max_length=12)
    