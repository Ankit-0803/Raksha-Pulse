# Generated by Django 3.0.8 on 2020-08-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uno', '0011_location_cctv'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='coordinates',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
