from django.db import models
# Create your models here.
class StudentPortal(models.Model):
    user_name=models.CharField(max_length=25)
    user_email=models.EmailField()
    user_pass=models.CharField(max_length=15)

    def __str__(self):
        return self.user_email

class EmployeeDetails(models.Model):
    emp_name=models.CharField(max_length=25)
    emp_user=models.CharField(max_length=8)
    emp_email=models.EmailField()
    emp_pass=models.CharField(max_length=15)
    emp_address=models.TextField()

    def __str__(self):
        return self.emp_name+" - "+self.emp_user