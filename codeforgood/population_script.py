import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'codeforgood.settings')
import django
django.setup()

from health_in_mind.models import organisations


def eachOrganisation(name, description, websiteUrl, emailAddress, phoneNumber,
	min_age, max_age, contact_name, gender, location, key_words):

	rowan = organisations.objects.get_or_create('rowan' ,'The ROWAN project encourages people to enjoy the benefits of being close to nature and the sense of wellbeing it offers.' , 'http://www.health-in-mind.org.uk/services/rowan_respect_our_woodland_and_nature/d16/#parentHorizontalTab1' , 'phil.morris@orchardcentreservices.org.uk', '01316631616', 16, 100, 0, 'midlothian', 'exercise, art, environment')






