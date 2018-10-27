import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeforgood2018.settings')


import django
django.setup()
from codeforgood.models import organisations


def add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport):
    organisation = organisations.objects.get_or_create(name = name, description = description,
                                                       emailAddress = emailAddress,phoneNumber = phoneNumber, age = age,
                                                       gender = gender, sexuality = sexuality, ethnicity = ethnicity,
                                                       race  = race, typeOfSupport = typeOfSupport, location = location)
    organisation.url = websiteUrl
    organisation.save()


def population():
    rowan = add_organisation(name = 'rowan', description = 'The ROWAN project encourages people to enjoy the benefits of being close to nature and the sense of wellbeing it offers.',
                             websiteUrl = 'http://www.health-in-mind.org.uk/services/rowan_respect_our_woodland_and_nature/d16/#parentHorizontalTab1',
                             emailAddress = 'phil.morris@orchardcentreservices.org.uk', phoneNumber = '0131 663 1616' ,
                             age = 0, gender = 'any', sexuality = 'any', ethnicity = 'any', race = 'any', typeOfSupport = 'walks, bushcraft, conservation, art')
    equalAccess = add_organisation(name = 'equal access', description = 'At Health in Mind,  we understand  how cultural differences can influence our feelings and emotions and how we respond to the challenges in our lives.',
                                   websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    midlothianWellbeingAccessPoint = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    reDiscover = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    dayService = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    outOfHours = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    earlyInterventionAndCrisisLine = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    supportAtHome = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    menShare = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    traumaSupport = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    clear = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    artPsychotherapy = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    guidedSelfHelp = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    midspace = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    counselling = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    eastspace = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    tcls = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    resolve = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    wellbeingCollege = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    socialPrescribing = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    swDevelopment = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    craigmillerCounselling = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    seCounselling = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    peerCollaborative = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    anxietyAndDepressionPeerSupport = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    loopsHospitalDischarge = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    edspace = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    wellbeingInTheFerry = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    theListeningSpace = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    loopsCommunityNavigator = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    oasis = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    wellbeingGateway = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    communityMentalhealthAndWellbeing = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))
    westSpace = add_organisation(name, description, websiteUrl, emailAddress, phoneNumber, age, gender, sexuality, ethnicity, race, typeOfSupport))





if __name__ == '__main__':
    print('Starting population scripts...')
    population()