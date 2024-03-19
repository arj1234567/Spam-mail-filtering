"""
URL configuration for spam_mail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_admin import views as adminviews
from user import views as userviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', adminviews.index,name="index"),
    path('login/',adminviews.login,name="login"),
    path('loginAction/',adminviews.loginAction,name="loginAction"),
    path('adminhome/',adminviews.adminhome,name="adminhome"),
    path('admin_hobby/',adminviews.add_hobby,name="add_hobby"),
    path('add_hobbyAction/',adminviews.add_hobbyAction,name="add_hobbyAction"),
    path('add_hobbyfactor/',adminviews.add_hobbyfactor,name="add_hobbyfactor"),
    path('add_hobbyfactorAction/',adminviews.add_hobbyfactorAction,name="add_hobbyfactorAction"),
    path('add_season/',adminviews.add_season,name="add_season"),
    path('add_seasonAction/',adminviews.add_seasonAction,name="add_seasonAction"),
    path('add_seasonfactor/',adminviews.add_seasonfactor,name="add_seasonfactor"),
    path('add_seasonfactorAction/',adminviews.add_seasonfactorAction,name="add_seasonfactorAction"),
    path('userhome/',userviews.userhome,name="userhome"),
    path('register/',userviews.register,name="register"),
    path('getstate/',userviews.getstate,name="getstate"),
    path('registerAction/',userviews.registerAction,name="registerAction"),
    path('send_message',userviews.send_message,name="send_message"),
    path('getreciever/',userviews.getreciever,name="getreciever"),
    path('messageAction/',userviews.messageAction,name="messageAction"),
    path('view_sendmsg/',userviews.view_sendmsg,name="view_sendmsg"),
    path('delete_sender<int:id>/',userviews.delete_sender,name="delete_sender"),
    path('view_recievedmsg/',userviews.view_recievedmsg,name="view_recievedmsg"),
    path('trash/',userviews.trash,name="trash"),
    path('viewtrash/',userviews.viewtrash,name="viewtrash"),
    path('delete_trash<int:id>/',userviews.delete_trash,name="delete_trash"),
    path('forward<int:id>/',userviews.forward,name="forward"),
    path('getReciever/',userviews.getReciever,name="getReciever"),
    path('forwardAction/',userviews.forwardAction,name="forwardAction"),
    path('reply<int:id>/',userviews.reply,name="reply"),
    path('replyAction/',userviews.replyAction,name="replyAction"),
    path('addcontact/',userviews.addcontact,name="addcontact"),
    path('addcontactAction/',userviews.addcontactAction,name="addcontactAction"),
    path('getcontact/',userviews.getcontact,name="getcontact"),
    path('addblocklist/',userviews.addblocklist,name="addblocklist"),
    path('blocklistAction/',userviews.blocklistAction,name="blocklistAction"),
    path('getblocklist/',userviews.getblocklist,name="getblocklist"),
    path('viewcontact/',userviews.viewcontact,name="viewcontact"),
    path('delete_contact<int:id>/',userviews.delete_contact,name="delete_contact"),
    path('movetoblocklist/',userviews.movetoblocklist,name="movetoblocklist"),
    path('viewblocklist/',userviews.viewblocklist,name="viewblocklist"),
    path('delete_blocklist<int:id>/',userviews.delete_blocklist,name="delete_blocklist"),
    path('addcustomerhobby/',userviews.addcustomerhobby,name="addcustomerhobby"),
    path('getfactor/',userviews.getfactor,name="getfactor"),
    path('customerhobbyAction/',userviews.customerhobbyAction,name="customerhobbyAction"),
    path('add_seasoncountry/',adminviews.add_seasoncountry,name="add_seasoncountry"),
    path('getseasonfactor/',adminviews.getseasonfactor,name="getseasonfactor"),
    path('getState/',adminviews.getState,name="getState"),
    path('seasoncountryAction/',adminviews.seasoncountryAction,name="seasoncountryAction"),
    path('addagefactor/',adminviews.addagefactor,name="addagefactor"),
    path('addagefactorAction/',adminviews.addagefactorAction,name="addagefactorAction"),
    path('customeragefactor/',userviews.customeragefactor,name="customeragefactor"),
    path('customerageAction/',userviews.customerageAction,name="customerageAction"),
    path('customerseasonfactor/',userviews.customerseasonfactor,name="customerseasonfactor"),
    path('customerseasonAction/',userviews.customerseasonAction,name="customerseasonAction"),
    path('viewspam/',userviews.viewspam,name="viewspam"),
    path('delete_spam<int:id>/',userviews.delete_spam,name="delete_spam"),
    path('updateprofile/',userviews.updateprofile,name="updateprofile"),
    path('updateprofileAction/',userviews.updateprofileAction,name="updateprofileAction"),
    path('changepassword/',adminviews.changepassword,name="changepassword"),
    path('changepasswordAction/',adminviews.changepasswordAction,name="changepasswordAction"),
    path('userchangepassword/',userviews.userchangepassword,name="userchangepassword"),
    path('userpasswordAction/',userviews.userpasswordAction,name="userpasswordAction"),
    path('forgetpassword/',userviews.forgetpassword,name="forgetpassword"),
    path('forgetpasswordAction/',userviews.forgetpasswordAction,name="forgetpasswordAction"),
    path('newpassword/',userviews.newpassword,name="newpassword"),
    path('newpasswordAction/',userviews.newpasswordAction,name="newpasswordAction"),
    path('logout/',userviews.logout,name="logout"),
    
]
