from django.db import models

class ThreadType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return "%s threading" % self.name

class Sprinkler(models.Model):
    make = models.CharField(max_length=128)
    model = models.CharField(max_length=256)
    thread_type = models.ForeignKey(ThreadType,
                                    on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2,
                                max_digits=12)
    coverage_radius = models.DecimalField(decimal_places=2,
                                          max_digits=8,
                                          blank=True,
                                          null=True)
    radius_units = models.ForeignKey('measures.DistanceUnit',
                                     blank=True,
                                     null=True,
                                     on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s sprinkler" % (self.make, self.model)

class SprinklerGuts(Sprinkler):

    class Meta:
        verbose_name_plural = "Sprinkler guts"

    def __str__(self):
        return "%s %s guts" % (self.make, self.model)

class GateValve(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    handle_type = models.CharField(max_length=256)
    threading = models.ForeignKey(ThreadType,
                                  on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%f %s gate valve" % (self.diameter,
                                     self.diameter_units.abbreviation)

class Drain(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    handle_type = models.CharField(max_length=256)
    threading = models.ForeignKey(ThreadType,
                                  on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%f %s drain (%s thread)" % (self.diameter,
                                            self.diameter_units.abbreviation,
                                            self.threading.name)

class QuickCoupler(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    coupler_size = models.CharField(max_length=256)
    threading = models.ForeignKey(ThreadType,
                                  on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%f %s quick coupler (%s thread)" % (self.diameter,
                                                    self.diameter_units.abbreviation,
                                                    self.threading.name)

class CompressionFitting(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%f %s compression fitting" % (self.diameter,
                                              self.diameter_units.abbreviation)

class Reducer(models.Model):
    large_end = models.DecimalField(decimal_places=2,
                                    max_digits=8)
    small_end = models.DecimalField(decimal_places=2,
                                    max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    threading = models.ForeignKey(ThreadType,
                                  on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%f to %f %s reducer" % (self.large_end,
                                        self.small_end,
                                        self.diameter_units.abbreviation)

class PvcPipe(models.Model):

    class Meta:
        verbose_name = "PVC pipe"
        verbose_name_plural = "PVC pipes"

    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    length = models.DecimalField(decimal_places=2,
                                 max_digits=16)
    length_units = models.ForeignKey('measures.DistanceUnit',
                                     on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%f %s PVC pipe (%f %s)" % (self.diameter,
                                           self.diameter_units.abbreviation,
                                           self.length,
                                           self.length_units.abbreviation)

class SwingJoint(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    thread_type = models.ForeignKey(ThreadType,
                                    on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%f %s swing joing (%s thread)" % (self.diameter,
                                                  self.diameter_units.abbreviation,
                                                  self.thread_type.name)

class EndCap(models.Model):
    diameter = models.DecimalField(decimal_places=2,
                                   max_digits=8)
    diameter_units = models.ForeignKey('measures.DistanceUnit',
                                       on_delete=models.CASCADE)
    thread_type = models.ForeignKey(ThreadType,
                                    on_delete=models.CASCADE)
    in_stock = models.PositiveIntegerField()

    def __str__(self):
        return "%f %s end cap (%s thread)" % (self.diameter,
                                              self.diameter_units.abbreviation,
                                              self.thread_type.name)
