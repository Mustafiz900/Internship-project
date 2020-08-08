from django.urls import path
from student import views

urlpatterns = [
   path('',views.index,name="Student"),
   path('search',views.search,name="search"),
   path('aboutus',views.aboutus,name="aboutus"),
   path('contactus',views.contactus,name="contactus"),
   path('viewmarks',views.viewmarks,name="viewmarks"),

]
