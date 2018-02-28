from django.db import models

from django.utils import timezone

# Create your models here.

class ChemManufacturer(models.Model):
    name = models.CharField(max_length = 128)

class Chemical(models.Model):
    scientific_name = models.CharField(max_length = 256)
    common_name = models.CharField(max_length = 256,
                                   blank = True,
                                   null = True)

class TradeChem(models.Model):
    manufacturer = models.ForeignKey(ChemManufacturer)
    chemical = models.ForeignKey(Chemical)
    trade_name = models.CharField(max_length = 128)
    unit_size = models.FloatField()
    unit_price = models.DecimalField(decimal_places = 2,
                                     max_digits = 15)
    notes = models.TextField()

class Spraying(models.Model):
    spray_date = models.DateTimeField(default = timezone.now)
    sprayer = models.ForeignKey('machines.Sprayer')

class ChemUsedInSpray(models.Model):
    chemical = models.ForeignKey(TradeChem)
    spray = models.ForeignKey(Spraying)
    tank_size = models.
    amount_used = models.FloatField()
    rate = models.FloatField()
