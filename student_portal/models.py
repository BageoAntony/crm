from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    fees = models.PositiveIntegerField()
    duration = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name

class Batches(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_code = models.CharField(max_length=200,unique=True)
    started_data = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.batch_code

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to='images',null=True)
    resume = models.FileField(upload_to='cvs',null=True)
    qualification = models.CharField(max_length=200)
    batch = models.ForeignKey(Batches, on_delete=models.CASCADE)
    phone = models.CharField(max_length=100)


class BatchStudents(models.Model):
    student=models.ForeignKey(Students,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batches,on_delete=models.CASCADE)

    class Meta:
        unique_together=("student","batch")

class Placements(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)