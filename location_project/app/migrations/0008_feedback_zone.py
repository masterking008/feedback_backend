# Generated by Django 5.1.5 on 2025-01-21 17:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_zone_comment_zone_name_alter_zone_coordinates_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='zone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.zone'),
        ),
    ]
