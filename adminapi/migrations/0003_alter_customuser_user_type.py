# Generated by Django 4.2.5 on 2024-06-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapi', '0002_meeting_technologies_rating_dailytask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('manager', 'manager'), ('employee', 'employee'), ('teamlead', 'teamlead')], max_length=50),
        ),
    ]