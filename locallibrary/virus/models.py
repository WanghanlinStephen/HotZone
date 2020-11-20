from django.db import models


# Create your models here.
class Virus(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name
    # def get_absolute_url(self):
    #     """Returns the url to access a particular book instance."""
    #     return reverse('virus-detail', args=[str(self.id)])


class Case(models.Model):
    case_number = models.IntegerField()
    date = models.DateField(help_text="Enter the date of infecious")
    CATEGORY_CHOICES = (
        ("Local", 'Local'),
        ("Imported", 'Imported'),
    )
    category = models.CharField(max_length=32, choices=CATEGORY_CHOICES)
    virus = models.ForeignKey(Virus, on_delete=models.CASCADE)

    def __str__(self):
        return f'virus: {self.virus.name}, case_number: {self.case_number}'
    # def get_absolute_url(self):
    #     """Returns the url to access a particular book instance."""
    #     return reverse('case-detail', args=[str(self.id)])
