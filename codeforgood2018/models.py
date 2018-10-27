from django.db import models
from django_mysql.models import ListCharField

class organisations(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	description = models.CharField(max_length = 500, unique = True)
	websiteUrl = models.URLField()
	emailAddress = models.CharField(max_length = 300, unique = True)
	phoneNumber = models.CharField(max_length = 150, unique = True)
	age = models.IntegerField()
	gender = models.CharField(max_length = 200, unique = True)
	sexuality = models.CharField(max_length = 200, unique = True)
	ethnicity = models.CharField(max_length = 200, unique = True)
	race = models.CharField(max_length = 200, unique = True)
	location = models.CharField(max_length = 200, unique = True)
	#typeOfSupport = ListCharField()







