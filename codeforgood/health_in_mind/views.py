from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import redirect,get_object_or_404
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




def start(request):
    #if request.method == 'POST':
    user_input=request.POST.get("message")
    if "suicide" in str(user_input):
        print("please no")




    return render(request, 'chatbot.html')