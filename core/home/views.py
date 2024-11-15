from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):


    peoples = [
        {'name': 'Alice', 'age': int(15)},
        {'name': 'Bob', 'age': int(16)},
        {'name': 'Catty', 'age': int(17)},
        {'name': 'Duke', 'age': int(18)},
        {'name': 'Emilly', 'age': int(19)}
    ]   
    
    vegetable = ['pumpkin', 'tomato', 'potatoe']


    text = "sd  agar  asgsag wg a agaw  awg ae a weg "
    return render(request, "index.html", context= { 'page': 'Django Server' ,  'peoples': peoples, 'text': text, 'vegetable': vegetable})


def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)
def about(request):
    context = {'page' : 'About'}
    return render(request, "about.html", context)


def success_page(request):
    return HttpResponse("This is a success page niggaa")

