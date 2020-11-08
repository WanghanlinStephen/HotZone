from django.contrib import admin
from .models import Case,Patient,Virus,Location,Visit

# Register your models here.

admin.site.register(Patient)
admin.site.register(Case)
admin.site.register(Virus)
admin.site.register(Location)
admin.site.register(Visit)