
from django import forms 
from .models import Interview_Experience  
class Interview_Experience_Form(forms.Form): 
    name = forms.CharField() 
    geeks_field = forms.ImageField() 
    model = Interview_Experience
    fields = ['user_name', 'profile_pic', 'date', 'job_title',
              'company', 'difficulty', 'experience', 'questions']
              