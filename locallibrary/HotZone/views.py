from django.shortcuts import render
from django.shortcuts import render
from .models import Virus,Patient,Case,Location
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import os
import json
import requests
from requests.auth import HTTPBasicAuth

# Create your views here.
@login_required
def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_virus=Virus.objects.all().count()
    num_patient=Patient.objects.all().count()
    # Available books (status = 'a')
    num_location=Location.objects.all().count()
    num_case=Case.objects.all().count()  # The 'all()' is implied by default.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_virus':num_virus,'num_patient':num_patient,'num_location':num_location,'num_case':num_case,'num_visits':num_visits},
    )
@login_required
def search(request):
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'HotZone/search.html',
    )


@login_required
def searchItem(request):
    if(request.method=='GET'):
        search= request.GET.get('search')
        #post= Location.objects().all().filter(Location=search)
        url='https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q='+search
        response = requests.get(url=url,headers={'Content-Type': 'application/json'})
        if response.status_code == 200:
            Array=json.loads(response.text)
            return render(
                request,
                'HotZone/searchResult.html',
                {'Array': Array}
            )
        else:
            return render(
                request,
                'HotZone/searchError.html',
            )

@login_required
def AddLocation(request):
    # Render the HTML template index.html with the data in the context variable
    print('index的值为',request.GET.get('index'))
    data= request.GET.get('index')
    data = data.replace("\'", "\"")
    print(data)
    Array=json.loads(data)
    Location.objects.create(
        Location=Array["nameEN"],
        Address=Array["addressEN"],
        XCoordinate=Array["x"],
        YCoordinate=Array["y"],
    )

    return render(
                request,
                'HotZone/Comfirm.html',
            )

class VirusListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view for a list of books."""
    model = Virus
    paginate_by = 10


class PatientListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view for a list of books."""
    model = Patient
    paginate_by = 10

class CaseListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view for a list of books."""
    model = Case
    paginate_by = 10

class LocationListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view for a list of books."""
    model = Location
    paginate_by = 10