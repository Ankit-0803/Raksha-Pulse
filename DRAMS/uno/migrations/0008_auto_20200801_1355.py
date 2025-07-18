# Generated by Django 3.0.8 on 2020-08-01 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uno', '0007_auto_20200730_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('coordinates', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='nc_category',
            field=models.CharField(choices=[('parking', 'Police'), ('first-aid', 'Ambulance'), ('fire-extinguisher', 'Fire Brigade')], default='first-aid', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uno.City'),
        ),
    ]
