from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Place, PlaceImage


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'place',
        'image',
        'position',
        'preview',
    )
    list_display = ['title', ]
    readonly_fields = ("preview",)

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')


class PlaceImageInline(SortableStackedInline):
    model = PlaceImage
    fields = ['image', 'preview', ]

    readonly_fields = ("preview",)

    def preview(self, model):
        return mark_safe(f'<img src="{model.image.url}" style="max-height: 200px;">')

    def get_extra(self, request, obj=Place, ):
        extra = 2
        if obj:
            return extra - obj.images.count()
        return extra


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = (
        'title',
        'description_short',
        'description_long',
        'lng',
        'lat',)
    inlines = (PlaceImageInline,)
