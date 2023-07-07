# Generated by Django 4.2.2 on 2023-07-05 12:19

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_remove_place_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lat',
            field=models.DecimalField(decimal_places=16, max_digits=22, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='place',
            name='lng',
            field=models.DecimalField(decimal_places=16, max_digits=22, verbose_name='Долгота'),
        ),
    ]