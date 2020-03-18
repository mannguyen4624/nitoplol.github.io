from django.shortcuts import render
from django.http import HttpResponse
from backend.models import User

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
    data = request.POST
    print(data)
    new_user = User(
      first=data.get('first'),
      last=data.get('last'),
      email=data.get('email'),
      role=data.get('ident'),
      password=data.get('psw')
       )
    new_user.save()
    #handle login, make database requests, save info, etc.
    # print(request.POST.get('email'))
    context = {'first_name': data.get('first')}
    return render(request, 'backend/confirmation.html', context)

def handle_adding_class(request):
  if request.method == "GET":
    return render(request, 'backend/addClassStudent.html')
  else:
    #handle adding a class
    pass

def handle_forgot(request):
  if request.method == "GET":
    return render(request, 'backend/forgotPassword.html')
  else:
    #handle them forgetting their password and requesting a new one
    pass