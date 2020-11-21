from django.urls import path
from NewsFeed import views
urlpatterns = [

    path('',views.Newsfeed.as_view(),name="newsfeed"),
    #path('', views.home,name="home"),

]
