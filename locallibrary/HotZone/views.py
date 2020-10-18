from django.shortcuts import render
from django.shortcuts import render
from .models import Virus,Patient,Case,Location
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
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