from django.db import models

from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    pay_rate = models.DecimalField(decimal_places=2,
                                   max_digits=12)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)

class Task(models.Model):
    assigned_by = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="task_assigned")
    supervisor = models.ForeignKey(Employee,
                                   on_delete=models.CASCADE,
                                   related_name="task_super")
    additional_workers = models.ManyToManyField(Employee,
                                                related_name="task_workers",
                                                blank=True,
                                                null=True)
    description = models.TextField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    started = models.DateTimeField(blank=True, null=True)
    completed = models.DateTimeField(blank=True, null=True)
    duration = models.DateTimeField(blank=True, null=True)
    
    labor_cost = models.DecimalField(decimal_places=2,
                                     max_digits=15,
                                     default=0)

    def __str__(self):
        return "%s %s" % (self.started, self.description)

class MowTask(Task):
    mowing = models.ForeignKey('mowing.Mowing',
                               on_delete=models.CASCADE)

    def __str__(self):
        return "Mowing by: %s; start: %s, end: %s" % (self.supervisor.user.first_name,
                                                      self.started,
                                                      self.completed)


class TrapTask(Task):

    def __str__(self):
        return "Traps: %s" % self

class RecordsTask(Task):

    def __str__(self):
        return "Record Keeping: %s" % self

class ShopTask(Task):

    def __str__(self):
        return "Shop Work: %s" % self

class MiscTask(Task):

    def __str__(self):
        return "Misc: %s" % self

class WtfTask(Task):

    def __str__(self):
        return "%s" % self
