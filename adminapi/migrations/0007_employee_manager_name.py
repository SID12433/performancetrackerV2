# Generated by Django 4.2.5 on 2024-06-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0006_projectdetail_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='manager_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]