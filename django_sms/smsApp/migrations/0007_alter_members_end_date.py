# Generated by Django 4.1.7 on 2023-05-15 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smsApp', '0006_members_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='end_date',
            field=models.DateField(default=datetime.date(2024, 1, 31)),
        ),
    ]
