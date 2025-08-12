from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from logisticsapp.models import *

# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message'],
        )
        mycontact.save()
        return redirect('/')
    else:
        return render(request, 'contact.html')


def Myquote(request):
    if request.method == "POST":
        myquotes = quote(
            departure = request.POST['departure'],
            Delivery = request.POST['delivery'],
            Weight = request.POST['weight'],
            Dimensions = request.POST['dimensions'],
            name = request.POST['name'],
            email = request.POST['email'],
            phone = request.POST['phone'],
            message = request.POST['message'],

        )
        myquotes.save()
        return redirect('/')

    else:
        return render(request, 'get-a-quote.html')

def index(request):
    return render(request,'index.html')

def pricing(request):
    return render(request,'pricing.html')

def service(request):
    return render(request,'service-details.html')

def services(request):
    return render(request,'services.html')

def starter(request):
    return render(request,'starter-page.html')

def show(request):
    all = quote.objects.all()
    return render(request,'show.html',{'all':all})

def show(request):
    all = Contact.objects.all()
    return render(request, 'show.html',{'all':all})

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, password=password)
                user.save()

                messages.success(request, 'Account created successfully')
                return redirect('/login')
            except:
                messages.error(request, 'Username already exists')

        else:
            messages.error(request, 'Passwords do not match')

    return render(request, 'register.html')

def loginview(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('/home')
        else:
            messages.error(request, 'Invalid login credentials')

    return render(request,'login.html')


