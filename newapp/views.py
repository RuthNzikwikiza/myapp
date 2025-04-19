from django.shortcuts import render

def home(request):
    context = {
        'title': 'Welcome to My Homepage'
    }
    return render(request,'newapp/home.html', context)

def contact(request):
    return render(request,'newapp/contact.html' )