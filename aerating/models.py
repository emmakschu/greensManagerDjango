from django.db import models

class Aerating(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    aerate_date = models.DateField()
    aerator = models.ForeignKey('machines.Aerator', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    
class GreensAerating(Aerating):
    green = models.ManyToManyField('courses.Green')
    
class TeeAerating(Aerating):
    tee = models.ManyToManyField('courses.Tee')
    
class FairwayAerating(Aerating):
    fairway = models.ManyToManyField('courses.Fairway')
    
class RoughAerating(Aerating):
    rough = models.ManyToManyField('courses.Rough')

class QuadraTining(Aerating):
    green = models.ManyToManyField('courses.Green')

    def __str__(self):
        return "Quadra-tining on %s" % self.aerate_date

class DeepTine(Aerating):
    green = models.ManyToManyField('courses.Green')
