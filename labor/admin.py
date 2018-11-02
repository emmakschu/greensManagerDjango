from django.contrib import admin

from .models import (
    Employee,
    Task,
    MowTask,
    TrapTask,
    RecordsTask,
    ShopTask,
    MiscTask,
    WtfTask
)

admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(MowTask)
admin.site.register(TrapTask)
admin.site.register(RecordsTask)
admin.site.register(ShopTask)
admin.site.register(MiscTask)
admin.site.register(WtfTask)
