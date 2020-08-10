from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages
from student.models import Contact,Signup,Branch,Semister
from .models import Subject,Marks

# Create your views here.
def index(request):
    return render(request,"faculty/index.html")

def viewmarks(request):
    return render(request,"faculty/view1.html")

def view2(request):
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

    return render(request,"faculty/view2.html",params)

# def facultyview(request):
#     return render(request,"faculty/facultyviewmarks.html")

# def view3(request):
#     return render(request,"faculty/view3.html")

def entermarks(request):
    if request.method=='POST':
        usn=request.POST['usn']
        branch=request.POST['branch']
        sem=request.POST['sem']
        internal=request.POST['internal']
        sub_1=request.POST['sub_1']
        sub_2=request.POST['sub_2']
        sub_3=request.POST['sub_3']
        sub_4=request.POST['sub_4']
        sub_5=request.POST['sub_5']
        sub_6=request.POST['sub_6']
        sub_7=request.POST['sub_7']
        sub_8=request.POST['sub_8']

        myuserMarks=Marks(usn=usn,branch=branch,sem=sem,internal=internal,sub1_marks=sub_1,sub2_marks=sub_2,sub3_marks=sub_3,sub4_marks=sub_4,sub5_marks=sub_5,sub6_marks=sub_6,sub7_marks=sub_7,sub8_marks=sub_8)
        myuserMarks.save()
        messages.warning(request,"Marks Entered Successfully")
        return redirect('entermarks')
        

    allBranch=Branch.objects.all()
    allSem=Semister.objects.all()
    context={'allBranch':allBranch,'allSem':allSem}
    return render(request,"faculty/entermarks.html",context)