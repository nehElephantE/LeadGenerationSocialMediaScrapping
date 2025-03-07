from django.http import HttpResponse, JsonResponse
from django.http import JsonResponse
from django.shortcuts import HttpResponse
import requests
import datetime
import pyrebase
from django.views.decorators.csrf import csrf_exempt
import json
# from .reactor import getSentiments

import tweepy
import pandas as pd

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

# HelperFunctions
def getSentiments(dataList):
    answers = []
    for data in dataList:
        analysis=TextBlob(data['text'])
        obj = SentimentIntensityAnalyzer()
        sentiment_dict = obj.polarity_scores(data['text'])
        if sentiment_dict['compound'] > 0.3:
            sentiment_dict['sentiment'] = "possitive"
        elif sentiment_dict['compound'] < -0.3:
            sentiment_dict['sentiment'] = "negative"
        else:
            sentiment_dict['sentiment'] = "neutral"
        sentiment_dict['author_id'] = data['author_id']
        answers.append(sentiment_dict)
    return answers
# Create your views here.

firebaseConfig = {
  "apiKey": "API_KEY",
  "authDomain": "metadata-ee971.firebaseapp.com",
  "projectId": "metadata-ee971",
  "storageBucket": "metadata-ee971.appspot.com",
  "messagingSenderId": "101391171303",
  "appId": "1:101391171303:web:5f19fe2751468318d36c42",
  "measurementId": "G-HEDT1PEHML",
  "databaseURL": "https://metadata-ee971-default-rtdb.firebaseio.com"
}

firebase = pyrebase.initialize_app(firebaseConfig)
database = firebase.database()
headers = {'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAIxHdwEAAAAAA52WV4lx1pZPwETXdIDT8cRn40E%3DEgHRwDtdezUZ3svok8RdhDzHxZw8JMsYzgl4UPHae4Lx50krzj' }
def hello(request):
    return HttpResponse("hello world");


# ---------------------------------------------------------------------------- #
#                                  Twitter API                                 #
# ---------------------------------------------------------------------------- #

def getRecentTweets(request, category):
    current = datetime.datetime.utcnow()
    span = datetime.timedelta(minutes=5)
    recent = current - span
    # print();
    payload = {
        'query': str(category), 
        'max_results': 50, 
        'start_time': recent.strftime('%Y-%m-%dT%H:%M:%S.000Z'),
        "expansions": "author_id",
        'user.fields': 'name,username,public_metrics'
    }
    tweets = requests.get("https://api.twitter.com/2/tweets/search/recent", headers=headers, params=payload)
    # print(tweets)
    database.child("twitter").child(str(recent.strftime("%H%m%S%d%m%y"))).set(tweets.json())
    data = tweets.json()["data"]
    # print(tweets.json())
    # text_data = []
    # for i in range(len(data)):
    #     text = data[i]["text"]
    #     text_data.append(text)
    return JsonResponse(tweets.json(), safe=False)


def getTwitterUser(request, id):
    payload = {
        "expansions": "author_id",
        "user.fields": "created_at,description,entities,id,location,name,profile_image_url,protected,public_metrics,url,username"
    }
    user = requests.get("https://api.twitter.com/2/tweets/"+id, params=payload, headers=headers)
    return JsonResponse(user.json()['includes']['users'][0], safe=False)


def sendTweet(request, id):
    consumer_key = 'nwU1wkyAOrnr4c7D3HnIIoMmC'
    consumer_secret = 'ECftUMGtv5EvtMwz0mtUq0i73cffesUl4vuQ3ZTzBdP3KwXUBt'
    access_token = '1540737761266659330-1NymUA5LtWexlcv1IwiliEpvnsPKxf'
    access_token_secret = 'g69M0lOzmt9p6o6fIaHdkZax4PhclWxRrn2Ulv81z0zrs'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit = True)

    def profile_image(filename):
        api.update_profile_image(filename)

    #profile_image("D:\HACK_RX\ht.jpg")
    # def update_profile_info(name, url, location, description):
    #     api.update_profile(name, url, location, description)

    #recipient_id ="AbhayAr14780082"
    recipient_id=int(id)


    # text to be sent
    text = "Hello!, We would like to invite you to our website! www.bajajallianz.com"

    # sending the direct message
    direct_message = api.send_direct_message(recipient_id, text)

    # printing the text of the sent direct message
    print(direct_message.message_create['message_data']['text'])
    return JsonResponse({"status": "success"})

# ---------------------------------------------------------------------------- #
#                                   User apis                                  #
# ---------------------------------------------------------------------------- #
@csrf_exempt
def storeUser(request):
    if request.method == "POST":
        data = json.loads(request.body);
        # print(data)
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        # age = data.get("age")
        favourites = data.get("interests")
        # social_instagram = data.get("instagram")
        social_twitter = data.get("twitter")
        # social_whatsapp = data.get("whatsapp")
        email = data.get("email")
        reward = 0
        if(email != ""):
            reward+= 200
        if(social_twitter != ""):
            reward+= 300
        print({
            "username": first_name+last_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            # "age": age,
            "favourites": favourites,
            "reward_points": 0,
            # "social_instagram": social_instagram,
            "social_twitter": social_twitter,
            # "social_whatsapp": social_whatsapp,
        })
        database.child("users").child(first_name+last_name).set({
            "username": first_name+last_name,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            # "age": age,
            "favourites": favourites,
            # "social_instagram": social_instagram,
            "social_twitter": social_twitter,
            "reward": reward
            # "social_whatsapp": social_whatsapp,
        })
        return JsonResponse({
            "status": "success",
        })
    return JsonResponse({
        "status": "error",
        "message": "Some error occured"
    })

