import json

from django.contrib import admin, messages

# Register your models here.
from django.db.models import QuerySet
from django.shortcuts import redirect
from django.utils.html import format_html

from .models import *
import requests


@admin.register(PatientVisit)
class VisitAdmin(admin.ModelAdmin):
    """
    visit
    """
    search_fields = ('patient__name',)
    list_filter = ('date_of_visit', 'date_of_confirmed')
    list_display = ('patient', 'date_of_visit', 'date_of_confirmed', 'location')

    def location(self, obj):
        """
        see location
        :param obj:
        :return:
        """
        return format_html(
            f'''
                <a href='/admin/visit/visitlocation/?visit__id={obj.id}'>see location</a>
            '''
        )


def add_api(modeladmin, request, queryset): 
    queryset = queryset.filter(is_from_api=1)
    if queryset.count() == 0:
        messages.error(request, 'No API DATA')
    else:
        queryset.update(is_from_api=0)
        Location.objects.filter(is_from_api=1).delete()
        messages.success(request, 'add OK!')


add_api.short_description = 'Add API TO DB' #Display it at the end of the selection list


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    # actions = [add_api, ]
    search_fields = ('name',)
    list_display = ('name', 'address', 'x', 'y', 'choose')
    readonly_fields = ('is_from_api',)

    def choose(self, obj):
        if obj.is_from_api == 1:
            return format_html(
                f'''
                    <a href="/add_api/{obj.id}">add to db</a>
                '''
            )
        else:
            return format_html(
                '''
                no action
                '''
            )

    def get_search_results(self, request, queryset, search_term):
        """
        search
        :param request:
        :param queryset:
        :param search_term:
        :return:
        """
        queryset, use_distinct = super(LocationAdmin, self).get_search_results(
            request, queryset, search_term
        )
        # check if the 'search_term' is within database
        # if not,search it from external API
        if queryset.count() == 0:
            Location.objects.filter(is_from_api=1).delete()
            url = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=' + search_term
            response = requests.get(url=url, headers={'Content-Type': 'application/json'})
            if response.status_code == 200:
                dataset = json.loads(response.text)
                # Example
                # {'addressZH': '駱克道   137-141號|柯布連道   4A-4C號', 'nameZH': '香江大廈', 'x': 835860, 'y': 815493,
                #  'nameEN': 'Hong Kong Building', 'addressEN': "137-141 LOCKHART ROAD|4A-4C O'BRIEN ROAD"}
                location_data = []
                for data in dataset:
                    item = {}
                    location = Location(address=data['addressEN'], name=data['nameEN'], x=data['x'], y=data['y'],
                                        is_from_api=1)
                    location_data.append(location)

                Location.objects.bulk_create(location_data)
                queryset = Location.objects.filter(is_from_api=1)
                return queryset, use_distinct
            else:
                messages.error(request, 'API No data')
        # Else directly return the searched item from the database
        return queryset, use_distinct

    def get_queryset(self, request):
        qs = super(LocationAdmin, self).get_queryset(request)
        Location.objects.filter(is_from_api=1).delete()
        return qs


@admin.register(VisitLocation)
class VisitLocationAdmin(admin.ModelAdmin):
    search_fields = ('location__name',)
    # list_filter = ('visit__id',) # 链接 http://127.0.0.1:8000/admin/visit/visitlocation/?visit__id=1
    list_display = ('visit', 'location', 'date_from', 'date_to', 'category')  # 'address', 'XCoordinate', 'YCoordinate',
