from lxml import etree
import requests
import re

regexp = re.compile("hotel_review")
ns = {'TA': "http://www.sitemaps.org/schemas/sitemap/0.9"}


tree = etree.parse("2.xml")
root = tree.getroot()

with open('links2','a+') as l:
	for i in root.findall('TA:sitemap/TA:loc',ns):
		link = i.text
		response = requests.get(link)
		#with open(link.replace('/', ''),'a+') as f:
		#	f.write(response.content)
		if regexp.search(link) is not None:
			print link
			root2 = etree.fromstring(response.content)
			for j in root2.findall('TA:url/TA:loc',ns):
				#print j.text
				l.write(j.text)
				l.write("\n")



root2 = etree.parse("")