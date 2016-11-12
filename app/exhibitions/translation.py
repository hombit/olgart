from modeltranslation.translator import translator, TranslationOptions

from exhibitions.models import Exhibition


class ExhibitionTranslationOptions(TranslationOptions):
	fields = ('title', 'showroom',)
	required_languages = ('ru', 'en',)


translator.register(Exhibition, ExhibitionTranslationOptions)
