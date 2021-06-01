from django.shortcuts import render
import sqlite3
# Create your views here.

def Index(request):
    return render(request,'pollapp/Index.html')

def login(request):
    return render(request,'pollapp/login.html')

def register(request):
    db = sqlite3.connect('Registration')
    rs = db.cursor()
    return render(request,'pollapp/register.html')

