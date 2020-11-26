from django.urls import path
from NewsFeed import views
urlpatterns = [

    path('get_experience', views.Get_experience.as_view(),name="get_experience"),

    path('<str:username>',views.Newsfeed.as_view()),

]
