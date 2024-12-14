# Generated by Django 5.0.3 on 2024-05-13 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HomeApp', '0031_agentsinfo_operating_since'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('message', models.TextField()),
                ('contact', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HomeApp.members')),
            ],
        ),
        migrations.DeleteModel(
            name='login',
        ),
    ]
