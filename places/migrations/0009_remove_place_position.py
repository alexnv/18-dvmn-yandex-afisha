# Generated by Django 4.2.2 on 2023-07-03 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_alter_place_lat_alter_place_lng'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='position',
        ),
    ]
