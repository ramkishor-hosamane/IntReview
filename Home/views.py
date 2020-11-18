from django.shortcuts import render

# Create your views here.
def home(request):
    render(request, 'home.html')
    
def signin(request):
    render(request, 'signin.html')
    
def signup(request):
    render(request,'signup.html')