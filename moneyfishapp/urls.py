"""MoneyFish URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from moneyfishapp import views

app_name = 'moneyfishapp'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('debts/', views.debts, name='debts'),
    path('loans/', views.loans, name='loans'),
    path('money/', views.money, name='money'),
    path('friends/', views.friends, name='friends'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_loan/', views.add_loan, name='add_loan'),
    path('add_debt/', views.add_debt, name='add_debt'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_outgoing/', views.add_outgoing, name='add_outgoing'),
]
