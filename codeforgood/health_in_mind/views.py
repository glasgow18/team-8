from django.shortcuts import render
from django.http import HttpResponse
#from health_in_mind.models import organisations
#from codeforgood.health_in_mind.models import organisations
from health_in_mind.models import organisations

# Create your views here.



def start(request):
    return render(request, 'chatbot.html')