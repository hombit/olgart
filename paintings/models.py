import os.path

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from django.utils.translation import ugettext_lazy as _
from io import BytesIO
from PIL import Image


class Gallery(models.Model):
	title = models.CharField( "Название", help_text="Одно слово", max_length=128 )
	position = models.IntegerField( "Положение", blank=True, null=True )
	
	class Meta:
		ordering = ('position',)
		verbose_name = 'Галерея'
		verbose_name_plural = 'Галереи'
	
	def get_absolute_url(self):
		return ( '/galleries/' + self.title_en + '/' )

	def save(self):
		if self.position == None:
			try:
				last = self.__class__.objects.order_by('-position')[0]
				self.position = last.position + 1
			except IndexError:
				self.position = 0
				
		super(Gallery, self).save()

	def __str__(self):
		return (self.title)


class Painting(models.Model): 
	SURFACES = (
		("canvas", _("canvas")),
		("wood panel", _("wood panel")),
		("cardboard", _("cardboard")),
		("paper", _("paper")),
	)
	MATERIALS = (
		("oil", _("oil")),
		("gouache", _("gouache")),
		("water-colour", _("water-colour")),
		("ink", _("ink")),
		("pencil", _("pencil")),
		("tempera", _("tempera")),
	)

	gallery = models.ForeignKey( 'Gallery', verbose_name='Галерея' )
	is_sold = models.BooleanField( "Продана", default=False )
	title = models.CharField( "Название", unique=True, max_length=256 )
	surface = models.CharField(
		"поверхность",
		max_length=32,
		choices=SURFACES,
		default=SURFACES[0]
	)
	material = models.CharField(
		"материал",
		max_length=32,
		choices=MATERIALS,
		default=MATERIALS[0]
	)
	height = models.IntegerField( "Высота", help_text="в см" )	
	width = models.IntegerField( "Ширина", help_text="в см" )
	year = models.IntegerField( "Год написания", help_text="4 цифры" )
	image = models.ImageField( "Файл с картинкой", help_text="только jpg", max_length=500, upload_to='images/paintings/' )
	image_small = models.ImageField( editable=False, max_length=500, upload_to='images/paintings/' )
	position = models.IntegerField( "Положение", blank=True, null=True )

	class Meta:
		ordering = ('position',)
		verbose_name = "Картина"
		verbose_name_plural = "Картины"

	def get_absolute_url(self):
		return ( "{}{}/".format(self.gallery.get_absolute_url(), self.id) )

	def get_img_tag_for_admin(self):
		if self.image_small:
			return ( u'<img src="{}" height="75" />'.format(self.image_small.url) )
		else:
			return ''
	get_img_tag_for_admin.allow_tags=True
	get_img_tag_for_admin.short_description="Картина"

	def produce_image_small(self):
		DJANGO_TYPE = 'image/jpeg'
		PIL_TYPE = 'jpeg'
		FILE_EXTENSION = 'jpg'
		thumb = Image.open(BytesIO(self.image.read()))
		thumb.thumbnail( settings.THUMBNAIL_SIZE, Image.ANTIALIAS )
		temp_handle = BytesIO()
		thumb.save(temp_handle, PIL_TYPE)
		temp_handle.seek(0)
		suf = SimpleUploadedFile( os.path.split(self.image.name)[-1], temp_handle.read(), content_type=DJANGO_TYPE )
		self.image_small.save( '%s_small.%s'%(os.path.splitext(suf.name)[0],FILE_EXTENSION), suf, save=False )

	def save(self):
		if self.position == None:
			try:
				last = self.__class__.objects.order_by('-position')[0]
				self.position = last.position + 1
			except IndexError:
				self.position = 0

		try:
			this = Painting.objects.get(id=self.id)
			if this.image != self.image:
				this.image.delete(save=False)
		except:
			pass

		self.produce_image_small()

		super(Painting, self).save()

	def __str__(self):
		return (self.title)
