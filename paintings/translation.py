from modeltranslation.translator import translator, TranslationOptions

from paintings.models import Gallery, Painting


class GalleryTranslationOptions(TranslationOptions):
	fields = ('title',)
	required_languages = ('ru', 'en',)


class PaintingTranslationOptions(TranslationOptions):
	fields = ('title',)
	required_languages = ('ru', 'en',)


translator.register(Gallery, GalleryTranslationOptions)
translator.register(Painting, PaintingTranslationOptions)
