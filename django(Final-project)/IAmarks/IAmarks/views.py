from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def handlelogin(request):
    if request.method=='POST':
        usn=request.POST['usn']
        pass1=request.POST['password1']
        user=authenticate(username=usn,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"Login Successfull")
            return redirect('/student')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')

    return render(request,'login.html')




def signup(request):
    if request.method=='POST':
        usn=request.POST['usn']
        branch=request.POST['branch']
        sem=request.POST['sem']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        if pass1 != pass2:
            messages.warning(request,"Password does not match")
            return redirect('/signup')

        try:
            if User.objects.get(usn=usn):
                messages.warning(request,"USN Already Exist")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(usn,email,pass1)
        myuser.first_name=username
        myuser.last_name=branch
        myuser.save()
        messages.warning(request,"Signup Successfull, Please Go to Login")
        return redirect('/')

    return render(request,'signup.html')
