from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from paintings.models import Gallery, Painting


class GalleryAdmin(TranslationAdmin):
	pass


class PaintingAdmin(TranslationAdmin):
	list_display = ('title','get_img_tag_for_admin','gallery','is_sold',)
	list_editable = ('is_sold',)
	list_filter = ('gallery','is_sold',)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Painting, PaintingAdmin)
