from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': 'this page leads to the login and register page'}
	return render(request, 'moneyfishapp/bootstrap-base.html', context=context_dict)

def debts(request):
	return HttpResponse("This is the debts page")

def money(request):
	return HttpResponse("This is the money page")

def login(request):
	return HttpResponse("This is the login page")

# Create your views here.
