from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
import datetime


times = (('1', '1'),
        ('2', '2'),
        ('3', '3'))
class medicine(models.Model):

    name= models.CharField(max_length=50, unique=True)
    start_date = models.DateField(auto_now=False, editable=True,default=datetime.date.today)
    duration = models.PositiveIntegerField(default=1, validators=[MaxValueValidator(180),MinValueValidator(1)])
    times = models.CharField(
        max_length=1,
        choices=times,
        default=1,
    )
    medicine_times_m = models.BooleanField(default=True, blank=True)
    medicine_times_a = models.BooleanField(default=False, blank=True)
    medicine_times_n = models.BooleanField(default=False, blank=True)

    is_active = models.BooleanField(default=True, blank=False)

    owner = models.ForeignKey(
        User, related_name="medicines",
        on_delete = models.CASCADE,null=True
    )


class medicineslist(models.Model):
    name= models.CharField(max_length=50, unique=False)