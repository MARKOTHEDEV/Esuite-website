# Generated by Django 3.2 on 2021-12-16 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_countryaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryaddress',
            name='state',
            field=models.CharField(default='..', max_length=300),
        ),
    ]
