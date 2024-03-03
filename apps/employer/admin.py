from django.contrib.admin import *
from .models import *

@register(Employer)
class EmployerAdmin(ModelAdmin):
    list_display = ("id", "name", "foundation_date")
    list_display_links = ("id", "name", "foundation_date")
    ordering = ("foundation_date",)

