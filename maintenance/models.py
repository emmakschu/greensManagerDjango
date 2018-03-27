from django.db import models
from django.contrib.auth.models import User

class RepairPart(models.Model):
    repair = models.ForeignKey('Maintenance')
    part = models.ForeignKey('parts.Part')
    qty = models.IntegerField(default=1)

class Maintenance(models.Model):
    date_ooc = models.DateTimeField(auto_now_add=True)
    date_fixed = models.DateTimeField(blank=True, null=True)
    machine = models.ForeignKey('machines.Machine')
    hours_on_machine = models.FloatField()
    description = models.TextField()
    parts_used = models.ManyToManyField('parts.Part',
                                        through=RepairPart,
                                        blank = True)
    parts_cost = models.DecimalField(decimal_places=2,
                                     max_digits=12,
                                     blank=True,
                                     null=True)
    acked = models.ForeignKey(User)
    updated_at = models.DateTimeField(auto_now=True)

class OilChange(Maintenance):
    oil = models.ForeignKey('parts.Oil')
    oil_qty = models.DecimalField(decimal_places=2,
                                  max_digits=12)
    oil_cost = models.DecimalField(decimal_places=2,
                                   max_digits=12,
                                   blank=True,
                                   null=True)
    
class Repair(Maintenance):
    def __str__(self):
        return "Repair on %s" % self.machine
