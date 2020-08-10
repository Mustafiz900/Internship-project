from django.urls import path
from .import views

urlpatterns = [
   path('',views.index,name="FacultyHome"),
   path('viewmarks',views.viewmarks,name="viewmarks"),
   path('view2',views.view2,name="view2"),
   # path('facultyview',views.facultyview,name="facultyview"),
   # path('view3',views.view3,name="view3"),
   path('entermarks',views.entermarks,name="entermarks")

]
