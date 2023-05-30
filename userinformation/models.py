from django.db import models

# Create your models here.

class admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    dob = models.DateField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    desc = models.CharField(max_length=500)

    