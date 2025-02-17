from django.shortcuts import render
from django.http import HttpResponse
from moneyfishapp.forms import UserForm, UserProfileForm, LoansForm, DebtsForm, IncomeForm, OutgoingForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from moneyfishapp.models import Loans, Debts, Income, Outgoing
from django.contrib.auth.models import User


def index(request):
	return render(request, 'moneyfishapp/index.html')

def debts(request):

	debt_list = Debts.objects.order_by('-dvalue')[:5]

	context_dict = {}
	context_dict['debts'] = debt_list

	return render(request, 'moneyfishapp/debts.html', context=context_dict)

def loans(request):

	loan_list = Loans.objects.order_by('-lvalue')[:5]

	context_dict = {}
	context_dict['loans'] = loan_list

	return render(request, 'moneyfishapp/loans.html', context=context_dict)

def friends(request):
	return HttpResponse("This is the friends page")

def money(request):
	income_list = Income.objects.order_by('-invalue')[:5]
	outgoing_list = Outgoing.objects.order_by('outvalue')[:5]

	context_dict = {}
	context_dict['income'] = income_list
	context_dict['outgoing'] = outgoing_list


	return render(request, 'moneyfishapp/myMoney.html', context=context_dict)

def add_loan(request, username_search):
	try:
		user = User.objects.get(username= username_search)
	except User.DoesNotExist:
		user = None

	if user is None:
		return redirect('money/')

	form = LoansForm()

	if request.method =='POST':
		form = LoansForm(request.POST)

		if form.is_valid():
			if user:
				loan = form.save(commit=False)
				loan.user = user
				loan.save()

			return redirect('/moneyfishapp/loans/')
		else:
			print(form.errors)
	context_dict = {'form': form, 'user':user}
	return render(request, 'moneyfishapp/add_loan.html', context=context_dict)

def add_debt(request, username_search):
	try:
		user = User.objects.get(username= username_search)
	except User.DoesNotExist:
		user = None

	if user is None:
		return redirect('money/')
	form = DebtsForm()

	if request.method == 'POST':
		form = DebtsForm(request.POST)

		if form.is_valid():
			if user:
				debt = form.save(commit=False)
				debt.user = user
				debt.save()
			return redirect('/moneyfishapp/debts/')
		else:
			print(form.errors)
	context_dict = {'form': form, 'user':user}
	return render(request, 'moneyfishapp/add_debt.html', context=context_dict)

def add_income(request, username_search):
	try:
		user = User.objects.get(username = username_search)
	except User.DoesNotExist:
		user = None

	if user is None:
		return redirect('money/')
	form = IncomeForm()

	if request.method == 'POST':
		form = IncomeForm(request.POST)

		if form.is_valid():
			if user:
				income = form.save(commit=False)
				income.user = user
				income.save()

			return redirect('/moneyfishapp/money/')
		else:
			print(form.errors)
	context_dict = {'form': form, 'user':user}
	return render(request, 'moneyfishapp/add_income.html', context = context_dict)


def add_outgoing(request, username_search):
	try:
		user = User.objects.get(username= username_search)
	except User.DoesNotExist:
		user = None

	if user is None:
		return redirect('money/')
	form = OutgoingForm()

	if request.method == 'POST':
		form = OutgoingForm(request.POST)

		if form.is_valid():
			if user:
				outgoing = form.save(commit=False)
				outgoing.user = user
				outgoing.save()

			return redirect('/moneyfishapp/money/')
		else:
			print(form.errors)
	context_dict = {'form': form, 'user':user}
	return render(request, 'moneyfishapp/add_outgoing.html', context=context_dict)
	

def register(request):
	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = UserProfileForm(request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()


			profile = profile_form.save(commit=False)
			profile.user = user

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			print(user_form.errors, profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	
	return render(request, 'moneyfishapp/register.html', context = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return redirect(reverse('moneyfishapp:index'))
			else:
				return HttpResponse("Your MoneyFish account is disabled.")
		else:
			print(f"Invalid login details: {username}, {password}")
			return HttpResponse("Invalid login details supplied.")
	else:
		return render(request, 'moneyfishapp/login.html')

@login_required
def user_logout(request):
	logout(request)
	return redirect(reverse('moneyfishapp:index'))