from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone

# Create your models here.

class Pest(models.Model):
    name = models.CharField(max_length=256)
    notes = models.TextField()
    susceptible = models.ManyToManyField('turfs.TurfgrassSpecies')

class ChemManufacturer(models.Model):
    name = models.CharField(max_length = 128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Chemical(models.Model):
    scientific_name = models.CharField(max_length = 256)
    common_name = models.CharField(max_length = 256,
                                   blank = True,
                                   null = True)
    targets = models.ManyToManyField(Pest)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TradeChem(models.Model):
    manufacturer = models.ForeignKey(ChemManufacturer)
    chemical = models.ForeignKey(Chemical)
    trade_name = models.CharField(max_length = 128)
    unit_size = models.FloatField()
    units = models.ForeignKey('measures.Unit',
                              related_name='+')
    unit_price = models.DecimalField(decimal_places = 2,
                                     max_digits = 15)
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Spraying(models.Model):
    spray_date = models.DateTimeField(default = timezone.now)
    sprayer = models.ForeignKey('machines.Sprayer')
    operator = models.ForeignKey(User)
    tanks_sprayed = models.FloatField()
    water_per_tank = models.FloatField()
    water_units = models.ForeignKey('measures.VolumeUnit',
                                    related_name='+')
    area_covered = models.FloatField(blank=True, null=True)
    area_units = models.ForeignKey('measures.AreaUnit',
                                   related_name='+')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ChemUsedInSpray(models.Model):
    chemical = models.ForeignKey(TradeChem)
    spray = models.ForeignKey(Spraying)
    amount_used_per_tank = models.FloatField()
    units = models.ForeignKey('measures.Unit',
                              related_name='+')
    rate = models.FloatField()
    rate_units = models.ForeignKey('measures.RateUnit',
                                   related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class GreensSpraying(Spraying):
    greens = models.ManyToManyField('courses.Green')
    surrounds = models.BooleanField()

class TeeSpraying(Spraying):
    tees = models.ManyToManyField('courses.Tee')

class FairwaySpraying(Spraying):
    fairways = models.ManyToManyField('courses.Fairway')

class RoughSpraying(Spraying):
    roughs = models.ManyToManyField('courses.Rough')
