from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentMarks
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'student/index.html')

def search(request):
    query=request.GET['search']
    if len(query)>80:
        allPosts= StudentMarks.objects.none()
    else:
        allPostsusn=StudentMarks.objects.filter(usn__icontains=query)
        allPostsname=StudentMarks.objects.filter(name__icontains=query)
        allPosts=allPostsusn.union(allPostsname)

    if allPosts.count()==0:
        return HttpResponse("No search results found")
    params={'allPosts':allPosts,'query':query} 

    return render(request,'student/search.html',params)

def aboutus(request):
    return render(request,'student/aboutus.html')

def viewmarks(request):
    return render(request,'student/studentviewmarks1.html')

def contactus(request):
    return render(request,'student/contactus.html')
