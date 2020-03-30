from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    picture = models.ImageField(upload_to='profile_images', blank=True)
    #email = models.EmailField(max_length=254,unique = True)
    #given_name = models.CharField(max_length =128)
    #family_name = models.CharField(max_length =128)
    def __str__(self):
        return self.user.username
        
class Income(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    insource = models.CharField(max_length =128)
    invalue = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Income'

    def __str__(self):
        return self.insource

class Outgoing(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    outsource  = models.CharField(max_length =128)
    outvalue = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Outgoing'

    def __str__(self):
        return self.outsource

class Loans(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    borrower = models.CharField(max_length =128)
    lvalue = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Loans'

    def __str__(self):
        return self.lsource
    

class Debts(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    lender = models.CharField(max_length =128)
    dvalue = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta:
        verbose_name_plural = 'Debts'
        
    def __str__(self):
        return self.dsource

class Friends(models.Model):
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    given_name = models.CharField(max_length =128)
    family_name = models.CharField(max_length =128)
    email = models.EmailField(max_length=254,unique = True)
    # user = models.ManyToManyField(User)    
    
    def __str__(self):
        return "%s %s" (self.given_name, self.family_name)