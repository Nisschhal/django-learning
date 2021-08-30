from django.db import models


# Create your models here.
class Topic(models.Model):
	top_name = models.CharField(max_length=200, unique=True)

	def __str__(self):
		return self.top_name


class WebPage(models.Model):
	topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
	web_page_name = models.CharField(max_length=200, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.web_page_name


class AccessRecord(models.Model):
	web_page_name = models.ForeignKey(WebPage, on_delete=models.CASCADE)
	date = models.DateTimeField()

	def __str__(self):
		return self.date
