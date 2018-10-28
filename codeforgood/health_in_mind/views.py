from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
organisations = {'name': {
    'rowan': {'general information':
                  {'description': '''The ROWAN project encourages people to enjoy the benefits of being 
			close to nature and the sense of wellbeing it offers.''',
                   'website link': 'http://www.health-in-mind.org.uk/services/rowan_respect_our_woodland_and_nature/d16/#parentHorizontalTab1',
                   'visiting information': 'no information provided',
                   'contact details': {'location': {
                       'midlothian': {'name': 'Phil Morris', 'email': 'phil.morris@orchardcentreservices.org.uk',
                                      'phone number': '01316631616'}, }, }, },
              'target audience': {'demographics': {'lower_age': 0, 'upper_age': 0, 'gender': 'any', 'sexuality': 'any',
                                                   'ethnicity': 'any',
                                                   'race': 'any'},
                                  },
              'typeOfSupport': {'walks', 'bushcraft', 'conservation', 'art'},
              },

    'equal access': {'general information':
                         {'description': '''The ROWAN project encourages people to enjoy the benefits of being 
			close to nature and the sense of wellbeing it offers.''',
                          'website link': 'http://www.health-in-mind.org.uk/services/rowan_respect_our_woodland_and_nature/d16/#parentHorizontalTab1',
                          'visiting information': 'no information provided',
                          'contact details': {'location': {
                              'midlothian': {'name': 'Monika Dyczko', 'email': 'monika.dyczko@health-in-mind.org.uk',
                                             'phone number': '07776594315'},
                              'east lothian': {'name': 'Krzysztof Nowak',
                                               'email': 'krzysztofNowak@health-in-mind.org.uk',
                                               'phone number': 'no phone number available'}, }, }, },
                     'target audience': {
                         'demographics': {'lower_age': 16, 'upper_age': 100, 'gender': 'any', 'sexuality': 'any',
                                          'ethnicity': 'minority',
                                          'race': 'any'},
                         },
                     'typeOfSupport': {'depression', 'isolation', 'anxiety', 'unhapiness'},
                     },

    'midlothian wellbeing access point': {'general information':
                                              {'description': '''If you’re feeling low and stressed and want to do something about it, there’s a service that couldn’t 
			be easier to access – you just turn up.''',
                                               'website link': 'http://www.health-in-mind.org.uk/services/wellbeing_access_point/d99/#parentHorizontalTab1',
                                               'visiting information': {'loganlea centre': {
                                                   'address': 'Eastfield Medical Centre at Eastfield Farm Roa',
                                                   'days': 'monday',
                                                   'times': {'from': '9:30am', 'to': '11:30am'}, },
                                                                        'midlothian community hospital': {
                                                                            'address': '70 Eskbank Road in Bonnyrigg ',
                                                                            'days': 'wednesday',
                                                                            'times': {'from': '1pm', 'to': '3pm'}, }, },
                                               'contact details': {'location': {
                                                   'midlothian': {'name': 'Lawrence Hawkings',
                                                                  'email': 'laurence.hawkings@health-in-mind.org.uk',
                                                                  'phone number': '0131 536 8981'},
                                                   }, }, },
                                          'target audience': {
                                              'demographics': {'lower_age': 18, 'upper_age': 65, 'gender': 'any',
                                                               'sexuality': 'any', 'ethnicity': 'any',
                                                               'race': 'any'},
                                              },
                                          'typeOfSupport': {'mood', 'stress', 'confidence', 'self-esteem'},
                                          },

    'day service': {'general information':
                        {'description': '''Health in Mind offers a wide range of activities and groups from our Orchard Centre in Bonnyrigg 
			and in other community buildings in Midlothian. ''',
                         'website link': 'http://www.health-in-mind.org.uk/services/day_service/d46/',
                         'visiting information': 'no information provided',
                         'contact details': {'location': {
                             'midlothian': {'name': 'day service', 'email': 'reception@orchardcentreservices.org.uk',
                                            'phone number': '0131 663 1616'},
                             '': {'name': '', 'email': '',
                                  'phone number': ''}, }, }, },
                    'target audience': {
                        'demographics': {'lower_age': 0, 'upper_age': 0, 'gender': 'any', 'sexuality': 'any',
                                         'ethnicity': 'any',
                                         'race': 'any'},
                        },
                    'typeOfSupport': {'service': '',
                                      'keywords': {'social', 'relaxation', 'art', 'arts', 'craft', 'crafts', 'music',
                                                   'discussion', 'group', 'swim', 'swimming',
                                                   'knit', 'knitting', 'stitch', 'photography'}, },
                    },

    'out of hours': {'general information':
                         {'description': '''Health in Mind's base in Bonnyrigg is the Orchard Centre and it offers a 
			varied programme of activities that are updated every month. ''',
                          'website link': 'http://www.health-in-mind.org.uk/services/out_of_hours_service/d69/',
                          'visiting information': 'no information given',
                          'contact details': {'location': {
                              'midlothian': {'name': 'The Orchard Centre', 'email': 'contactus@health-in-mind.org.uk',
                                             'phone number': '0131 663 1616'},
                              '': {'name': '', 'email': '',
                                   'phone number': ''}, }, }, },
                     'target audience': {
                         'demographics': {'lower_age': 0, 'upper_age': 0, 'gender': 'any', 'sexuality': 'any',
                                          'ethnicity': 'any',
                                          'race': 'any'},
                         },
                     'typeOfSupport': {'service': '', 'keywords': {'social', 'bingo'}, },
                     },

    'early intervention and crisis line': {'general information':
                                               {'description': '''If you have mental ill-health and are experiencing a non-medical crisis, the Early Intervention Crisis 
			Response Service can arrange for an experienced member of the team to meet with you. They will assist you in any 
			appropriate way to resolve what is causing you concern. ''',
                                                'website link': 'http://www.health-in-mind.org.uk/services/early_intervention_and_crisis_response_service/d47/',
                                                'visiting information': 'no information given',
                                                'contact details': {'location': {
                                                    'midlothian': {'name': 'The Orchard Centre',
                                                                   'email': 'contactus@health-in-mind.org.uk',
                                                                   'phone number': '0131 663 1616'},
                                                    '': {'name': '', 'email': '',
                                                         'phone number': ''}, }, }, },
                                           'target audience': {
                                               'demographics': {'lower_age': 0, 'upper_age': 0, 'gender': 'any',
                                                                'sexuality': 'any', 'ethnicity': 'any',
                                                                'race': 'any'},
                                               },
                                           'typeOfSupport': {'service': 'face to face',
                                                             'keywords': {'social', 'bingo'}, },
                                           },

    'men\'s share': {'general information':
                         {
                             'description': '''The Men's SHARE Project provides an accessible comfortable space which offers social and emotional support. ''',
                             'website link': 'http://www.health-in-mind.org.uk/services/mens_share/d40/',
                             'visiting information': {
                                 'dalkeith mva': {'address': '4-6 White Hart Street', 'days': 'thursday',
                                                  'times': {'from': 'not defined yet', 'to': 'not defined yet'}, },
                                 'penicuik town hall ': {'address': '33 High Street', 'days': 'thursday',
                                                         'times': {'from': 'not defined yet',
                                                                   'to': 'not defined yet'}, },
                                 'newbattle education centre': {'address': '67 Gardiner Place', 'days': 'monday',
                                                                'times': {'from': '9:30am', 'to': '11:30am'}, },
                                 'loanhead leisure centre': {'address': 'George Avenue', 'days': 'monday',
                                                             'times': {'from': '5:30am', 'to': 'undefined'}, },
                                 },
                             'contact details': {'location': {'midlothian': {'name': 'The Orchard Centre',
                                                                             'email': 'contactus@health-in-mind.org.uk',
                                                                             'phone number': '0131 663 1616'},
                                                              }, }, },
                     'target audience': {
                         'demographics': {'lower_age': 18, 'upper_age': 100, 'gender': 'male', 'sexuality': 'any',
                                          'ethnicity': 'any',
                                          'race': 'any'},
                         },
                     'typeOfSupport': {'service': '',
                                       'keywords': {'support', 'social', 'emotional', 'isolated', 'lonely',
                                                    'loneliness'}, },
                     },

},

}

def start(request):
    return render(request, 'chatbot.html')


"""def collectDemographics():
    userDemographics = []

    userInput = input('''Hello, thank you for getting in touch. Before we start, could you please give me a few details about yourself?/n
		Please answer with yes/no''')
    if userInput == 'yes':
        age = input('Could you please tell me what your age is?')
        gender = input('What is your gender (e.g. male/female/androgenous)?')
        userDemographics.append(age)
        userDemographics.append(gender)
        # print(userDemographics)
        print('Thank you for this information! This will help me provide you with customised recommendations.')
    else:
        pass


def check():
    check = True

    collectDemographics()
    checkSituation = input('How can I help you today?')
    print(checkSituation)

    while check:
        if 'quit' in checkSituation:
            check = False


check()
"""