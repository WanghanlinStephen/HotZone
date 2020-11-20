from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# Create your views here.

def add_api(request, lid):
    location = get_object_or_404(Location, id=lid)
    location.is_from_api = 0
    location.save()

    Location.objects.filter(is_from_api=1).delete()
    messages.success(request, 'Ok!')
    return redirect('/admin/visit/location/')
