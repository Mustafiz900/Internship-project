from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentMarks

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