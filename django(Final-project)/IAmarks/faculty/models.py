from django.db import models

# Create your models here.
class Subject(models.Model):
    sub_id=models.AutoField(primary_key=True)
    sub1=models.CharField(max_length=50)
    sub2=models.CharField(max_length=50)
    sub3=models.CharField(max_length=50)
    sub4=models.CharField(max_length=50)
    sub5=models.CharField(max_length=50)
    sub6=models.CharField(max_length=50)
    sub7=models.CharField(max_length=50)
    sub8=models.CharField(max_length=50)

    def __str__(self):
        return self.sub1
    
class Marks(models.Model):
    usn=models.CharField(max_length=12)
    branch=models.CharField(max_length=20)
    sem=models.CharField(max_length=10)
    internal=models.IntegerField()
    sub1_marks=models.IntegerField()
    sub2_marks=models.IntegerField()
    sub3_marks=models.IntegerField()
    sub4_marks=models.IntegerField()
    sub5_marks=models.IntegerField()
    sub6_marks=models.IntegerField()
    sub7_marks=models.IntegerField()
    sub8_marks=models.IntegerField()

    def __str__(self):
        return self.usn
    