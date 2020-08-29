from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime

class appointment(models.Model):

    doctor_name= models.CharField(max_length=50, unique=True)
    doctor_type= models.CharField(max_length=50, unique=False)
    hospital_name= models.CharField(max_length=50, unique=False)
    date = models.DateField(auto_now=False, editable=True,default=datetime.date.today)
    time = models.TimeField(auto_now=False, auto_now_add=False, editable=True, unique=False)
    tests= models.CharField(max_length=50, unique=False)

    is_active = models.BooleanField(default=True, blank=False)

    owner = models.ForeignKey(
        User, related_name="appointments",
        on_delete = models.CASCADE,null=True
    )


# class medicineslist(models.Model):
#     name= models.CharField(max_length=50, unique=False)