from django.db import models

# Create your models here.
class Interview_Experience(models.Model):
    user_name = models.CharField(max_length=20)
    profile_pic = models.ImageField(upload_to = "images/newsfeed")
    date = models.DateField() 
    job_title = models.CharField(max_length=20)
    company = models.CharField(max_length=20)
    difficulty = models.CharField(max_length=10)
    experience = models.CharField(max_length=255)
    questions = models.CharField(max_length=255)
