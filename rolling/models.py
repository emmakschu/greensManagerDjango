from django.db import models
from django.utils import timezone

class Rolling(models.Model):
    roll_date = models.DateTimeField(default = timezone.now)
    roller = models.ManyToManyField('machines.Roller')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GreensRolling(Rolling):
    green = models.ManyToManyField('courses.Green')

class TeeRolling(Rolling):
    tee = models.ManyToManyField('courses.Tee')

class FairwayRolling(Rolling):
    fairway = models.ManyToManyField('courses.Fairway')
