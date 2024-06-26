# Generated by Django 5.0.3 on 2024-03-28 05:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetoone', '0003_alter_employee_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='onetoone.address'),
        ),
    ]
