# Generated by Django 5.0.7 on 2024-07-13 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('waitlists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='waitlistentry',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
