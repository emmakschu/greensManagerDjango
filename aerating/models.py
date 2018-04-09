from django.db import models

class Aerating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    aerate_date = models.DateField()
    aerator = models.ForeignKey('machines.Aerator')
    
class GreensAerating(Aerating):
    green = models.ManyToManyField('courses.Green')
    
class TeeAerating(Aerating):
    tee = models.ManyToManyField('courses.Tee')
    
class FairwayAerating(Aerating):
    fairway = models.ManyToManyField('courses.Fairway')
    
class RoughAerating(Aerating):
    rough = models.ManyToManyField('courses.Rough')
