from django.contrib import admin

from django.contrib import admin
from moneyfishapp.models import UserProfile, Income, Outgoing, Loans, Debts, Friends

# Register your models here.
admin.site.register(Income)
admin.site.register(Outgoing)
admin.site.register(Loans)
admin.site.register(Debts)
admin.site.register(UserProfile)
