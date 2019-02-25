from django.db import models

class Build(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    build_date = models.DateField()
    details = models.TextField()

class BuildGreen(Build):
    green = models.ForeignKey('courses.Green',
                              on_delete=models.CASCADE)
    soil_type = models.ForeignKey('turfs.SoilType',
                                  blank=True,
                                  null=True,
                                  on_delete=models.CASCADE)
    cultivar = models.ForeignKey('turfs.Cultivar',
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)
    species = models.ForeignKey('turfs.TurfgrassSpecies',
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)
    
    def __str__(self):
        return "Greens build %s on %s" % (self.green,
                                          self.build_date)
    
class BuildTee(Build):
    tee = models.ForeignKey('courses.Tee')
    soil_type = models.ForeignKey('turfs.SoilType',
                                  blank=True,
                                  null=True,
                                  on_delete=models.CASCADE)
    cultivar = models.ForeignKey('turfs.Cultivar',
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)
    species = models.ForeignKey('turfs.TurfgrassSpecies',
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)
    
class BuildFairway(Build):
    fairway = models.ForeignKey('courses.Fairway',
                                on_delete=models.CASCADE)
    soil_type = models.ForeignKey('turfs.SoilType',
                                  blank=True,
                                  null=True,
                                  on_delete=models.CASCADE)
    cultivar = models.ForeignKey('turfs.Cultivar',
                                 blank=True,
                                 null=True,
                                 on_delete=models.CASCADE)
    species = models.ForeignKey('turfs.TurfgrassSpecies',
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)

class BuildBunker(Build):
    bunker = models.ForeignKey('courses.Bunker',
                               on_delete=models.CASCADE)
    
