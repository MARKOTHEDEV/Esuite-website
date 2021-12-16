# Generated by Django 3.2 on 2021-12-16 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParthershipNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='WorkWithus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=300)),
                ('upload_cv', models.FileField(upload_to='emtrics_cv/')),
            ],
        ),
    ]