# -*- coding: utf-8 -*-
"""Findom.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ALc8WwCS5fDYCoxmcfQ6_G1hk-nB0cPG
"""

pip install git+https://github.com/tweepy/tweepy.git

!pip install tweepy

import tweepy

tweepy.__version__

CONSUMER_KEY = "Rg7g7mmyae2yZfG6Ch6g91dAN"
CONSUMER_SECRET = "PcQzF7Df7c8Q8wZtVCX3l5xJOA21qqgT9dqTSBUJ50MYsoMmBj"
#Bearer_token = "AAAAAAAAAAAAAAAAAAAAABjfFwEAAAAAZxzAtRTUbK9g1K6a%2BWFTU2kdcxA%3DlYZhCtrFdPICkaodXE0wovYnH0mOgJT60xe135c8eLvF5glTCn"
Access_Token = "1282557457445859329-tKUyAmEJW0E7WaTaCafmw2QKKYcY7i"
Access_Token_secret = "KYYtG2qnqzthY6GQfr2sJwqGfre24Rs8HxrFVlauzUYJv"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(Access_Token, Access_Token_secret)
#auth.set_access_token(user.acc_token,user.acc_secret)
api = tweepy.API(auth)

abc = api.search(q='#findom',lang="en", count = 45)
len(abc)

abc[0].__dict__.keys()

abc[0].__dict__

abc[0].__dict__.keys()

def get_tweets(query, count = 1000):

    # empty list to store parsed tweets
    tweets = []
    target = io.open("mytweets2.txt", 'w', encoding='utf-8')
    # call twitter api to fetch tweets
    q=str(query)
    a=str(q+" findom")
    b=str(q+" #findom")
    c=str(q+" Findom")
    fetched_tweets = api.search(a, count = count)+ api.search(b, count = count)+ api.search(c, count = count)
    # parsing tweets one by one
    print(len(fetched_tweets))

    for tweet in fetched_tweets:

        # empty dictionary to store required params of a tweet
        parsed_tweet = {}
        # saving text of tweet
        parsed_tweet['text'] = tweet.text
        if "http" not in tweet.text:
            line = re.sub("[^A-Za-z]", " ", tweet.text)
            target.write(line+"\n")
    return tweets

    # creating object of TwitterClient Class
    # calling function to get tweets
tweets = get_tweets(query ="", count = 20000)

import re
import io
import csv
import tweepy
from tweepy import OAuthHandler

tweets = tweepy.Cursor(api.search,
              q='Findom',
              lang="en", count = '6').items(10)
tweets
#len(tweets)

bc

api.send_direct_message(1166721132717756418, 'Hi')

for i in id:
  message = i
  api.send_direct_message(recipient_id=message,text='I am Bot')
  print(message)

api.send_direct_message()

id

author_s

u = api.get_user(493768969)
print(u.screen_name)

data_s = []
author_s = []
id = []
bc = 0
for tweet in tweets:
  data_s.append(tweet.text)
  author_s.append(tweet.author.screen_name)
  id.append(tweet.author.id)
  print(tweet.text)
  print(tweet.author.id)
  #a1 = tweet.created_at
  a2 = tweet.metadata
    #a3 = tweet.author
  bc += 1



abc

for i in abc:
  print(i.__dict__)

abc[1].__dict__.keys()

abc[1].metadata

abc[1].text

abc[1].__dict__

!pip install searchtweets



u = api.get_user(1464224159857319975)
print(u.screen_name)

abc[0].__dict__.keys()

for i in abc:
  print(i.__dict__.keys())

import pandas as pd
import numpy as np

lol = []
for i in tweets:
  lol.append(i)

lol = [tweets]
lol

lol1

tweets

lol1 = []
for i in abc:
  tweets = i.text
  lol1.append(tweets)

  print(tweets)

abc[1].author

abc[1].author.screen_name

pruth = pd.DataFrame(data = lol1)
pruth
