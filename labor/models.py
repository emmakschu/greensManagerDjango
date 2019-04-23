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

class TaskClass(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Task(models.Model):
    task_class = models.ForeignKey(TaskClass,
                                  on_delete=models.CASCADE)
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
