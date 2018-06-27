#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tweepy
import MySQLdb
import sys
from bs4 import BeautifulSoup
import requests
import os, os.path,csv




access_token=""
access_token_secret=""
consumer_key=""
consumer_secret=""



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


connection =  MySQLdb.connect(host= ",
    user="",
    passwd="",
    db="")
cursor = connection.cursor()

# The table schema: CREATE TABLE tweets (id INT PRIMARY KEY AUTO_INCREMENT, tweet_id BIGINT NOT NULL, tweet_text VARCHAR(160) NOT NULL, screen_name VARCHAR(160) NOT NULL, author_id BIGINT, created_at DATETIME NOT NULL, inserted_at DATETIME NOT NULL)


class TwitterStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        try:
            cursor.execute("INSERT INTO tweets (tweet_id, tweet_text, screen_name, author_id, created_at, inserted_at) VALUES (%s, %s, %s, %s, %s, NOW());", (status.id, status.text, status.author.screen_name, status.author.id, status.created_at))
            connection.commit()
        except:
            pass

    def on_error(self, status_code):
        
        if status_code == 420:
            return False 
try:
    streamListener = TwitterStreamListener()
    twitterStream = tweepy.Stream(auth = api.auth, listener=streamListener)
    

    list="http://tweeplers.com/hashtags/?cc=IN"
    response=requests.get(list)

    soup=BeautifulSoup(response.text, "html.parser")
    listings=[]

    rows = soup.findAll("div", {"class":"col-xs-8 wordwrap"})

    for i in range(5):
        listings.append(rows[i].find('a').text)  
        for ll in listings:
            twitterStream.filter(track=[ll])


except tweepy.error.TweepError:
    print "Whoops, something went terribly wrong!"
except UnicodeEncodeError:
    pass
except:
    print "Unexpected error: ", sys.exc_info()[0]
    raise
finally:
    cursor.close()
connection.close()
