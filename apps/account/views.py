from django.shortcuts import render

# Our libs import
from django.http import HttpResponse

# Create your views here.
# |-----| Profile page
def home(request):
    return HttpResponse("Welcome to the lobby of account app")

# |-----| 
def account(request):
    return HttpResponse("Your profile page")