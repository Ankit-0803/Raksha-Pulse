# Generated by Django 3.0.8 on 2020-08-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uno', '0009_auto_20200801_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='disaster_status',
            field=models.CharField(default=0, max_length=5, null=True),
        ),
    ]
