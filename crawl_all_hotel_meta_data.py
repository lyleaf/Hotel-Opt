# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 10:38:46 2016

@author: liuy
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

Store all reviews of hotel at the link of url into Reviews.csv
"""
import time
from bs4 import BeautifulSoup
import codecs
import requests
from lxml import html
from lxml import etree
#url = "https://www.tripadvisor.com/Hotel_Review-g1584858-d1461983-Reviews-Ghonday_Village_Resort-West_Sikkim_Sikkim.html"

headers = {'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5); lyleaf@gmail.com'}
with open ('links2','r') as f:
    links = f.readlines()

f = codecs.open("TripAdvisorMeta.csv", 'a+', 'utf-8')

for url in links:
    response = requests.get(url,headers = headers)
    tree = html.fromstring(response.content)
    soup = BeautifulSoup(response.content)


    TRIPADVISORID1 = url.split("-")[1]
    TRIPADVISORID2 = url.split("-")[2]
    try:
        ZIP_CODE = soup.find_all("span",{"property":"postalCode"})[0].text
    except:
        ZIP_CODE = ""

    try:   
        PROPERTY_NAME = soup.find_all("span",{"property":"postalCode"})[0].text
    except:
        PROPERTY_NAME = ""

    try:   
        CITY2 = soup.find_all("span",{"property":"addressLocality"})[0].text
    except:
        CITY2 = ""
    
    try:   
        REGION = soup.find_all("span",{"property":"addressRegion"})[0].text
    except:
        REGION = ""
    
    try:   
        COUNTRY_NAME =soup.find_all("span",{"property":"addressCountry","class":"country-name"})[0].text
    except:
        COUNTRY_NAME = ""
    
    try:   
        ADDRESS_LINE_1 = soup.find_all("span",{"property":"streetAddress","class":"street-address"})[0].text
    except:
        ADDRESS_LINE_1 = ""
    
  
    try:
        comment = soup.find_all("div",{"class":"fl contact_item"})[-1].script.string
        after_var = comment.split("var a,b,c")[1]
        before_document_write = after_var.split("document.write")[0] 
        exec (before_document_write + """\nPHONE = a+c+b""")
    except:
        PHONE = ""

    f.write(TRIPADVISORID1 +  "*" + TRIPADVISORID2 + "*" + PROPERTY_NAME + "*" + COUNTRY_NAME + "*" + CITY2 + "*" + REGION + "*" + ZIP_CODE + "*" + ADDRESS_LINE_1 + "*" + PHONE + "\n")
    time.sleep(3)


f.close()
