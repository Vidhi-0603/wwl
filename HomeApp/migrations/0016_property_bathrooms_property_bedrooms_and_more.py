# Generated by Django 5.0.3 on 2024-04-24 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0015_enquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(default='3'),
        ),
        migrations.AddField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(default='3'),
        ),
        migrations.AddField(
            model_name='property',
            name='furnished',
            field=models.CharField(choices=[('Furnished', 'Furnished'), ('Not Furnished', 'Not Furnished'), ('semi Furnished', 'Semi Furnished')], default='furnished', max_length=128),
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='posted_on',
            field=models.DateField(default=datetime.date(2024, 4, 24)),
        ),
        migrations.AlterField(
            model_name='property',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='updated',
            field=models.DateField(default=datetime.date(2024, 4, 24)),
        ),
    ]
