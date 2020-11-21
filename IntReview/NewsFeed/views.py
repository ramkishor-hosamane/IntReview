from django.shortcuts import render
from django.views import View
# Create your views here.


#Routing for Newsfeed
class Newsfeed(View):    
    def get(self,request,username):
        context={"user_name":username}
        return render(request, 'newsfeed.html',context=context)
