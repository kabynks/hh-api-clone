from django.contrib.admin import *
from .models import *

@register(Employee)
class EmployeeAdmin(ModelAdmin):
    list_display = ("id", "fullname", "email")
    list_display_links = ("id", "fullname", "email")
    ordering = ("id",)

@register(EmployeeSkill)
class EmployeeSkillAdmin(ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ('id', "name")
    ordering = ("id",)
