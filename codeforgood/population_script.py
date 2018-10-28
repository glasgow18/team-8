import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'codeforgood.settings')
import django

django.setup()

from health_in_mind.models import organisations


def eachOrganisation(name, description, websiteUrl, emailAddress, phoneNumber, min_age, max_age, contact_name, gender,
                     location, key_words):
    organisation = organisations.objects.get_or_create(name=name, description=description,
                                                       websiteUrl=websiteUrl, emailAddress=emailAddress,
                                                       phoneNumber=phoneNumber, min_age=min_age,max_age=max_age,
                                                       contact_name=contact_name, location=location,
                                                       key_words=key_words)[0]
    print(organisation)
    organisation.save()
    print(organisation)
    return organisation


def populate():
    rowan = eachOrganisation('rowan',
                             'The ROWAN project encourages people to enjoy the benefits of being close to nature and the sense of wellbeing it offers.',
                             'http://www.hesalth-in-mind.org.uk/services/rowan_respect_our_woodland_and_nature/d16/#parentHorizontalTab1',
                             'phil.morris@orchardcentreservices.org.uk',
                             '01316631616', '16', '100', 'Phil Morris', '0', 'midlothian', 'exercise, art, environment')
    rowan.save()

if __name__ == '__main__':
        print("Starting Bark population scripts...")
        populate()
