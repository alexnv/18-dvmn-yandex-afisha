# Generated by Django 4.2.2 on 2023-07-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placeimage_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='placeimage',
            name='position',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]