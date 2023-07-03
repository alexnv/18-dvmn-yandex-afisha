# Generated by Django 4.2.2 on 2023-07-01 13:43

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_placeimage_options_alter_placeimage_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('position', models.IntegerField(db_index=True, default=1)),
            ],
            options={
                'verbose_name': 'изображение',
                'verbose_name_plural': 'изображения',
                'ordering': ('position',),
            },
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Полное описание'),
        ),
        migrations.DeleteModel(
            name='PlaceImage',
        ),
        migrations.AddField(
            model_name='image',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place'),
        ),
    ]