from django.shortcuts import render,redirect
from user.models import *
from site_admin.models import *
from django.contrib import messages
from site_admin.views import *
from django.http import JsonResponse
from datetime import date,datetime

def index(request):
    return render(request,"common/index.html")

def userhome(request):
    return render(request,"user/userhome.html")

def register(request):
    country = Country_tb.objects.all()
    hobby = Hobbyname_tb.objects.all()
    return render(request,"user/register.html",{'count':country,'hob':hobby})

def getstate(request):
    country  = request.GET['c']
    state = State_tb.objects.filter(Country_id=country)
    return render(request,"user/getstate.html",{'st':state})

def registerAction(request):
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    address = request.POST['address']
    country = request.POST['country']
    state = request.POST['state']
    phone = request.POST['phone']
    security = request.POST['security']
    answer = request.POST['answer']
    username = request.POST['username']
    password = request.POST['password']
    register = Register_tb(Name=name,Gender=gender,DOB=dob,Address=address,Country_id_id=country,State_id_id=state,Phone=phone,Security_question=security,Answer=answer,Username=username+"@myname.com",Password=password)
    register.save()
    hobby = request.POST.getlist('hobby')
    user_id = register.id
    for i in hobby:
        hobby_data = Hobby_tb(Hobby_id_id=i,User_id_id=user_id)
        hobby_data.save()
    messages.add_message(request,messages.INFO,"Registration Succesfull")
    return redirect('index')
def send_message(request):
    return render(request,"user/send_message.html")

def getreciever(request):
    reciever = request.GET['r']
    data = Register_tb.objects.filter(Username = reciever)
    if data.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})
def messageAction(request):
    user_id = request.session['userid']
    reciever = request.POST['reciever']
    subject = request.POST['subject']
    print(subject)
    message = request.POST['message']
    current_date = date.today()
    time = datetime.now().strftime("%H:%M")
    reciever_data = Register_tb.objects.filter(Username=reciever)
    for i in reciever_data:
        reciever_id = i.id
    message_data = Message_tb(Sender_id_id = user_id,Subject=subject,Message=message,Date=current_date,Time=time,Reciever_id_id=reciever_id,Status="pending",Filterstatus="pending")
    message_data.save()
    messages.add_message(request,messages.INFO,"Message send succesfully")
    return redirect("userhome")

def view_sendmsg(request):
    user_id = request.session['userid']
    message_data = Message_tb.objects.filter(Sender_id_id = user_id,Status__in=["pending","deleted by reciever"])
    return render(request,"user/view_sendmsg.html",{'message':message_data})

def delete_sender(request,id):
    delete_msg = Message_tb.objects.filter(id=id)
    for i in delete_msg:
        status = i.Status
    if status == "pending":
        delete_msg = Message_tb.objects.filter(id=id).update(Status="deleted by sender")
    else:
        delete_msg = Message_tb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Message deleted")
    return redirect("view_sendmsg")


def view_recievedmsg(request):
    user_id = request.session['userid']
    agefactor = Customer_agefactor_tb.objects.filter(User_id = user_id)
    for i in agefactor:
        msg = Message_tb.objects.filter(Reciever_id_id = user_id,Message__icontains = i.Agefactor_id.Factor_name).exclude(Sender_id__in = Blocklist_tb.objects.filter(User_id_id = user_id).values("Contact_id_id")).update(Filterstatus = "filtered")
    hobbyfactor = Customerhobby_factor_tb.objects.filter(User_id_id = user_id)
    for j in hobbyfactor:
        msg = Message_tb.objects.filter(Reciever_id_id = user_id,Message__icontains = j.Factor_id.Factorname).exclude(Sender_id__in = Blocklist_tb.objects.filter(User_id_id = user_id).values("Contact_id_id")).update(Filterstatus = "filtered")
    seasonfactor = Customerseason_factor_tb.objects.filter(User_id = user_id)
    for k in seasonfactor:
        msg = Message_tb.objects.filter(Reciever_id_id = user_id,Message__icontains = k.Factor_id.Season_factorname).exclude(Sender_id__in = Blocklist_tb.objects.filter(User_id_id = user_id).values("Contact_id_id")).update(Filterstatus = "filtered")
    contact_data = Contact_tb.objects.filter(User_id_id = user_id)
    for s in contact_data:
        contact_id = s.Contact_id_id
        print(contact_id)
        msg = Message_tb.objects.filter(Sender_id_id= contact_id).update(Filterstatus = "filtered") 
    received_msg = Message_tb.objects.filter(Reciever_id=user_id,Status__in=["pending","deleted by reciever"],Filterstatus = "filtered")
    return  render(request,"user/view_recievedmsg.html",{'rec':received_msg})

