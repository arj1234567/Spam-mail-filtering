from django.db import models
from site_admin.models import *

class Country_tb(models.Model):
    Country_name = models.TextField(max_length = 20)

class State_tb(models.Model):
    State_name = models.TextField(max_length =20)
    Country_id = models.ForeignKey(Country_tb,on_delete=models.CASCADE)

class Register_tb(models.Model):
    Name = models.TextField(max_length =20)
    Gender = models.TextField(max_length = 20)
    DOB = models.TextField(max_length = 20)
    Address = models.TextField(max_length =20)
    Country_id = models.ForeignKey(Country_tb,on_delete = models.CASCADE)
    State_id = models.ForeignKey(State_tb,on_delete = models.CASCADE)
    Phone = models.TextField(max_length = 20)
    Security_question = models.TextField(max_length = 20)
    Answer = models.TextField(max_length =20)
    Username = models.TextField(max_length =20)
    Password = models.TextField(max_length =20)

class Hobby_tb(models.Model):
    User_id = models.ForeignKey(Register_tb,on_delete = models.CASCADE)
    Hobby_id = models.ForeignKey("site_admin.Hobbyname_tb",on_delete = models.CASCADE)
    
class Message_tb(models.Model):
    Sender_id = models.ForeignKey(Register_tb,related_name = 'sender_id',on_delete=models.CASCADE)
    Subject = models.TextField(max_length = 20)
    Message = models.TextField(max_length = 20)
    Date = models.TextField(max_length =20)
    Time = models.TextField(max_length =20)
    Reciever_id = models.ForeignKey(Register_tb,related_name = 'reciever_id',on_delete=models.CASCADE)
    Status = models.TextField(max_length =20)
    Filterstatus = models.TextField(max_length =20)
    
class Trash_tb(models.Model):
    Date = models.TextField(max_length =20)
    Time = models.TextField(max_length = 20)
    Message_id = models.ForeignKey(Message_tb,on_delete = models.CASCADE)
    Reciever_id = models.ForeignKey(Register_tb, related_name="reciever_Id",on_delete = models.CASCADE)
    
class Contact_tb(models.Model):
    Contact_id = models.ForeignKey(Register_tb,related_name='contact_id',on_delete = models.CASCADE)
    User_id = models.ForeignKey(Register_tb,related_name = "user_id" ,on_delete = models.CASCADE)
    Name = models.TextField(max_length = 20)
    Date = models.TextField(max_length = 20)
    Time = models.TextField(max_length = 20)
    Remark = models.TextField(max_length =20)
    
class Blocklist_tb(models.Model):
    Contact_id = models.ForeignKey(Register_tb,related_name = 'contact_Id',on_delete = models.CASCADE)
    User_id = models.ForeignKey(Register_tb,related_name = "user_Id",on_delete = models.CASCADE)
    Name = models.TextField(max_length = 20)
    Date = models.TextField(max_length = 20)
    Time = models.TextField(max_length = 20)
    Remark = models.TextField(max_length = 20)
    
class Customerhobby_factor_tb(models.Model):
    User_id = models.ForeignKey(Register_tb,related_name='user_ID',on_delete = models.CASCADE)
    Hobby_id = models.ForeignKey("site_admin.Hobbyname_tb",on_delete=models.CASCADE)
    Factor_id = models.ForeignKey("site_admin.Hobbyfactor_tb",on_delete = models.CASCADE)
    
class Customer_agefactor_tb(models.Model):
    User_id = models.ForeignKey(Register_tb,related_name = "user_iD",on_delete = models.CASCADE)
    Agefactor_id = models.ForeignKey("site_admin.Agefactor_tb",on_delete = models.CASCADE)

class Customerseason_factor_tb(models.Model):
    User_id = models.ForeignKey(Register_tb,related_name="user",on_delete=models.CASCADE)
    Factor_id = models.ForeignKey("site_admin.Seasonfactor_tb",on_delete=models.CASCADE)
# Create your models here.
