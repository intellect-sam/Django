# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Hello world i im at home')
    return render(request, 'home.html')

def aboutPage(request):
    # return HttpResponse('This is the about page')
    return render(request, 'about.html')

def loginPage(request):
    return render(request, 'login.html')