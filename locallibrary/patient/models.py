from django.db import models
from virus.models import *


# Create your models here.
class Patient(models.Model):
    """
    Basic info for patient
    """
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=32, unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f'name: {self.name} number: {self.number}'


class PatientCase(models.Model):
    """
    Patient-Case
    """
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    CONDITION_CHOICES = (
        ('Recovered', 'Recovered'),
        ('Dead', 'Dead'),
        ('Recovering', 'Recovering')
    )
    condition = models.CharField(max_length=32, choices=CONDITION_CHOICES, default='Recovering')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'patient: {self.patient.name} case: {self.case.case_number}'
