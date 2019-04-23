from django.db import models

class POGOreading(models.Model):
    hole = models.ForeignKey('courses.Hole',
                             on_delete=models.CASCADE)
    sample_date = models.DateTimeField()
    dataset = models.IntegerField()
    moisture = models.FloatField()
    ec = models.FloatField()
    canopy_temp = models.FloatField()
    soil_temp = models.FloatField(blank=True,
                                  null=True)
    soil_temp_depth = models.FloatField(blank=True,
                                        null=True)
    salinity_index = models.FloatField()
    notes = models.TextField(blank=True,
                             null=True)

class POGO_green_reading(POGOreading):
    green = models.ForeignKey('courses.Green',
                              on_delete=models.CASCADE)

class POGO_tee_reading(POGOreading):
    tee = models.ForeignKey('courses.Tee',
                            on_delete=models.CASCADE)

class POGO_fw_reading(POGOreading):
    fairway = models.ForeignKey('courses.Fairway',
                                on_delete=models.CASCADE)
