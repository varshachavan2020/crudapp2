from django.db import models

# Create your models here.

StudentChoice=(('Mechanical Engineering','Mechanical Engineering'),
('Information Technology','Information Technology'),('ElectricalEngineering','Electrical Engineering'),
('Computer Science&Engineering','Computer Science&Engineering'),('Civel Engineering','Civel Engineering'),
('Electronic & telecommunication Engineering','Electronic & telecommunication Engineering')
)
class Student(models.Model):
    no=models.IntegerField(blank=False,null=True,unique=True)
    name=models.CharField(max_length=100,blank=False,null=True)
    age=models.IntegerField(blank=False,null=True)
    address=models.CharField(max_length=100,blank=False,null=True)
    contactno=models.IntegerField(blank=False,null=True)
    date = models.DateField(null=True,blank=False)
    department=models.CharField(choices=StudentChoice,max_length=50,blank=False,null=True)
