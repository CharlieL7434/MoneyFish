from django import forms
from django.contrib.auth.models import User
from moneyfishapp.models import UserProfile, Loans, Income, Outgoing, Debts

class LoansForm(forms.ModelForm):
    borrower = forms.CharField(max_length=128, help_text="Please enter the name of the person you are lending your money to")
    lvalue = forms.DecimalField(max_digits=8, decimal_places=2, help_text="Please enter the amount you will be lending.")

    class Meta:
        model = Loans
        fields = ('borrower', 'lvalue',)

class IncomeForm(forms.ModelForm):
    insource = forms.CharField(max_length=128, help_text="Please enter your income source.")
    invalue = forms.DecimalField(max_digits=8, decimal_places=2, help_text="Please enter the income amount")

    class Meta:
        model = Income
        fields = ('insource', 'invalue',)

class OutgoingForm(forms.ModelForm):
    outsource = forms.CharField(max_length=128, help_text="Please enter your outgoing source.")
    outvalue = forms.DecimalField(max_digits=8, decimal_places=2, help_text="Please enter outgoing amount")

    class Meta:
        model = Outgoing
        fields = ('outsource', 'outvalue',)

class DebtsForm(forms.ModelForm):
    lender = forms.CharField(max_length=128, help_text="Please enter your debt source.")
    dvalue = forms.DecimalField(max_digits=8, decimal_places=2, help_text="Please debt amount")

    class Meta:
        model = Debts
        fields = ('lender', 'dvalue',)


class UserForm(forms.ModelForm):
    #first_name = forms.CharField(max_length=128, help_text="Please enter your first name.")
    #surname = forms.CharField(max_length=128, help_text="Please enter your given surname.")
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)