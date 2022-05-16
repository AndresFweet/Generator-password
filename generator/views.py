from django.shortcuts import render
#from django.http import HttpResponse 
import random 

def home(reques):
    return render(reques, 'home.html')

def about(request):
   return render(request, 'about.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    genereta_password = ''

    lenght = int(request.GET.get('lenght')) 

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) 
    if request.GET.get('special'):
        characters.extend(list('!@#$^&()-.+_'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    

    for x in range(lenght):
        genereta_password += random.choice(characters)

    return render(request, 'password.html', {'password': genereta_password})
