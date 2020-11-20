# Generated by Django 3.1.2 on 2020-11-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientcase',
            name='condition',
            field=models.CharField(choices=[('Recovered', 'Recovered'), ('Dead', 'Dead'), ('Recovering', 'Recovering')], default='Recovering', max_length=32),
        ),
    ]
