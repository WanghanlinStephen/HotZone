from django.contrib import admin
from django.utils.html import format_html

from .models import *


# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
    Patient's basic information
    """
    # search_fields:Add the search function for a certain field
    # list_display:List certain property out in the database
    search_fields = ('name',)
    list_display = ('name', 'number', 'date_of_birth', 'visit')

    def visit(self, obj):
        """
        Add clicking functions 'see visit' at the end of the line, enable CHP users to see visit records of a specific patient
        http://127.0.0.1:8000/admin/visit/patientvisit/?patient__id=1
        :param obj:
        :return:
        """
        return format_html(
            f'''
                  <a href='/admin/visit/patientvisit/?patient__id={obj.id}'>see visit</a>
            '''
        )



@admin.register(PatientCase)
class PatientCaseAdmin(admin.ModelAdmin):
    """
    Patient case
    """
    list_filter = ('patient__name', 'case__case_number', )
    list_display = ('patient', 'case', 'create_time', 'condition')
