# from django.db import models
from  django.db import  models
from django.contrib.auth.models import User
# Create your views here.
class profile1(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=20)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

# class project(models.Model):
#     project_title=models.CharField(max_length=10)

from django.db import models

# class Project(models.Model):
#     project_title = models.CharField(max_length=100)

class project_model(models.Model):
    project_title=models.CharField(max_length=10)


from django.db import models

class Todo(models.Model):
    project_title = models.CharField(max_length=100)
    todo_name = models.CharField(max_length=100)
    todo_description = models.TextField()
    created_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ])
