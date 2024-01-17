from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

