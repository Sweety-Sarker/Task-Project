
from django.contrib import admin
from django.urls import path
from taskapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage,name='homepage'),
    path('',registerpage,name='registerpage'),
    path('loginpage/',loginpage,name='loginpage'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('changepassword/',changepassword,name='changepassword'),
    path('tasklist/',tasklist,name='tasklist'),
    path('addtask/',addtask,name='addtask'),
    path('editpage/<str:id>',editpage,name='editpage'),
    path('viewpage/<str:id>',viewpage,name='viewpage'),
    path('deletepage/<str:id>',deletepage,name='deletepage'),

    
    path('taskcompleted/<str:id>',taskcompleted,name='taskcompleted'),
    path('statusechange/<str:id>',statusechange,name='statusechange'),
    path('prioritychange/<str:id>',prioritychange,name='prioritychange'),
    
]
