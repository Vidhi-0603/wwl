# Generated by Django 5.0.3 on 2024-04-20 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0010_alter_property_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_image',
            field=models.FileField(default=None, null=True, upload_to='property_images/'),
        ),
    ]
