from django.contrib.admin import *
from .models import Vacancy

@register(Vacancy)
class VacancyAdmin(ModelAdmin):
    list_display = ('id', 'company', 'created_date')
    list_display_links = ('id', 'created_date')
    ordering = ('-created_date',)
