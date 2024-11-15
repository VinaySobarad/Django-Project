from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url="/login/")
def receipes(request):
    
    if request.method =="POST":
        data =request.POST
        
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        # print(name)
        # print(description)
        # print(image)

        Receipe.objects.create(
        name = name,
        description = description,
        image = image,
        )

        return redirect('/receipes/')
    

    queryset = Receipe.objects.all()


    if request.GET.get('search'):
       queryset = queryset.filter(name__icontains = request.GET.get('search'))

    context = {'receipes': queryset} 

    return render(request, 'receipes.html', context)


@login_required(login_url="/login/")
def delete_receipe(request, id):


    print(f"Attempting to delete Receipe with id: {id}")  # Debugging

    queryset = Receipe.objects.get(id =id)
    queryset.delete()

    print(f"Receipe with id {id} deleted successfully.")  # Debugging

    # print(id)
    return redirect('/receipes/') 
    # print(f"Received request to delete Receipe with id: {id}")
    # try:
    #     receipe = get_object_or_404(Receipe, id=id)
    #     print(f"Deleting Receipe: {receipe.name}")
    #     receipe.delete()
    # except Exception as e:
    #     print(f"Error while deleting receipe: {e}")
    # return redirect('/receipes/')


@login_required(login_url="/login/")
def update_receipe(request ,id):
    # queryset = Receipe.objects.get(id =id)
    queryset = Receipe.objects.get(id=id)


    if request.method == "POST":

        data =request.POST
        name = data.get('name')
        description = data.get('description')
        image = request.FILES.get('image')

        queryset.name = name
        queryset.description = description

        if image:
            queryset.image = image

        queryset.save()
        return redirect('/receipes/')
    

    context = {'receipe': queryset}
    return render (request, 'update_receipes.html', context) 


def login_page(request):


    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username= username).exists():
            messages.info(request, "Invalid Username")
            return redirect('/login/')    
        

        user = authenticate(username= username, password = password)
        
        if user is None:
            messages.info(request, "Invalid Password")
            return redirect('/login/')    
        else:
            login(request, user)
            return redirect('/receipes/')
    return render(request, 'login.html')



def logout_page(request):
    logout(request )
    return redirect('/login/')




def register(request):
   
    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = User.objects.filter(username = username)

        if(user.exists()):
            messages.info(request, "Username already taken")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()
        messages.info(request, "Account Created Successfully!!")
        return redirect('/register/')


    return render(request, 'register.html')