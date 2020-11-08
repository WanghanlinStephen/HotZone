from django.db import models
from django import forms 

Location_CHOICES =( 
    ("Local"), 
    ("Imported"), 
) 
Type_CHOICES =(
    ("Visit"),
    ("Residence"),
    ("Workplace"),
),

# Create your models here.


class Virus(models.Model):
    id= models.CharField(max_length=200,primary_key=True)
    name= models.CharField(max_length=200,null=True)
    dateofBrith=models.DateTimeField(max_length=100,null=True)
    

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Patient(models.Model):
    id= models.CharField(max_length=200,primary_key=True)
    Name= models.CharField(max_length=200)
    DateofBrith=models.DateTimeField(max_length=100)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Name

class Case(models.Model):
    caseNumber= models.IntegerField()
    date= models.DateTimeField(max_length=100,help_text="Enter the date of infecious")
    category= forms.ChoiceField(choices = Location_CHOICES)
    Virus= models.ForeignKey(Virus,on_delete=models.CASCADE, null=True)
    Patient=models.ForeignKey(Patient,on_delete=models.CASCADE, null=True)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return 'CaseNumber:%s' % (self.caseNumber)

class Visit(models.Model):
    Patient= models.ForeignKey(Patient,on_delete=models.CASCADE, null=True)

class Location(models.Model):
    Location= models.CharField(max_length=200)
    Address= models.CharField(max_length=200)
    XCoordinate= models.IntegerField()
    YCoordinate= models.IntegerField()
    DateFrom= models.DateTimeField(max_length=100,null=True, blank=True)
    DateTo= models.DateTimeField(max_length=100,null=True, blank=True)
    Category= forms.ChoiceField(choices = Type_CHOICES)
    Visit= models.ForeignKey(Visit,on_delete=models.CASCADE, null=True)
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Location

