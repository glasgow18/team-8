from django.db import models

class organisations(models.Model):
	name = models.CharField(max_length = 200,unique=True)
	description = models.CharField(max_length = 500)
	websiteUrl = models.URLField()
	emailAddress = models.CharField(max_length = 300)
	phoneNumber = models.CharField(max_length = 150)
	min_age = models.IntegerField(default=16)
	max_age=models.IntegerField(default=100)
	contact_name=models.CharField(max_length = 250)
	gender = models.CharField(max_length = 1)
	#sexuality = models.CharField(max_length = 200)
	#ethnicity = models.CharField(max_length = 200)
	#race = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200)
	key_words=models.CharField(max_length = 200)

	def __str__(self):  # For Python 2, use __unicode__ too
			return self.name


