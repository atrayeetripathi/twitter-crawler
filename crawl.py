#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import tweepy
from bs4 import BeautifulSoup
import requests
import os, os.path,csv


access_token=""
access_token_secret="
consumer_key=""
consumer_secret=""



class StdoutListener(StreamListener):
    def on_data(self,data):
        try:
            print(data)
            savefile=open("twitterfinal.txt","a")
            savefile.write(data)
            savefile.write('\n')
            savefile.close()
            return true
        except BaseException as e:
            print ("done")
            time.s    def on_error(self,status):
                print(status)

if __name__=="__main__":


    l=StdoutListener()
    auth=OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    stream=Stream(auth,l)


    list="http://tweeplers.com/hashtags/?cc=IN"
    response=requests.get(list)

    soup=BeautifulSoup(response.text, "html.parser")
    listings=[]

    rows = soup.findAll("div", {"class":"col-xs-8 wordwrap"})

    for i in range(5):
        listings.append(rows[i].find('a').text)
        for ll in listings:
            stream.filter(track=[ll])



