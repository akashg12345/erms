
from email.policy import default

from django.db import models
from django.contrib.auth.models import User


class EmployeeCreate(models.Model):
    FirstName = models.CharField(max_length=100, null=False)
    LastName = models.CharField(max_length=100, null=False)
    Email = models.EmailField(max_length=100, blank=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    Ecode = models.IntegerField()
    Edesignation = models.CharField(max_length=100)
    Econtact = models.IntegerField(null=True)
    BatchName = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    cover = models.FileField(upload_to="records/covers", null=True, blank=True)

    def __str__(self):
        return self.FirstName

    def delete(self, *args, **kwargs):

        self.cover.delete()
        super().delete(*args, **kwargs)

    class Meta:
        db_table = "Employee_RMS1"


class EmployeeEducation1(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PostGraduation = models.CharField(max_length=100, null=True)
    CollegePG = models.CharField(max_length=100, null=True)
    YearOfPassing1 = models.CharField(max_length=100, null=True)
    PGPercentage = models.CharField(max_length=100, null=True)
    Graduation = models.CharField(max_length=100, null=True)
    CollegeGraduation = models.CharField(max_length=100, null=True)
    YearOfPassing2 = models.CharField(max_length=100, null=True)
    GraduationPercentage = models.CharField(max_length=100, null=True)
    CourseHSC = models.CharField(max_length=100, null=True)
    CollegeHSC = models.CharField(max_length=100, null=True)
    YearOfPassing3 = models.CharField(max_length=100, null=True)
    HSCPercentage = models.CharField(max_length=100, null=True)
    CourseSSC = models.CharField(max_length=100, null=True)
    CollegeSSC = models.CharField(max_length=100, null=True)
    YearOfPassing4 = models.CharField(max_length=100, null=True)
    SSCPercentage = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "EmployeeEDU1"


class StudentResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    TestName = models.CharField(max_length=100,null=True)
    TestTopics = models.CharField(max_length=100,null=True)
    TestScore = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "EmployeeExp1"
    
class StudyMaterial(models.Model):
    
    SubjectName = models.CharField(max_length=100,null=True)
    SubjectTopics = models.CharField(max_length=100,null=True)
    Material = models.FileField(upload_to="records/material", null=True, blank=True)
    class Meta:
        db_table = "StudyMaterial"
class TestResults(models.Model):
    TestName = models.CharField(max_length=100,null=True)
    TestTopics = models.CharField(max_length=100,null=True)
    Material = models.FileField(upload_to="records/results", null=True, blank=True)
    class Meta:
        db_table = "TestResults"