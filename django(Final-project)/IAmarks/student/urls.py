from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name="Student"),
   path('search',views.search,name="search"),
   path('aboutus',views.aboutus,name="aboutus"),
   path('contactus',views.contactus,name="contactus"),
   path('viewmarks',views.viewmarks,name="viewmarks"),
   path('viewmarks2',views.viewmarks2,name="viewmarks2"),
   path('csetoppers',views.csetoppers,name="csetoppers"),
   path('isetoppers',views.isetoppers,name="isetoppers"),
   path('ecetoppers',views.ecetoppers,name="ecetoppers"),
   path('mechtoppers',views.mechtoppers,name="mechtoppers"),
   path('civiltoppers',views.civiltoppers,name="civiltoppers"),
   

]
