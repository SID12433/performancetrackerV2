# Generated by Django 4.2.5 on 2024-06-29 14:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizer', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.PositiveIntegerField()),
                ('data', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.CharField(max_length=100)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.employee')),
                ('teamlead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.teamlead')),
            ],
        ),
        migrations.CreateModel(
            name='DailyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=100)),
                ('is_completed', models.BooleanField(default=False)),
                ('emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.employee')),
                ('teamlead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapi.teamlead')),
            ],
        ),
    ]
