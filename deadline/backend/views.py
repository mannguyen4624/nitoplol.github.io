from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'backend/index.html')

def handle_login(request):
  return render(request, 'backend/calendar.html')

def handle_classes(request):
  return render(request, 'backend/classes.html')

def handle_calendar(request):
  return render(request, 'backend/calendar.html')

def handle_account_creation(request):
  if request.method == "GET":
    return render(request, 'backend/creation.html')
  else:
    #handle login, make database requests, save info, etc.
    return render(request, 'backend/confirmation.html')

def handle_adding_class(request):
  if request.method == "GET":
    return render(request, 'backend/addClassStudent.html')
  else:
    #handle adding a class
    pass