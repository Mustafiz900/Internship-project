from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,"faculty/index.html")

def viewmarks(request):
    return render(request,"faculty/view1.html")

def view2(request):
    return render(request,"faculty/view2.html")

def facultyview(request):
    return render(request,"faculty/facultyviewmarks.html")

def view3(request):
    return render(request,"faculty/view3.html")

def entermarks(request):
    return render(request,"faculty/entermarks.html")