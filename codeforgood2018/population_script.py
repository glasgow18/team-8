

import django
django.setup()


def add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport):
    organisation = organisations.objects.get_or_create(name = name, description = description,
                                                       emailAddress = emailAddress,phoneNumber = phoneNumber, age = age,
                                                       gender = gender, sexuality = sexuality, ethnicity = ethnicity,
                                                       race  = race, typeOfSupport = typeOfSupport)
    organisation.url = websiteUrl
    organisation.save()


def population():
    rowan = add_organisation(name = 'rowan', description = 'The ROWAN project encourages people to enjoy the benefits of being close to nature and the sense of wellbeing it offers.',
                             websiteUrl = 'http://www.health-in-mind.org.uk/services/rowan_respect_our_woodland_and_nature/d16/#parentHorizontalTab1',
                             emailAddress = 'phil.morris@orchardcentreservices.org.uk', phoneNumber = '0131 663 1616' ,
                             age = 0, gender = 'any', sexuality = 'any', ethnicity = 'any', race = 'any', typeOfSupport = ['walks', 'bushcraft', 'conservation', 'art']))

if __name__ == '__main__':
    print('Starting population scripts...')
    population()