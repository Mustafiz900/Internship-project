from django.db import models

# Create your models here.
class StudentMarks(models.Model):
    usn=models.CharField(max_length=12,primary_key=True)
    name=models.CharField(max_length=50)
    subject=models.CharField(max_length=25)
    marks=models.IntegerField()
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.name