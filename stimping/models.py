from django.db import models


class Stimp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    simple_version = models.BooleanField()
    green = models.ForeignKey('courses.Green')
    
    forward1 = models.DecimalField(decimal_places=2,
                                   max_digits=12)
    forward2 = models.DecimalField(decimal_places=2,
                                   max_digits=12,
                                   blank=True,
                                   null=True)
    forward3 = models.DecimalField(decimal_places=2,
                                   max_digits=12,
                                   blank=True,
                                   null=True)
    forwardAvg = models.DecimalField(decimal_places=2,
                                     max_digits=12)
    
    backward1 = models.DecimalField(decimal_places=2,
                                    max_digits=12)
    backward2 = models.DecimalField(decimal_places=2,
                                    max_digits=12,
                                    blank=True,
                                    null=True)
    backward3 = models.DecimalField(decimal_places=2,
                                    max_digits=12,
                                    blank=True,
                                    null=True)
    backwardAvg = models.DecimalField(decimal_places=2,
                                      max_digits=12)
    
    left1 = models.DecimalField(decimal_places=2,
                                max_digits=12)
    left2 = models.DecimalField(decimal_places=2,
                                max_digits=12,
                                blank=True,
                                null=True)
    left3 = models.DecimalField(decimal_places=2,
                                max_digits=12,
                                blank=True,
                                null=True)
    leftAvg = models.DecimalField(decimal_places=2,
                                  max_digits=12)
    
    right1 = models.DecimalField(decimal_places=2,
                                 max_digits=12)
    right2 = models.DecimalField(decimal_places=2,
                                 max_digits=12,
                                 blank=True,
                                 null=True)
    right3 = models.DecimalField(decimal_places=2,
                                 max_digits=12,
                                 blank=True,
                                 null=True)
    rightAvg = models.DecimalField(decimal_places=2,
                                   max_digits=12)
    
    stdDev = models.DecimalField(decimal_places=5,
                                 max_digits=15)
    mu_k = models.DecimalField(decimal_places=5,
                               max_digits=15)
    raw_speed = models.DecimalField(decimal_places=2,
                                    max_digits=12)
    adj_speed = models.DecimalField(decimal_places=2,
                                    max_digits=12)
    
