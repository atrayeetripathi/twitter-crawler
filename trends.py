from bs4 import BeautifulSoup
import requests
import os, os.path,csv

list="http://tweeplers.com/hashtags/?cc=IN"
response=requests.get(list)

soup=BeautifulSoup(response.text, "html.parser")
listings=[]

rows = soup.findAll("div", {"class":"col-xs-8 wordwrap"})

for i in range(5):
    print(rows[i].find('a').text)
