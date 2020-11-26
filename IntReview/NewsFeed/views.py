from django.shortcuts import render
from django.views import View
from .forms import Interview_Experience_Form
# Create your views here.


#Routing for Newsfeed
class Newsfeed(View):    
    def get(self,request,username):
        context={"user_name":username}
        return render(request, 'newsfeed.html',context=context)

class Get_experience(View):

    def get(self,request):
        experience_form = Interview_Experience_Form()

        context={"experience_form":experience_form}
        
        return render(request, 'get_experience.html',context=context)
            
    def post(self,request):
        experience_form = Interview_Experience_Form()

        context={"experience_form":experience_form}

        print(request.POST)
        e = Interview_Experience_Form(request.POST)
        if e.is_valid():
            e.save()

        return render(request, 'get_experience.html',context=context)
    