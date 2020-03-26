from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = {'boldmessage': 'this page leads to the login and register page'}
	return render(request, 'moneyfishapp/index.html')

def debts(request):
	return render(request, 'moneyfishapp/debts.html')

def loans(request):
	return render(request, 'moneyfishapp/loans.html')

def friends(request):
	return HttpResponse("This is the login page")

def money(request):
	return render(request, 'moneyfishapp/myMoney.html')

def login(request):
	return render(request, 'moneyfishapp/login.html')

# Create your views here.
