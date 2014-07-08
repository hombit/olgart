from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from exhibitions.models import Exhibition


class ExhibitionAdmin(TranslationAdmin):
	list_filter = ['begin']
	
	fieldsets = [
		(
			None, {
				'fields': (
					('begin',
					'end',),
					'title',
					'showroom',
					'showroom_url',
					'image',
				)
			}
		),
	]


admin.site.register(Exhibition, ExhibitionAdmin)