def trash(request):
    message_id = request.POST['message_id'] 
    trash = request.POST.getlist('trash')
    reciever_id = request.session['userid']
    current_date = date.today()
    time = datetime.now().strftime("%H:%M")
    for i in trash:
        trash_data = Message_tb.objects.filter(id=i).update(Status="move to trash")
        data = Trash_tb(Date=current_date,Time=time,Message_id_id = i,Reciever_id_id = reciever_id)
        data.save()
    messages.add_message(request,messages.INFO,"Added to Trash")
    return redirect("userhome")
    
def viewtrash(request):
    user_id = request.session['userid']
    trash_data = Trash_tb.objects.filter(Reciever_id_id = user_id)
    return render(request,"user/viewtrash.html",{'trash':trash_data})

def delete_trash(request,id):
    data= Trash_tb.objects.filter(id=id)
    for i in data:
        message_id = i.Message_id_id
    delete_trashdata = Trash_tb.objects.filter(id=id).delete()
    delete_data = Message_tb.objects.filter(id=message_id)
    for i in delete_data:
        status = i.Status
    if status == "pending" :
        delete_data = Message_tb.objects.filter(id=message_id).update(Status="deleted by reciever")
    elif status == "move to trash":
        delete_data = Message_tb.objects.filter(id=message_id).update(Status="deleted by reciever")
    else:
        delete_data = Message_tb.objects.filter(id=message_id).delete()
    messages.add_message(request,messages.INFO,"Message deleted")
    return redirect("viewtrash")
def forward(request,id):
    forward_data = Message_tb.objects.filter(id=id)
    return render(request,"user/forward.html",{'forward':forward_data})

def getReciever(request):
    reciever = request.GET['rec']
    data = Register_tb.objects.filter(Username = reciever)
    if data.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})

def forwardAction(request):
    sender_id = request.session['userid']
    reciever = request.POST['reciever']
    subject = request.POST['subject']
    message = request.POST['message']
    current_date = date.today()
    time = datetime.now().strftime("%H:%M")
    reciever_data = Register_tb.objects.filter(Username = reciever)
    for i in reciever_data:
        reciever_id = i.id
    forward_data = Message_tb(Sender_id_id=sender_id,Reciever_id_id=reciever_id,Subject=subject,Message=message,Date=current_date,Time=time,Status="pending",Filterstatus="pending")
    forward_data.save()
    messages.add_message(request,messages.INFO,"Message send succesfully")
    return redirect("view_recievedmsg")

def reply(request,id):
    reply_data = Message_tb.objects.filter(id=id)
    return render(request,"user/reply.html",{'reply':reply_data})

def replyAction(request):
    sender_id = request.session['userid']
    reciever = request.POST['reciever']
    subject = request.POST['subject']
    message = request.POST['message']
    current_date = date.today()
    time = datetime.now().strftime("%H:%M")
    reciever_data = Register_tb.objects.filter(Username = reciever)
    for i in reciever_data:
        reciever_id = i.id
    reply_data = Message_tb(Sender_id_id = sender_id,Reciever_id_id = reciever_id,Subject=subject,Message = message,Date=current_date,Time=time,Status="pending",Filterstatus="pending")
    reply_data.save()
    messages.add_message(request,messages.INFO,"Message send succesfully")
    return redirect("userhome")

def addcontact(request):
    return render(request,"user/addcontact.html")

def addcontactAction(request):
    user_id = request.session['userid']
    name = request.POST['name']
    current_date = date.today()
    time = datetime.now().strftime("%H:%M")
    remark = request.POST['remark']
    contact = request.POST['contact']
    contact_data = Register_tb.objects.filter(Username = contact)
    for i in contact_data:
        contact_id = i.id      
    add_contact = Contact_tb(Name=name,Date=current_date,Time=time,Remark=remark,Contact_id_id=contact_id,User_id_id=user_id)  
    add_contact.save()
    messages.add_message(request,messages.INFO,"Contact added succesfully")
    return redirect("userhome")

def getcontact(request):
    contact = request.GET['con']
    data = Register_tb.objects.filter(Username=contact)
    if data.count()>0:
        msg="exist"
    else:
        msg="not exist"
    return JsonResponse({'valid':msg})
def addblocklist(request):
    return render(request,"user/addblocklist.html")

