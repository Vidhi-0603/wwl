# Generated by Django 5.0.3 on 2024-04-26 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0021_alter_property_furnished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
