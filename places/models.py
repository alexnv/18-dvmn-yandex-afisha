from django.db import models
from tinymce.models import HTMLField


# Create your models here.
class Place(models.Model):
    title = models.CharField(
        'Название',
        unique=True,
        max_length=200,
    )

    description_short = models.TextField(
        'Краткое описание',
        blank=True,
        null=True,
    )

    description_long = HTMLField(
        'Полное описание',
        blank=True,
        null=True,

    )

    lng = models.DecimalField(
        'Долгота',
        max_digits=22,
        decimal_places=16,
        blank=True,
        null=True,
    )

    lat = models.DecimalField(
        'Широта',
        max_digits=22,
        decimal_places=16,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title

    position = models.IntegerField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'места'


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField()

    position = models.IntegerField(
        default=1,
        db_index=True
    )

    def __str__(self):
        return self.image.name if self.image.name else ""

    class Meta:
        verbose_name = 'изображение'
        verbose_name_plural = 'изображения'
        ordering = ('position',)