def blocklistAction(request):
    user_id = request.session['userid']
    name = request.POST['name']
    contact = request.POST['contact']
    current_date = date.today()
    time = datetime.now().strftime("%H:%M")
    remark = request.POST['remark']
    blocklist_data = Register_tb.objects.filter(Username = contact)
    for i in blocklist_data:
        contact_id = i.id
    addblocklist_data = Blocklist_tb(Name=name,Date=current_date,Time=time,Remark=remark,Contact_id_id=contact_id,User_id_id=user_id)
    addblocklist_data.save()
    block_data = Blocklist_tb.objects.filter(User_id_id = user_id)
    messages.add_message(request,messages.INFO,"Added a blocklist")
    return redirect("userhome")

def getblocklist(request):
    contact = request.GET['cont']
    data = Register_tb.objects.filter(Username=contact)
    if data.count()>0:
        msg = "exist"
    else:
        msg = "not exist"
    return JsonResponse({'valid':msg})

def viewcontact(request):
    user_id = request.session['userid']
    contact_data = Contact_tb.objects.filter(User_id_id = user_id)
    return render(request,"user/viewcontact.html",{'contact':contact_data})

def delete_contact(request,id):
    delete_contact = Contact_tb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Deleted Succesfully")
    return redirect("viewcontact")
    
def movetoblocklist(request):
    blocklist = request.POST.getlist('blocklist')
    user_id = request.session['userid']
    current_date = date.today()
    time = datetime.now().strftime("%H:%M")
    for i in blocklist:
        blocklist_data = Contact_tb.objects.filter(id=i)
        for j in blocklist_data:
            name = j.Name
            remark = j.Remark
            contact_id = j.Contact_id_id
            movetoblocklist = Blocklist_tb(Name=name,Date=current_date,Time=time,Remark=remark,Contact_id_id=contact_id,User_id_id=user_id)
            movetoblocklist.save()
        delete_contact = Contact_tb.objects.filter(id=i).delete()
    messages.add_message(request,messages.INFO,"Succesfully moved to blocklist")
    return redirect("viewcontact")
    
def viewblocklist(request):
    user_id =request.session['userid']
    viewblocklist_data = Blocklist_tb.objects.filter(User_id_id = user_id)
    return render(request,"user/viewblocklist.html",{'viewblocklist':viewblocklist_data})

def delete_blocklist(request,id):
    delete_blocklist = Blocklist_tb.objects.filter(id=id).delete()
    messages.add_message(request,messages.INFO,"Deleted Succesfully")
    return redirect("viewblocklist")

def addcustomerhobby(request):
    hobby_data = Hobbyname_tb.objects.all()
    return render(request,"user/addcustomerhobby.html",{'hobby':hobby_data})

def getfactor(request):
    hobby = request.GET['hob']
    data = Hobbyfactor_tb.objects.filter(Hobby_id=hobby)
    return render(request,"user/getfactor.html",{'factor':data})

def customerhobbyAction(request):
    user_id = request.session['userid']
    hobby_id = request.POST['hobby']
    factor_id = request.POST['factor']
    customerhobby_data = Customerhobby_factor_tb(Factor_id_id=factor_id,Hobby_id_id=hobby_id,User_id_id=user_id)
    customerhobby_data.save()
    messages.add_message(request,messages.INFO,"Succesfully added customer hobbies ")
    return redirect("userhome")

def customeragefactor(request):
    user_id = request.session['userid']
    dob_data = Register_tb.objects.filter(id=user_id)
    for i in dob_data:
        dob = i.DOB
    dob_date = datetime.strptime(dob,'%d-%m-%Y')
    yob = dob_date.year
    print(yob)
    current_date = date.today()
    current_year = current_date.year
    print(current_year)
    age = current_year-yob
    print(age)
    age_factor_data = Agefactor_tb.objects.filter(Minimum_age__lte = age,Maximum_age__gte = age)
    return render(request,"user/customeragefactor.html",{'age_factor':age_factor_data})

def customerageAction(request):
    user_id = request.session['userid']
    factor_id = request.POST['factor_id']
    age_data = Customer_agefactor_tb(Agefactor_id_id = factor_id,User_id_id=user_id)
    age_data.save()
    messages.add_message(request,messages.INFO,"Age factor added succesfully")
    return redirect("userhome")

def customerseasonfactor(request):
    user_id = request.session['userid']
    customer_data = Register_tb.objects.filter(id=user_id)
    for i in customer_data:
        country_id = i.Country_id_id
        state_id = i.State_id_id
    current_date = date.today()
    current_month = current_date.month
    print(current_month)
    customer_seasonfactor_data = Season_country_tb.objects.filter(Country_id_id=country_id,State_id_id=state_id,Month=current_month)
    return render(request,"user/customerseasonfactor.html",{'seasonfactor':customer_seasonfactor_data})

