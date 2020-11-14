from django.db import models
from django import forms 
from django.urls import reverse  

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

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('virus-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Case(models.Model):
    id= models.CharField(max_length=200,primary_key=True)
    caseNumber= models.IntegerField()
    date= models.DateTimeField(max_length=100,help_text="Enter the date of infecious")
    category= forms.ChoiceField(choices = Location_CHOICES)
    Virus= models.ForeignKey(Virus,on_delete=models.CASCADE, null=True)
    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('case-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return 'CaseNumber:%s' % (self.caseNumber)


class Patient(models.Model):
    id= models.CharField(max_length=200,primary_key=True)
    Name= models.CharField(max_length=200)
    DateofBrith=models.DateTimeField(max_length=100)
    Case=models.ForeignKey(Case,on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('patient-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Name

class Visit(models.Model):
    id= models.CharField(max_length=200,primary_key=True)
    Patient= models.ForeignKey(Patient,on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('visit-detail', args=[str(self.id)])
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.id

class Location(models.Model):
    Location= models.CharField(max_length=200)
    Address= models.CharField(max_length=200)
    XCoordinate= models.IntegerField()
    YCoordinate= models.IntegerField()
    DateFrom= models.DateTimeField(max_length=100,null=True, blank=True)
    DateTo= models.DateTimeField(max_length=100,null=True, blank=True)
    Category= forms.ChoiceField(choices = Type_CHOICES)
    Visit= models.ForeignKey(Visit,on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('location-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.Location

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    staff_number=models.IntegerField()
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)


    def __str__(self):
        return f'{self.user.username} Profile'
