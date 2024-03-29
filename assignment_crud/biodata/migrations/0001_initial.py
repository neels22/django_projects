# Generated by Django 5.0.3 on 2024-03-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('photo', models.ImageField(upload_to='photo/')),
                ('resume', models.FileField(upload_to='resume/')),
            ],
        ),
    ]