# Generated by Django 5.0.3 on 2024-04-30 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0024_alter_property_bathrooms_alter_property_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
