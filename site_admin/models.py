from django.db import models
from user.models import *
class Admin_tb(models.Model):
    Username = models.TextField(max_length = 20)
    Password = models.TextField(max_length = 20)

class Hobbyname_tb(models.Model):
    Hobbyname = models.TextField(max_length =20)

class Hobbyfactor_tb(models.Model):
    Factorname = models.TextField(max_length = 20)
    Hobby_id = models.ForeignKey(Hobbyname_tb,on_delete = models.CASCADE)

class Season_tb(models.Model):
    Season_name = models.TextField(max_length = 20)
class Seasonfactor_tb(models.Model):
    Season_factorname = models.TextField(max_length =20)
    Season_id = models.ForeignKey(Season_tb,on_delete=models.CASCADE)
    
class Season_country_tb(models.Model):
    Season_id = models.ForeignKey(Season_tb,on_delete=models.CASCADE)
    Season_factor_id = models.ForeignKey(Seasonfactor_tb,on_delete = models.CASCADE)
    Country_id = models.ForeignKey("user.Country_tb",on_delete=models.CASCADE)
    State_id = models.ForeignKey("user.State_tb",on_delete=models.CASCADE)
    Month = models.IntegerField()
    
class Agefactor_tb(models.Model):
    Minimum_age = models.IntegerField()
    Maximum_age = models.IntegerField()
    Factor_name = models.CharField(max_length=200)

# Create your models here.
