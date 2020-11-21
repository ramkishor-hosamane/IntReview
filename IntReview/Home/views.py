from django.shortcuts import render
from django.views import View
# Create your views here.


#Routing for Home
def home(request):
    return render(request, 'home.html')


#Routing for Signup
class Signup(View):    
    def get(self,request):
        return render(request,'signup.html')
    
    
    def post(self,request):
        
        user_name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        #Profile picture is not done yet
        #profile_pic = request.POST.get('profile_pic')
        phone_number = request.POST.get('phone_number')
        

        print(user_name,password,email,phone_number)
        ''' 
            Over to you Akanksha 
            All the best !!!!!!!

        '''

        return render(request,'signup.html')




#Routing for Signin
class Signin(View):    
    def get(self,request):
        return render(request, 'signin.html')
