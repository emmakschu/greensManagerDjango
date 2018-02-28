from django.db import models

# Create your models here.

class Fluid(models.Model):
    name = models.TextField()
    price_per_unit = models.DecimalField(decimal_places = 2,
                                         max_digits = 10)
    last_updated = models.DateTimeField(auto_now = True)

class Fuel(Fluid):
    def __str__(self):
        return "Fuel type: %s" % self.name

class Oil(Fluid):
    def __str__(self):
        return "Oil type: %s" % self.name

class Part(models.Model):
    part_no = models.CharField(max_length=256)
    alt_part_no = models.CharField(max_length=256,
                                   blank = True,
                                   null = True)
    make = models.CharField(max_length=256)
    description = models.TextField(blank = True, null = True)
    location = models.TextField(blank = True, null = True)
    in_stock = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places = 2,
                                max_digits = 10)
    date_added = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)
    obsolete = models.BooleanField(default = False)

    def __str__(self):
        return "%s %s" % (self.make, self.description)

class Filter(Part):
    def __str__(self):
        return "Filter %s" % self.part_no

