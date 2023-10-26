from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=['title','description','Complete']
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User 
        fields=['username','password1','password2']
