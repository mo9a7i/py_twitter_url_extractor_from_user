#!/usr/bin/env python
# -*- coding: utf-8 -*-
# using https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file
# and https://stackoverflow.com/questions/42013072/extracting-external-links-from-tweets-in-python

import sys, re, urllib, json
#http://www.tweepy.org/
import tweepy
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

#Get your Twitter API credentials and enter them here
consumer_key = "aBNNwJW3w0Ud7FpJgxTDzmyqG"
consumer_secret = "rsKsXFaraMu6Pqy42jrhg5rDNLL1SC0XvjFCQt5mzusROwA6nW"
access_key = "209559725-uEKBipnD1XUfDU1X1c9U5wHK4Ott2BtD7bh2AN9T"
access_secret = "01xpTueWRlQi0qYfctA7d9BH5R4VVBy3neuZxfygpF7Vx" 

#method to get a user's last  200 tweets
def get_tweets(username):

    #http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #set count to however many tweets you want; twitter only allows 200 at once
    number_of_tweets = 5

    #get tweets
    tweets = api.user_timeline(screen_name = username,  count = number_of_tweets)
   
    for tweet in tweets:
        try:
            print(tweet._json)
        except NameError:
            print("well, it WASN'T defined after all!")


        # urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text)
        

        
        # for url in urls:
        #     try:
        #         res = urllib.urlopen(url)
        #         actual_url = res.geturl()
        #         print("printing actual: " + actual_url)
        #     except:
        #         print("printing URL: " + url)


#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print("Error: enter one username")

    #alternative method: loop through multiple users
        # users = ['user1','user2']

        # for user in users:
#       get_tweets(user)


