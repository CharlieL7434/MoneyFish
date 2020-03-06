from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("This is the index page")

def debts(request):
	return HttpResponse("This is the debts page")

def money(request):
	return HttpResponse("This is the money page")

def login(request):
	return HttpResponse("This is the login page")

# Create your views here.
