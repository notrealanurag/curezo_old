# Generated by Django 3.0.5 on 2020-04-25 20:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=50, unique=True)),
                ('doctor_type', models.CharField(max_length=50)),
                ('hospital_name', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('time', models.TimeField()),
                ('tests', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