def customerseasonAction(request):
    user_id = request.session['userid']
    factor_id = request.POST['factor']
    customerseason_data = Customerseason_factor_tb(User_id_id=user_id,Factor_id_id=factor_id)
    customerseason_data.save()
    return redirect("userhome")

def viewspam(request):
    user_id = request.session['userid']
    spam_data = Message_tb.objects.filter(Reciever_id_id= user_id,Filterstatus="pending",Status__in=["pending","deleted by sender"])
    return render(request,"user/viewspam.html",{'spam':spam_data})

def delete_spam(request,id):
    deletespam_data = Message_tb.objects.filter(id=id)
    for i in deletespam_data:
        status = i.Status
    if status == "pending":
        delete_data = Message_tb.objects.filter(id=id).update(Status="deleted by reciever")
    else:
        delete_data = Message_tb.objects.filter(id=id).delete()
    return redirect("userhome")

def updateprofile(request):
    user_id = request.session['userid']
    profile_data = Register_tb.objects.filter(id=user_id)
    hobby = Hobbyname_tb.objects.all()
    hobby_data = Hobby_tb.objects.filter(User_id_id = user_id)
    country_data = Country_tb.objects.all()
    return render(request,"user/updateprofile.html",{'prof':profile_data,'hob':hobby_data,'cntry':country_data,'hobs':hobby})

def updateprofileAction(request):
    user_id = request.session['userid']
    name = request.POST['name']
    gender = request.POST['gender']
    dob = request.POST['dob']
    phone = request.POST['phone']
    address = request.POST['address']
    country = request.POST['country']
    state = request.POST['state']
    hobby = request.POST.getlist('hobby')
    security = request.POST['security']
    answer = request.POST['answer']
    username = request.POST['username']
    update_data = Register_tb.objects.filter(id=user_id).update(Name=name,Gender=gender,DOB=dob,Address=address,Phone=phone,Country_id_id=country,State_id_id = state,Security_question = security,Answer = answer,Username=username)
    hobby_data = Hobby_tb.objects.filter(User_id_id = user_id).delete()
    for i in hobby:
        hobby_data = Hobby_tb(Hobby_id_id=i,User_id_id=user_id)
        hobby_data.save()
    messages.add_message(request,messages.INFO,"Profile Updated")
    return redirect("userhome")

def userchangepassword(request):
    return render(request,"user/userchangepassword.html")

def userpasswordAction(request):
    user_id = request.session['userid']
    prof_data = Register_tb.objects.filter(id=user_id)
    for i in prof_data:
        password = i.Password
    oldpassword = request.POST['oldpassword']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    if password == oldpassword:
        if newpassword == confirmpassword:
            pass_data = Register_tb.objects.filter(id=user_id).update(Password = confirmpassword)
            messages.add_message(request,messages.INFO,"Password updated")
        else:
            messages.add_message(request,messages.INFO,"Password mismatch")
    else:
        messages.add_message(request,messages.INFO,"Invalid password")
    return redirect("userhome")

def forgetpassword(request):
    return render(request,"user/forgetpassword.html")

def forgetpasswordAction(request):
    username = request.POST['username']
    password_data = Register_tb.objects.filter(Username=username)
    if password_data.count()>0:
        request.session['username'] = password_data[0].Username
        return render(request,"user/newpassword.html")
    else:
        messages.add_message(request,messages.INFO,"Invalid username")
    return redirect("index")

def newpassword(request):
    name = request.POST['name']
    dob = request.POST['dob']
    phone = request.POST['phone']
    password_data = Register_tb.objects.filter(Name=name,DOB=dob,Phone=phone)
    if password_data.count()>0:
        return render(request,"user/newpassword1.html")
    else:
        messages.add_message(request,messages.INFO,"Invalid data")
    return redirect("index")

def newpasswordAction(request):
    username = request.session['username']
    newpassword = request.POST['newpassword']
    confirmpassword = request.POST['confirmpassword']
    if newpassword == confirmpassword:
        Register_tb.objects.filter(Username = username).update(Password = confirmpassword)
        messages.add_message(request,messages.INFO,"Password changed")
    else:
        messages.add_message(request,messages.INFO,"Password mismatch")
    return redirect("index")

def logout(request):
    request.session.flush()
    return redirect("login")
# Create your views here.
