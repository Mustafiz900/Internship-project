from django.contrib import admin
from .models import Contact,Signup,Branch,Semister,CseTopper,IseTopper,EceTopper,MechTopper,CivilTopper

# Register your models here.
admin.site.register(Contact)
admin.site.register(Signup)
admin.site.register(Branch)
admin.site.register(Semister)
admin.site.register(CseTopper)
admin.site.register(IseTopper)
admin.site.register(EceTopper)
admin.site.register(MechTopper)
admin.site.register(CivilTopper)