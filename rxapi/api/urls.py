from django.urls import path
from . import views
urlpatterns = [
    path("greet/", views.hello),
    path("getTweets/<str:category>", views.getRecentTweets),
    path("getTwitterUser/<str:id>", views.getTwitterUser),
    path("newUser/", views.storeUser),
    path("getUser/<str:username>", views.getUserDetails),
    path("updateUser/", views.updateUser),
    path("getTwitterSentiments/<str:category>", views.getSentimentResponse),

    path("getLeaderboard/", views.getLeaderboard),

    path("getUsers/<str:category>", views.getUsers),

    path("sendTweet/<int:id>", views.sendTweet)
]