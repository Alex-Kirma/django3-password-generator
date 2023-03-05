from django.shortcuts import render
from django.shortcuts import HttpResponse 
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    lenght = int(request.GET.get('lenght'))
    
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHLMBOPRESTUVWXYZ')
    
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    
    if request.GET.get('special'):
        characters.extend('!@#$%^&*()')
    
    thepassword =''
    for x in range(lenght):
        thepassword += random.choice(characters)
    
    return render(request, 'generator/password.html', { 'password': thepassword } )

def description(request):
    return render(request, 'generator/description.html')