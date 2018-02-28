from django.db import models

# Create your models here.

class SoilType(models.Model):
    name = models.CharField(max_length=256)
    sand_ratio = models.FloatField()
    silt_ratio = models.FloatField()
    clay_ratio = models.FloatField()

    def __str__(self):
        return "%s" % (self.name)

class TurfgrassGenus(models.Model):

    class Meta:
        verbose_name_plural = 'Turfgrass genuses'

    name = models.CharField(max_length=256)
    common_name = models.CharField(max_length=256)

    def __str__(self):
        return "%s (%s)" % (self.common_name, self.name)

class TurfgrassSpecies(models.Model):

    class Meta:
        verbose_name_plural = 'Turfgrass species'

    name = models.CharField(max_length=256)
    common_name = models.CharField(max_length=256)
    genus = models.ForeignKey(TurfgrassGenus)

    def __str__(self):
        return "%s (%s %s)" % (self.common_name,
                               self.genus.name,
                               self.name)

class Cultivar(models.Model):
    name = models.CharField(max_length=256)
    species = models.ForeignKey(TurfgrassSpecies)

    def __str__(self):
        return "%s (%s)" % (self.name, self.species)
