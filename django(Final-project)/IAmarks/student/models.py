from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.IntegerField()
    desc=models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Signup(models.Model):
    usn=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=10)

    def __str__(self):
        return self.usn
    
class Branch(models.Model):
    branch_id=models.AutoField(primary_key=True)
    branch_name=models.CharField(max_length=20)

    def __str__(self):
        return self.branch_name

class Semister(models.Model):
    sem_id=models.AutoField(primary_key=True)
    sem=models.CharField(max_length=10)

    def __str__(self):
        return self.sem

class CseTopper(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    sem=models.CharField(max_length=10)
    Internal=models.IntegerField()
    percentage=models.DecimalField(max_digits=6,decimal_places=3)
    img=models.ImageField(upload_to='toppersspic',blank=True,null=True)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

class IseTopper(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    sem=models.CharField(max_length=10)
    Internal=models.IntegerField()
    percentage=models.DecimalField(max_digits=6,decimal_places=3)
    img=models.ImageField(upload_to='toppersspic',blank=True,null=True)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

class EceTopper(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    sem=models.CharField(max_length=10)
    Internal=models.IntegerField()
    percentage=models.DecimalField(max_digits=6,decimal_places=3)
    img=models.ImageField(upload_to='toppersspic',blank=True,null=True)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

class MechTopper(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    sem=models.CharField(max_length=10)
    Internal=models.IntegerField()
    percentage=models.DecimalField(max_digits=6,decimal_places=3)
    img=models.ImageField(upload_to='toppersspic',blank=True,null=True)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.name

class CivilTopper(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    sem=models.CharField(max_length=10)
    Internal=models.IntegerField()
    percentage=models.DecimalField(max_digits=6,decimal_places=3)
    img=models.ImageField(upload_to='toppersspic',blank=True,null=True)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.name
            