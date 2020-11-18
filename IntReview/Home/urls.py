from django.urls import path
from Home import views

urlpatterns = [
    path('signup', views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('', views.home,name="home"),

]
