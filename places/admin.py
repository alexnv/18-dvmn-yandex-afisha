from adminsortable2.admin import SortableStackedInline, SortableAdminBase
from django.contrib import admin
from django.utils.html import format_html

from .models import Place, Image


class PreviewMixin(object):
    def preview(self, model):
        url = model.image.url
        return format_html('<img src="{}" style="max-height: 200px;">', url)


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin, PreviewMixin):
    fields = (
        'place',
        'image',
        'position',
        'preview',
    )

    readonly_fields = ('preview',)


class ImageInline(SortableStackedInline, PreviewMixin):
    model = Image
    fields = ['image', 'preview', ]

    readonly_fields = ('preview',)

    def get_extra(self, request, obj=None, **kwargs):
        return 0 if obj.images.exist() else 2


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    fields = (
        'title',
        'description_short',
        'description_long',
        'lng',
        'lat',
    )
    inlines = (ImageInline,)
