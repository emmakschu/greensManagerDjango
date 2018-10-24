from django.db import models

class Unit(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=12)

    def __str__(self):
        return "%s" % self.abbreviation

class WeightUnit(Unit):
    conversion = models.FloatField()

class VolumeUnit(Unit):
    conversion = models.FloatField()

class DistanceUnit(Unit):
    conversion = models.FloatField()

class AreaUnit(Unit):
    conversion = models.FloatField()

class TimeUnit(Unit):
    conversion = models.FloatField()

class RateUnit(models.Model):
    numerator = models.ForeignKey(Unit, related_name="num")
    denominator = models.ForeignKey(Unit, related_name="den")

    def __str__(self):
        return "%s / %s" % (self.numerator,
                            self.denominator)
