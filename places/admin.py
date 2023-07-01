from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Place, PlaceImage


# Register your models here.


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'image',
        'position',
        'preview',

    )

    readonly_fields = ("preview",)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    fields = ('image', 'position',)

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    fields = (
        'title',
        'description_short',
        'description_long',
        'lng',
        'lat',)
    inlines = (PlaceImageInline,)
