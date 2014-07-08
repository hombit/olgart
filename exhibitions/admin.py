from django.contrib import admin

from exhibitions.models import Exhibition


class ExhibitionAdmin(admin.ModelAdmin):
	list_filter = ['begin']


admin.site.register(Exhibition, ExhibitionAdmin)
