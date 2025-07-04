from django.shortcuts import render,redirect
from taskapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash


# Create your views here.
@login_required
def homepage(req):
    data=taskModel.objects.filter(user=req.user)
    inprogress=taskModel.objects.filter(user=req.user, status='inprogress')
    pending=taskModel.objects.filter(user=req.user, status='pending')
    completed=taskModel.objects.filter(user=req.user, status='completed')
    
    context={
        'data':data,
        'inprogress':inprogress,
        'pending':pending,
        'completed':completed,
    }


    return render(req,'homepage.html',context)


def registerpage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        email=req.POST.get('email')
        profile_picture=req.POST.get('profile_picture')
        bio=req.POST.get('bio')
        password=req.POST.get('password')
        confirm_password=req.POST.get('confirm_password')
        if password==confirm_password:
            customuserModel.objects.create_user(

                username=username,
                email=email,
                profile_picture=profile_picture,
                bio=bio,
                password=password,


            )
            return redirect('loginpage')

    return render(req,'registerpage.html')


def loginpage(req):
    if req.method == 'POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(req,username=username,password=password)
        if user:
            login(req,user)
            return redirect('homepage')


    return render(req,'loginpage.html')

@login_required
def logoutpage(req):
    logout(req)
    return redirect('loginpage')


@login_required
def tasklist(req):
    data=taskModel.objects.filter(user=req.user)
    context={
        'data':data
    }
    return render(req,'tasklist.html',context)

@login_required
def addtask(req):
    if req.method == 'POST':
        title=req.POST.get('title')
        description=req.POST.get('description')
        due_date=req.POST.get('due_date')
        priority=req.POST.get('priority')
        status=req.POST.get('status')

        data=taskModel(
            user=req.user,
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            status=status,

        )
        data.save()
        return redirect('tasklist')

    return render(req,'addtask.html')

@login_required
def editpage(req,id):
    data=taskModel.objects.get(id=id)
    context={
        'data':data
    }
    if req.method == 'POST':
        data.title=req.POST.get('title')
        data.description=req.POST.get('description')
        data.due_date=req.POST.get('due_date')
        data.priority=req.POST.get('priority')
        data.status=req.POST.get('status')
        data.save()
        return redirect('tasklist')

    return render(req,'editpage.html',context)

@login_required
def viewpage(req,id):
    data=taskModel.objects.get(id=id)
    context={
        'data':data
    }
    
    return render(req,'viewpage.html',context)

@login_required
def deletepage(req,id):
    data=taskModel.objects.get(id=id).delete()
    return redirect('tasklist')


def changepassword(req):
    current_user=req.user
    if req.method=='POST':
        old_password=req.POST.get('old_password')
        new_password=req.POST.get('new_password')
        confirm_password=req.POST.get('confirm_password')

        if check_password(old_password,req.user.password):
            if new_password==confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(req,current_user)

                return redirect('homepage')


    return render(req,'changepassword.html')

@login_required
def taskcompleted(req,id):
    data=taskModel.objects.get(id=id)
    data.status = 'completed'
    data.save()
    return redirect('tasklist')


def statusechange(req,id):
    data=taskModel.objects.get(id=id)

    if data.status== 'pending':
        data.status = 'inprogress'
    elif data.status == 'inprogress':
        data.status='completed'
    data.save()
    return redirect('tasklist')


def prioritychange(req,id):
    data=taskModel.objects.get(id=id)

    if data.priority=='low':
        data.priority='medium'

    elif data.priority=='medium':
        data.priority='high'
    data.save()
    return redirect('tasklist')