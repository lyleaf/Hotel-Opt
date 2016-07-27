# -*- coding: utf-8 -*-
"""
Spyder Editor

Store all reviews of hotel at the link of url into Reviews.csv
"""
import codecs
import requests
from lxml import html
from lxml import etree

TRIP_ADVISER = "https://www.tripadvisor.com/"
url = "https://www.tripadvisor.com/Hotel_Review-g187234-d289384-Reviews-Hyatt_Regency_Nice_Palais_de_la_Mediterranee-Nice_French_Riviera_Cote_d_Azur_Provence.html"

response = requests.get(url)
tree = html.fromstring(response.content)
#review = tree.xpath('//*[@id="rn392764024"]')[0].get('href')
#//*[@id="rn392764024"][0]
num_pages = int(tree.xpath('//*[@id="REVIEWS"]/div[16]/div/div/a[6]')[0].text)

f = codecs.open("Reviews.csv", 'w', 'utf-8')
for j in xrange(1, num_pages+1):
    for i in xrange(6,16):
     #   i = 9
        try:
            review_id = tree.xpath('//*[@id="REVIEWS"]/div[%d]' % i)[0].get('id')[7:]
            #print review_id
            review_link = tree.xpath('//*[@id="rn%s"]' % review_id)[0].get('href')#//*[@id="rn392764024"]
           #//*[@id="rn392764024"]
            review_link = TRIP_ADVISER + review_link
            #print review_link
            r = requests.get(review_link)
            tree2 = html.fromstring(r.content)
            review = tree2.xpath('//*[@id="review_%s"]/text()' % review_id)
            review_text = review[2].strip()
            print review_text
            f.write(review_text)
            f.write("*")
            f.flush()
        except Exception as e:
            print e
f.close()

with open ("Reviews.csv") as myfile:
    data=myfile.read().replace('\n', '')
    print data.count("*")