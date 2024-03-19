from django.shortcuts import render,redirect
from site_admin.models import *
from user.models import *
from django.contrib import messages



def index(request):
    return render( request,"common/index.html")

def login(request):
    return render(request,"common/login.html")

def loginAction(request):
    username = request.POST['username']
    password = request.POST['password']
    admin = Admin_tb.objects.filter(Username=username,Password=password)
    user = Register_tb.objects.filter(Username=username,Password=password)
    if admin.count()>0:
        messages.add_message(request,messages.INFO,"Login Succesfull")
        request.session['admin_id'] = admin[0].id
        return render(request,"admin/adminhome.html")
    elif user.count()>0:
        messages.add_message(request,messages.INFO,"Login Succesfull")
        request.session['userid'] = user[0].id
        return render(request,"user/userhome.html")
    else:
        messages.add_message(request,messages.INFO,"Login Failed")
        return redirect('login')

def adminhome(request):
    return render(request,"admin/adminhome.html")

def add_hobby(request):
    return render(request,"admin/add_hobby.html")

def add_hobbyAction(request):
    hobby = request.POST['hobby']
    add_hobby = Hobbyname_tb(Hobbyname=hobby)
    add_hobby.save()
    messages.add_message(request,messages.INFO,"Hobbies added succesfully")
    return redirect('adminhome')

def add_hobbyfactor(request):
    hobby = Hobbyname_tb.objects.all()
    return render(request,"admin/add_hobbyfactor.html",{'hob':hobby})
def add_hobbyfactorAction(request):
    hobby_id = request.POST['hobby']
    factor = request.POST['factor']
    add_hobbyfactor = Hobbyfactor_tb(Hobby_id_id = hobby_id,Factorname=factor)
    add_hobbyfactor.save()
    messages.add_message(request,messages.INFO,"Hobby factors Added Succesfully")
    return redirect('adminhome')
def add_season(request):
    return render(request,"admin/add_season.html")
def add_seasonAction(request):
    season = request.POST['season']
    add_season = Season_tb(Season_name=season)
    add_season.save()
    messages.add_message(request,messages.INFO,"Season added succesfully")
    return redirect("adminhome")
def add_seasonfactor(request):
    season = Season_tb.objects.all()
    return render(request,"admin/add_seasonfactor.html",{'seas':season})
def add_seasonfactorAction(request):
    season_id = request.POST['season']
    factor = request.POST['factor']
    add_seasonfactor = Seasonfactor_tb(Season_factorname = factor,Season_id_id = season_id)
    add_seasonfactor.save()
    messages.add_message(request,messages.INFO,"Season factors added succesfully")
    return redirect('adminhome')

def add_seasoncountry(request):
    season_data = Season_tb.objects.all()
    country_data = Country_tb.objects.all()
    return render(request,"admin/add_seasoncountry.html",{'season':season_data,'country':country_data})

def getseasonfactor(request):
    season = request.GET['s']
    data = Seasonfactor_tb.objects.filter(Season_id=season)
    return render(request,"admin/getseasonfactor.html",{'seasonfactor':data})

def getState(request):
    country = request.GET['co']
    data = State_tb.objects.filter(Country_id=country)
    return render(request,"admin/getState.html",{'state':data})

def seasoncountryAction(request):
    season_id = request.POST['season']
    season_factorid = request.POST['factor']
    country_id = request.POST['country']
    state_id = request.POST['state']
    month = request.POST['month']
    seasoncountry_data = Season_country_tb(Season_id_id=season_id,Season_factor_id_id=season_factorid,Country_id_id=country_id,State_id_id=state_id,Month=month)
    seasoncountry_data.save()
    messages.add_message(request,messages.INFO,"Season Country data added succesfully")
    return redirect("adminhome")

def addagefactor(request):
    return render(request,"admin/addagefactor.html")

def addagefactorAction(request):
    min_age = request.POST['min_age']
    max_age = request.POST['max_age']
    factor = request.POST['factor']
    agefactor_data = Agefactor_tb(Minimum_age =min_age,Maximum_age=max_age,Factor_name=factor)
    agefactor_data.save()
    messages.add_message(request,messages.INFO,"agefactors added succesfully")
    return redirect("adminhome")

def changepassword(request):
    return render(request,"admin/changepassword.html")

def changepasswordAction(request):
    admin_id = request.session['admin_id']
    admin_data = Admin_tb.objects.filter(id=admin_id)
    for i in admin_data:
        password = i.Password
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    if password == oldpassword:
        if newpassword == confirmpassword:
            data = Admin_tb.objects.filter(id=admin_id).update(Password = confirmpassword)
            messages.add_message(request,messages.INFO,"password updated")
        else:
            messages.add_message(request,messages.INFO,"Password mismatch")
    else:
        messages.add_message(request,messages.INFO,"Invalid Password")
    return redirect("adminhome")


    
        
        
# Create your views here.
