import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'MoneyFish.settings')

import django
django.setup()
from MoneyFish.moneyfishapp.models import User,Income,Outgoing,Loans,Debts,Friends
from random import randint

def populate():

    pauline_in = [{'insource':'Employment','invalue':randint(0,1000)},{'insource':'Student loan','invalue':randint(0,6000)}]
    pauline_out = [{'outsource':'rent','outvalue':randint(0,1000)},{'outsource':'utill','outvalue':randint(0,1000)}]
    pauline_loan = [{'borrower':'jane doe','lvalue':randint(0,1000)},{'borrower':'john smith','lvalue':randint(0,1000)}]
    pauline_debts =[{'lender':'leon crooks','dvalue':randint(0,1000)},]
    pauline_friends = [{'email':'LeonDCrooks@teleworm.us ','given_name':'leon','family_name':'crooks'},{'email':'janedoe@teleworm.us ','given_name':'jane','family_name':'doe'} ]

    user = {'PaulineGOlson@armyspy.com' :{'given_name':'Pauline', 'family_name':'Olson', 'income':pauline_in, 'outgoing':pauline_out,
    'loans':pauline_loan, 'debts':pauline_debts, 'friends':pauline_friends }}

    for user,user_data in user.items():
        u = add_user(user,user_data['given_name'],user_data['family_name'])
        for i in user_data['income']:
            add_income(u,i['insource'],i['invalue'])
        for o in user_data['outgoing']:
            add_outgoing(u,o['oursource'],o['outvalue'])
        for l in user_data['loans']:
            add_loans(u,l['borrower'],l['lvalue'])
        for d in user_data['debts']:
            add_debts(u,d['lender'],d['dvalue'])
        for f in user_data['friends']:
            add_friends(u,f['email'],f['given_name'],f['family_name'])

    for u in User.objects.all():
        for i in Income.objects.filter(user=u):
            print(f'-{u}: {i}')
        for o in Outgoing.objects.filter(user=u):
            print(f'-{u}: {i}')
        for l in Loans.objects.filter(user=u):
            print(f'-{u}: {i}')
        for d in Debts.objects.filter(user=u):
            print(f'-{u}: {i}')
        for f in Friends.objects.filter(user=u):
            print(f'-{u}: {i}')

def add_income(user, source, value):
    i = Income.objects.get_or_create(user=user,insource=source)[0]
    i.invalue = value
    i.save()
    return i

def add_outgoing(user, source, value):
    o = Outgoing.objects.get_or_create(user=user,outsource=source)[0]
    o.outvalue = value
    o.save()
    return o

def add_loans(user, source, value):
    l = Loans.objects.get_or_create(user=user,borrower=source)[0]
    l.lvalue = value
    l.save()
    return l

def add_debts(user, source, value):
    d = Debts.objects.get_or_create(user=user,lender=source)[0]
    d.invalue = value
    d.save()
    return d

def add_friends(user ,email, gname, fname):
    f = Friends.objects.get_or_create(user=user,email = email)[0]
    f.given_name = gname
    f.family_name = fname
    f.save()
    return f

def add_user(email, gname, fname):
    u = User.objects.get_or_create(email=email)[0]
    u.given_name = gname 
    u.family_name = fname
    u.save()
    return u

# Start execution here!
if __name__ == '__main__':
    print('Starting population script...')
    populate()

