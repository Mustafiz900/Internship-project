from django.urls import path
from student import views

urlpatterns = [
   path('',views.index,name="StudentHome"),
   path('student/search',views.search,name="search"),

]
