from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect,get_object_or_404
import datetime

#from health_in_mind.models import organisations
#from codeforgood.health_in_mind.models import organisations
from health_in_mind.models import organisations
'''
def get_split_lsit():
    organisations.objects.get()
print(organisations.objects)
#returns a filtered list
def check_keywords()
'''
# Create your views here.


red_flags=["suicide","suicidal","given up","end","life"]

def start(request):
    if request.method == 'POST':
        user_input=request.POST.get("message")
        for el in red_flags:
            if(el)in user_input:
                return redirect('http://breathingspace.scot/?fbclid=IwAR0-9xPonE8ww577E4YyahD4b921XOolWNXSU4XuGNDTj7O6NFEB3HVprTE')
        age,gender=user_input.split(" ")
        if (gender=="female"):
            numeric_gender="1"
        elif(gender=="male"):
            numeric_gender="0"
        else:numeric_gender="2"
        print(age,gender)

        target=organisations.objects.filter(gender=numeric_gender)
        print(target)
    messages=["So here are some options:"]





    return render(request, 'chatbot.html',context={"messages":messages})