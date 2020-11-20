from django.contrib import admin
from django.utils.html import format_html

from .models import *

# Register your models here.

admin.site.site_header = 'HotZone'
admin.site.site_title = 'HotZone'


@admin.register(Virus)
class VirusAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth', 'see_cases')

    def see_cases(self, obj):
        return format_html(
            f'''
                <a href="/admin/virus/case/?virus__id={obj.id}">cases</a>
            '''
        )


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('case_number', 'date', 'category', 'virus', 'see_patients')

    def see_patients(self, obj):
        return format_html(
            f'''
                <a href="/admin/patient/patientcase/?case__id={obj.id}">patients</a>
            '''
        )
