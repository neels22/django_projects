# Generated by Django 5.0.3 on 2024-03-28 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetoone', '0004_alter_employee_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.AddField(
            model_name='address',
            name='employee',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='onetoone.employee'),
        ),
    ]