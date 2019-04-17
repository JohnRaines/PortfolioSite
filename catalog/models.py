from django.db import models

# Create your models here.
class Pieces(models.Model):
	id = models.IntegerField(default="9999", primary_key=True)
	title = models.CharField(max_length=200, default="n/a")
	text = models.TextField(default = "n/a")
	series = models.IntegerField(default = "0")
	series_name = models.CharField(max_length=200, default="n/a")
	link = models.CharField(max_length=200, default = "n/a")
	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name_plural = "Pieces"