# Generated by Django 3.2 on 2021-12-16 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinentLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='countryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=300)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CountryLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=300)),
                ('continent_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.continentlocation')),
            ],
        ),
    ]
