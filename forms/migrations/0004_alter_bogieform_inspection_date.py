# Generated by Django 5.2.4 on 2025-07-14 08:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_rename_insepction_by_bogieform_inspection_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bogieform',
            name='inspection_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
