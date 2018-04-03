from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class RepairPart(models.Model):
    part = models.ForeignKey('parts.Part')
    repair = models.ForeignKey(Maintenance)
    qty = models.IntegerField()

class Maintenance(models.Model):
    date_ooc = models.DateTimeField(auto_now_add=True)
    date_fixed = models.DateTimeField(blank=True, null=True)
    machine = models.ForeignKey('machines.Machine')
    hours_on_machine = models.FloatField()
    description = models.TextField()
    parts_used = models.ManyToManyField(RepairPart,
                                        blank=True)
    parts_cost = models.DecimalField(decimal_places=2,
                                     max_digits=12,
                                     blank=True,
                                     null=True)
    shipping_cost = models.DecimalField(decimal_places=2,
                                        max_digits=12,
                                        blank=True,
                                        default=0)
    total_cost = models.DecimalField(decimal_places=2,
                                     max_digits=12)
    acked = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
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
