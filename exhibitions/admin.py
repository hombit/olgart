from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from exhibitions.models import Exhibition


class ExhibitionAdmin(TranslationAdmin):
	readonly_fields = ('get_img_tag_for_admin',)

	fieldsets = [
		(
			None, {
				'fields': (
					('begin', 'end',),
					'title',
					'showroom',
					'showroom_url',
					('image','get_img_tag_for_admin'),
				)
			}
		),
	]

	list_filter = ['begin','end']


admin.site.register(Exhibition, ExhibitionAdmin)
