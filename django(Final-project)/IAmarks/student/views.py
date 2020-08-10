from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Contact,CseTopper,IseTopper,EceTopper,MechTopper,CivilTopper,Branch,Semister,Signup
from faculty.models import Marks,Subject
from django.contrib import messages
from django.conf import settings

# Create your views here.
def index(request):
    # if not request.user.is_authenticated:
    #     return render(request,'index.html')
    return render(request,'student/index.html')

def search(request): 
    return render(request,'student/search.html')

def aboutus(request):
    return render(request,'student/aboutus.html')

def viewmarks(request):
   
    return render(request,'student/studentviewmarks1.html')

def viewmarks2(request):
    query=request.GET['search']
    if len(query)>30:
        allPosts=Marks.objects.none()
    else:
        allPostsusn=Marks.objects.filter(usn__icontains=query)
        # allPostsname=Marks.objects.filter(name__icontains=query)
        allPosts=allPostsusn
        allSub=Subject.objects.all()
    
    if allPosts.count()==0:
        messages.error(request,"Search result not found")

    params={'allPosts':allPosts,'query':query,'allSub':allSub} 

    return render(request,'student/studviewmarks2.html',params)


def csetoppers(request):
    posts=CseTopper.objects.all()
    context={'posts':posts}
    return render(request,'student/csetoppers.html',context)

def isetoppers(request):
    posts=IseTopper.objects.all()
    context={'posts':posts}
    return render(request,'student/isetoppers.html',context)

def ecetoppers(request):
    posts=EceTopper.objects.all()
    context={'posts':posts}
    return render(request,'student/ecetoppers.html',context)

def mechtoppers(request):
    posts=MechTopper.objects.all()
    context={'posts':posts}
    return render(request,'student/mechtoppers.html',context)

def civiltoppers(request):
    posts=CivilTopper.objects.all()
    context={'posts':posts}
    return render(request,'student/civiltoppers.html',context)


def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        if len(phone)<10:
            messages.error(request,"Phone number invalid")
            return render(request,'student/contactus.html')
        
        if len(desc)<5:
            messages.error(request,"Provide valid description")
            return render(request,'student/contactus.html')

        myusercontact=Contact(name=name,email=email,phone=phone,desc=desc)
        myusercontact.save()
        messages.warning(request,"Your Response has been recorded")
        return redirect('/student')


    return render(request,'student/contactus.html')
