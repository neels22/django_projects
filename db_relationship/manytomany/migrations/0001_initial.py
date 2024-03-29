# Generated by Django 5.0.3 on 2024-03-28 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.CharField(max_length=30)),
                ('empname', models.CharField(max_length=30)),
                ('salary', models.CharField(default=0, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.CharField(max_length=30)),
                ('employee', models.ManyToManyField(to='manytomany.employee')),
            ],
        ),
    ]