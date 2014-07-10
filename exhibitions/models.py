from django.db import models


class Exhibition(models.Model):
	title = models.CharField( "Название", max_length=1024 )
	begin = models.DateField( "Дата начала" )
	end = models.DateField( "Дата окончания" )
	showroom = models.CharField( "Выставочный зал", max_length=1024 )
	showroom_url = models.CharField( "Ссылка", blank=True, null=True, max_length=255 )
	image = models.ImageField( "Картинка", blank=True, null=True, max_length=500, upload_to="images/exhibitions/" )

	class Meta:
		ordering = ['-begin']
		verbose_name = 'Выставка'
		verbose_name_plural = 'Выставки'

	def save(self):
		if self.showroom_url:
			if self.showroom_url[:4] != 'http':
				self.showroom_url = 'http://' + self.showroom_url
		super(Exhibition, self).save()
	
	def __str__(self):
			return (self.title)