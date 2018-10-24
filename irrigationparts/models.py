from django.db import models

class ThreadType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s threading" % self.name

class Sprinkler(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=256)
    thread_type = models.ForeignKey(ThreadType)
    in_stock = models.IntegerField()
    price = models.DecimalField(decimal_places=2,
                                max_digits=12)
    coverage_radius = models.DecimalField(decimal_places=2,
                                          max_digits=8,
                                          blank=True,
                                          null=True)
    radius_units = models.ForeignKey('measures.DistanceUnit')

class PvcPipe(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit')
    length = models.DecimalField(decimal_places=2,
                                 max_digits=16)
    length_units = models.ForeignKey('measures.DistanceUnit')
    in_stock = models.IntegerField()

class SwingJoint(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit')
    thread_type = models.ForeignKey(ThreadType)
    in_stock = models.IntegerField()

class EndCap(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit')
    thread_type = models.ForeignKey(ThreadType)
    in_stock = models.IntegerField()

class CompressionFitting(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit')
    in_stock = models.IntegerField()
