from django.contrib import admin
from projects import models


# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Agent)
admin.site.register(models.Role)
admin.site.register(models.InputCategory)
admin.site.register(models.Input)
admin.site.register(models.UnitOfMeasure)
admin.site.register(models.Activity)
admin.site.register(models.Milestone)
admin.site.register(models.Action)

