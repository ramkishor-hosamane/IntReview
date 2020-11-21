from django.urls import path
from NewsFeed import views
urlpatterns = [

    path('/<str:username>',views.Newsfeed.as_view()),
    #path('newsfeed/<username>', views.Newsfeed.as_view()),

]
