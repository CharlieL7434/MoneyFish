from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=254,unique = True)
    given_name = models.CharField(max_length =128)
    family_name = models.CharField(max_length =128)
    def __str__(self):
        return "%s %s" (self.given_name, self.family_name)


class Income(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    insource = models.CharField(max_length =128)
    invalue = models.DecimalField(max_digits=8, decimal_places=2)
   
    def __str__(self):
        return self.insource

class Outgoing(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    outsource  = models.CharField(max_length =128)
    outvalue = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.outsource

class Loans(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    borrower = models.CharField(max_length =128)
    lvalue = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.lsource
    

class Debts(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    lender = models.CharField(max_length =128)
    dvalue = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return self.dsource

class Friends(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    given_name = models.CharField(max_length =128)
    family_name = models.CharField(max_length =128)
    email = models.EmailField(max_length=254,unique = True)
    # user = models.ManyToManyField(User)    
    
    def __str__(self):
        return "%s %s" (self.given_name, self.family_name)
    


