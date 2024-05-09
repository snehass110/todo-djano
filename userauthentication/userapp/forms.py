from  django import forms
from  .models import *

# class project_frms.CharField(max_length=20)
# forms.py
from django import forms


# class ProjectForm(forms.ModelForm):
#     class Meta:
#         model = Project
#         fields = ['project_title']  # Add more fields here if needed
from django import forms

class project_form(forms.Form):
    project_title=forms.CharField(max_length=10)

# forms.py
from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['project_title', 'todo_name', 'todo_description', 'created_time', 'status']