@csrf_exempt
def getUserDetails(request,username):
    if request.method == "GET":
        user = database.child("users").child(username).get()
        return JsonResponse(user.val(), safe=False)


@csrf_exempt
def updateUser(request):
    if request.method == "POST":
        data = json.loads(request.body)
        updates = {}
        for key, value in data.items():
            updates[key] = value
        database.child("users").child(data.get("username")).update(updates)
        return JsonResponse({
            "status": "success"
        })



# ---------------------------------------------------------------------------- #
#                               Scheduling a call                              #
# ---------------------------------------------------------------------------- #

def scheduleCall(request):
    if request.method == "POST":
        data = json.loads(request.body);
        requester = data.get("requester")
        timing = data.get("timing")
        approver = data.get("approver")
        message = data.get("message")
        database.child("schedules").child(requester).child(timing).set({
            "requester": requester,
            "approver": approver,
            "timing": timing,
            "message": message,
            "status": "wait"
        })
        return JsonResponse({
            'status' : "success"
        })

def approveCall(request):
    if request.method == "POST":
        data = json.loads(request.body);
        requester = data.get("requester")
        timing = data.get("timing")
        database.child("schedules").child(requester).child(timing).update({
            "status" : "approved"
        })
        return JsonResponse({
            'status' : "success"
        })

def denyCall(request):
    if request.method == "POST":
        data = json.loads(request.body);
        requester = data.get("requester")
        timing = data.get("timing")
        database.child("schedules").child(requester).child(timing).update({
            "status" : "denied",
            "message": "Your call request has been denied."
        })
        return JsonResponse({
            'status' : "success"
        })

def updateCallDetails(request):
    if request.method == "POST":
        data = json.loads(request.body);
        requester = data.get("requester")
        timing = data.get("timing")
        database.child("schedules").child(requester).child(timing).update({
            "status" : "denied",
            "message": "Your call request has been denied."
        })
        return JsonResponse({
            'status' : "success"
        })

def notificationTrigger(request):
    pass

def cancelCall(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        requester = data.get("requester")
        timing = data.get("timing")
        database.child(requester).child(timing).remove()
        return JsonResponse({
            'status' : "success"
        })


# ---------------------------------------------------------------------------- #
#                                    Groups                                    #
# ---------------------------------------------------------------------------- #

def createGroup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        description = data.get("desc")
        username = data.get("username")
        database.child("groups").child(name).set({
            "name": name,
            "description": description,
            "created_on" : datetime.datetime.utcnow(),
            "admin": username
        })
        database.child("groups").child(name).child("members").child("username").set({
            "username": username,
            "joined_on": datetime.datetime.utcnow(),
        })
        database.child("users").child(username).child("groups").child(name).set({
            "name": name,
            "chatlink": ""
        })
        return JsonResponse({
            "status": "success"
        })

def deleteGroup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get("username")
        name = data.get("name")
        if database.child("groups").child(name).get().val()['admin'] == username:
            database.child("groups").child(name).remove()
            return JsonResponse({
                "status": "success"
            })

def modifyDescription(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        description = data.get("desc")
        database.child("groups").child(name).update({
            "description": description
        })

def addMember(request):
    if request.method == "POST":
        data = json.loads(request.body)
    
def removeMember(request):
    if request.method == "POST":
        data = json.loads(request.body)

def getTotalMembers(request):
    if request.method == "POST":
        data = json.loads(request.body)


# ---------------------------------------------------------------------------- #
#                                public post api                               #
# ---------------------------------------------------------------------------- #
 
 # ---------------------------------------------------------------------------- #
 #                              Sentiment Analysis                              #
 # ----------------------------------------------------------------------------
def getSentimentResponse(request, category):
    url = "http://localhost:8000/api/getTweets/"+category
    response = requests.get(url)
    data = response.json()
    # sentiments = getSentiments(data['data'])
    # print(sentiments)
    # print(data)
    return JsonResponse({"data":getSentiments(data['data']),
    "users": data['includes']['users']}, safe=False)


# ---------------------------------------------------------------------------- #
#                                 Reward System                                #
# ---------------------------------------------------------------------------- #
def getLeaderboard(request):
    top10 = database.child("users").get()
    toppersList = []
    for member in top10:
        toppersList.append(member.val())
    toppersList = sorted(toppersList, key=lambda x: x["reward"], reverse=True)
    return JsonResponse({
        "status": "success",
        "data": toppersList
    })

def getUsers(request, category):
    members = database.child("users").get()
    leads = []
    for member in members:
        data = member.val()
        print(data)
        for interest in data["favourites"]:
            if interest in category:
                leads.append(data)
    return JsonResponse({
        "status": "success",
        "data": leads
    }, safe=False)
