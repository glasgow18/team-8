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
                                                       phoneNumber=phoneNumber, min_age=min_age,max_age=max_age,gender=gender,
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
                             '01316631616', 16, 100, 'Phil Morris', '0', 'midlothian', 'exercise, art, environment')
    rowan.save()

    equal_access = eachOrganisation('equal access',
      'If you are from a minority ethnic community and experiencing feelings of stress, isolation, depression, anxiety or unhappiness, Equal Access can provide you with support and information to help you.',
      'http://www.health-in-mind.org.uk/services/rowan_respect_our_woodland_and_nature/d16/#parentHorizontalTab1',
      'monika.dyczko@health-in-mind.org.uk',
      '07776594315', 16, 100, 'Monika Dyczko', "0", 'midlothian',
      'psychology, psychological help, psychological support, support, depression, anxiety, unhapy')
    equal_access.save()


    midlothian_wellbeing = eachOrganisation('midlothian wellbeing access point',
      'If you’re feeling low and stressed and want to do something about it, there’s a service that couldn’t be easier to access – you just turn up.',
      'http://www.health-in-mind.org.uk/services/wellbeing_access_point/d99/#parentHorizontalTab1',
      'laurence.hawkings@health-in-mind.org.uk',
      '0131 536 8981', 18, 65, 'Lawrence Hawkings',"0", 'midlothian',
      'depression, anxiety, low mood, unhapy')
    midlothian_wellbeing.save()


    day_service = eachOrganisation('day service',
      'Health in Mind offers a wide range of activities and groups from our Orchard Centre in Bonnyrigg and in other community buildings in Midlothian.',
      'http://www.health-in-mind.org.uk/services/day_service/d46/',
      'reception@orchardcentreservices.org.uk',
      '0131 663 1616', 16, 100, 'The Orchard Centre', "0", 'midlothian',
      'social, socialise, go out')
    day_service.save()


    out_of_hours = eachOrganisation('out of hours',
      'Health in Mind\'s base in Bonnyrigg is the Orchard Centre and it offers a varied programme of activities that are updated every month.',
      'http://www.health-in-mind.org.uk/services/out_of_hours_service/d69/',
      'contactus@health-in-mind.org.uk',
      '0131 663 1616', 16, 100, 'The Orchard Centre',"0", 'midlothian',
      'social, socialise, art, arts')
    out_of_hours.save()


    mens_share = eachOrganisation('men\'s share',
      'The Men\'s SHARE Project provides an accessible comfortable space which offers social and emotional support.',
      'http://www.health-in-mind.org.uk/services/mens_share/d40/',
      'contactus@health-in-mind.org.uk',
      '0131 663 1616', 18, 100, 'The Orchard Centre', "1", 'midlothian',
      'depression, sad, lonely, unhappy')
    mens_share.save()


if __name__ == '__main__':
        print("Starting Bark population scripts...")
        populate()
