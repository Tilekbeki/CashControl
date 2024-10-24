# Generated by Django 5.1.2 on 2024-10-16 04:02

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cashcontrolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('income', 'Доход'), ('expense', 'Расход')], default='expense', max_length=10),
        ),
    ]
