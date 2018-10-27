from django.db import models



class organisations(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	description = models.CharField(max_length = 500)
	websiteUrl = models.URLField()
	emailAddress = models.CharField(max_length = 300)
	phoneNumber = models.CharField(max_length = 150)
	age = models.IntegerField()
	gender = models.CharField(max_length = 200)
	sexuality = models.CharField(max_length = 200)
	ethnicity = models.CharField(max_length = 200)
	race = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200)
	typeOfSupport = models.CharField(max_length= 500)






