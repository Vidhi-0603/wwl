# Generated by Django 5.0.3 on 2024-04-26 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0020_alter_property_bathrooms_alter_property_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='furnished',
            field=models.CharField(choices=[('Furnished', 'Furnished'), ('Not Furnished', 'Not Furnished'), ('Semi Furnished', 'Semi Furnished'), ('N/A', 'N/A')], max_length=128),
        ),
    ]
