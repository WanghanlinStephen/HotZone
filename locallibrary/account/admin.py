from django.contrib import admin
from .models import *
from .views import *
# Register your models here.
@admin.register(Account)
class PersonalInfoAdmin(admin.ModelAdmin):
    # changelist_view用来自定义表格返回内容
    def changelist_view(self, request, extra_content=None):
        return index(request)