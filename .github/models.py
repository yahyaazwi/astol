from django.db import models

class Driver(models.Model):
    STATUS_CHOICES = [
        ('available', 'متاح'),
        ('on_trip', 'في رحلة'),
        ('idle', 'عاطل'),
        ('out_of_service', 'خارج الخدمة'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    truck_number = models.CharField(max_length=50)
    trailer_number = models.CharField(max_length=50)
    permit_number = models.CharField(max_length=50)
    load = models.DecimalField(max_digits=10, decimal_places=3)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    permit_image = models.ImageField(upload_to='permits/', null=True, blank=True)
    indicator_number = models.CharField(max_length=50)

class Employee(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=20)