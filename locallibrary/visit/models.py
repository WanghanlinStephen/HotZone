from django.db import models

# Create your models here.
from patient.models import *


class PatientVisit(models.Model):
    """
    病人访问
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_of_visit = models.DateField()
    date_of_confirmed = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'patient: {self.patient.name} date_of_visit: {self.date_of_visit}'


class Location(models.Model):
    """
    地点
    """
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    x = models.IntegerField()
    y = models.IntegerField()
    is_from_api = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f'address: {self.address} x: {self.x} y: {self.y}'


class VisitLocation(models.Model):
    """
    访问-地点
    """
    visit = models.ForeignKey(PatientVisit, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # location = models.CharField(max_length=200)
    # address = models.CharField(max_length=200)
    # XCoordinate = models.IntegerField()
    # YCoordinate = models.IntegerField()
    date_from = models.DateField()
    date_to = models.DateField()
    CATEGORY_CHOICES = (
        ("Visit", "Visit"),
        ("Residence", "Residence"),
        ("Workplace", "Workplace"),
    )
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f'visit: {str(self.visit)} location: {str(self.location)}'
