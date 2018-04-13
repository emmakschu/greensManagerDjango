from django.db import models


class SandType(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_char=256)
    notes = models.TextField()
    unit_size = models.DecimalField(decimal_places=2,
                                    max_digits=12,
                                    blank=True,
                                    null=True)
    price = models.DecimalField(decimal_places=2,
                                max_digits=2,
                                blank=True,
                                null=True)
    unit_price = models.DecimalField(decimal_places=2,
                                     max_digits=2,
                                     blank=True,
                                     null=True)

class Topdressing(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    topdress_date = models.DateField()
    sand = models.ForeignKey(SandType)
    
class GreenTopdressing(Topdressing):
    greens = models.ManyToManyField('courses.Green')
    
class TeeTopdressing(Topdressing):
    tees = models.ManyToManyField('courses.Tee')
    
class FairwayTopdressing(Topdressing):
    fairways = models.ManyToManyField('courses.Fairway')
