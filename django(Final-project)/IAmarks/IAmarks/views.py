from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from student.models import Contact,Signup,Branch,Semister
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def handleLogout(request):
    logout(request)
    messages.info(request," Student Logout succesful")
    return redirect('/')

def facultyLogout(request):
    logout(request)
    messages.info(request," Faculty Logout succesful")
    return redirect('/')

def studlogin(request):
    if request.method=='POST':
        usn=request.POST['usn']
        pass1=request.POST['password1']
        user=authenticate(username=usn,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"Student Login Successfull")
            return redirect('/student')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/studlogin')

    return render(request,'studlogin.html')

def facultylogin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass2=request.POST['password2']
        user=authenticate(username=username,password=pass2)
        if user is not None:
            login(request,user)
            messages.info(request,"Faculty Login Successfull")
            return redirect('/faculty')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/facultylogin')

    return render(request,'facultylogin.html')




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
            if User.objects.get(username=usn):
                messages.warning(request,"USN Already Exist")
                return redirect('/signup')
        except Exception as identifier:
            pass
        myuser=User.objects.create_user(usn,email,pass1)
        myusersignup=Signup(usn=usn,name=username,email=email,password=pass1)
        myuserbranch=Branch(branch_name=branch)
        myusersem=Semister(sem=sem)
        myuser.save()
        myusersignup.save()
        myuserbranch.save()
        myusersem.save()
        messages.warning(request,"Signup Successfull, Please Go to Login")
        return redirect('/')

    allBranch=Branch.objects.all()
    allSem=Semister.objects.all()
    context={'allBranch':allBranch,'allSem':allSem}

    return render(request,'signup.html',context)

   
    
