from django import forms
from django.contrib.auth.models import User
from moneyfishapp.models import UserProfile, Income, Outgoing, Loans, Debts, Friends

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)


class IncomeForm(forms.ModelForm):
    insource = forms.CharField(max_length =128, help_text="Please enter income source.")
    invalue = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Income
        fields = ('insource', 'invalue',)


class OutgoingForm(forms.ModelForm):
    outsource = forms.CharField(max_length =128, help_text="Please enter payments.")
    outvalue = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Outgoing
        fields = ('outsource', 'outvalue',)


class LoansForm(forms.ModelForm):
    borrower = forms.CharField(max_length =128, help_text="Please enter loan source.")
    lnvalue = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Loans
        fields = ('borrower', 'lnvalue',)

    
class DebtsForm(forms.ModelForm):
    lender = forms.CharField(max_length =128, help_text="Please enter debts source.")
    dvalue = forms.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        model = Debts
        fields = ('lender', 'dvalue',)


class FriendsForm(forms.ModelForm):
    given_name = forms.CharField(max_length =128, help_text="Please enter first name.")
    family_name = forms.CharField(max_length =128, help_text="Please enter family name.")
    email = forms.EmailField(max_length=254,unique = True)

    class Meta:
        model = Friends
        fields = ('given_name', 'family_name','email',)
