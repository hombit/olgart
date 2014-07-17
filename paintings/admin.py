from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from paintings.models import Gallery, Painting


class GalleryAdmin(TranslationAdmin):
	fieldsets = [
		(
			None, {
				'fields' : (
					'title',
				)
			}
		)
	]

	list_display = ( 'title', 'position', )
	list_editable = ( 'position', )

	class Media:
		js = (
			'http://yandex.st/jquery/2.1.1/jquery.min.js',
			'http://yandex.st/jquery-ui/1.10.4/jquery-ui.min.js',
			'js/jquery.ui.touch-punch.min.js',
			'js/admin-list-reorder.js',
		)


class PaintingAdmin(TranslationAdmin):
	readonly_fields = ('get_img_tag_for_admin',)
	fieldsets = [
		(
			None, {
				'fields' : (
					'gallery',
					'title',
					('surface', 'material',),
					('width', 'height',),
					'year',
					'is_sold',
					('image', 'get_img_tag_for_admin'),
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
			'js/jquery.ui.touch-punch.min.js',
			'js/admin-list-reorder.js',
		)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Painting, PaintingAdmin)
