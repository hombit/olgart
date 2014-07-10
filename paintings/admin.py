from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from paintings.models import Gallery, Painting


class GalleryAdmin(TranslationAdmin):
	pass


class PaintingAdmin(TranslationAdmin):
	fieldsets = [
		(
			None, {
				'fields' : (
					'gallery',
					'title',
					('surface', 'material',),
					('height', 'width',),
					'is_sold',
					'image',
				)
			}
		),
	]

	list_display = ('title','get_img_tag_for_admin','gallery','is_sold','position',)
	list_editable = ('is_sold','position',)
	list_filter = ('gallery','is_sold',)

	class Media:
		js = (
			'http://yandex.st/jquery/2.1.1/jquery.min.js',
			'http://yandex.st/jquery-ui/1.10.4/jquery-ui.min.js',
			'js/admin-list-reorder.js',
		)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Painting, PaintingAdmin)
