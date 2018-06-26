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


access_token="1002134885618733056-VXe11W6ajSBz9PzaAG4jPSqAsFEoKb"
access_token_secret="kz14W983NwBxGypd529vSQHffi4MARfrDovS0NfJ2clO0"
consumer_key="IL5kOm7MQeY8PmoNQ9lNTgh5R"
consumer_secret="TVnghOQQvJnj5R0pU9GrcZP7lZyx8r4kkmpXlU8m5w8nca8UkA"



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



