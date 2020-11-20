from django.contrib import admin
from .models import *
from .views import *


# Register your models here.

@admin.register(Cluster)
class ClusterAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_content=None):
        return index(request)
