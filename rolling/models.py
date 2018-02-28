from django.db import models
from django.utils import timezone

# Create your models here.

class Rolling(models.Model):
    roll_date = models.DateTimeField(default = timezone.now)
    roller = models.ManyToManyField('machines.Roller')

class GreensRolling(Rolling):
    green = models.ManyToManyField('courses.Green')

class TeeRolling(Rolling):
    tee = models.ManyToManyField('courses.Tee')

class FairwayRolling(Rolling):
    fairway = models.ManyToManyField('courses.Fairway')
