from django.db import models


class Stimp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    simple_version = models.BooleanField()
    green = models.ForeignKey('courses.Green',
                              on_delete=models.CASCADE)
    
    forward1 = models.FloatField()
    forward2 = models.FloatField(blank=True, null=True)
    forward3 = models.FloatField(blank=True, null=True)
    forwardAvg = models.FloatField(blank=True, null=True)
    
    backward1 = models.FloatField()
    backward2 = models.FloatField(blank=True, null=True)
    backward3 = models.FloatField(blank=True, null=True)
    backwardAvg = models.FloatField(blank=True, null=True)
    
    left1 = models.FloatField()
    left2 = models.FloatField(blank=True, null=True)
    left3 = models.FloatField(blank=True, null=True)
    leftAvg = models.FloatField(blank=True, null=True)
    
    right1 = models.FloatField()
    right2 = models.FloatField(blank=True, null=True)
    right3 = models.FloatField(blank=True, null=True)
    rightAvg = models.FloatField(blank=True, null=True)
    
    stdDev = models.FloatField()
    mu_k = models.FloatField()
    raw_speed = models.FloatField()
    adj_speed = models.FloatField()
    
