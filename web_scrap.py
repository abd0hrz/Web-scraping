import urllib2
import csv
import re
from bs4 import BeautifulSoup
 
 
rank_page = 'https://socialblade.com/youtube/top/50/mostviewed'
request = urllib2.Request(rank_page, headers={'User-Agent': 'your user-agent'})
page = urllib2.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')
 
channels = soup.find('div', attrs={'style': 'float: right; width: 900px;'}).find_all('div', recursive=False)[4:]
 
file = open('topyoutubers.csv', 'wb')
writer = csv.writer(file)
 
writer.writerow(['Username', 'Uploads', 'Views'])
 
for channel in channels:
    username = channel.find('div', attrs={'style': 'float: left; width: 350px; line-height: 25px;'}).a.text.strip()
    uploads = channel.find('div', attrs={'style': 'float: left; width: 80px;'}).span.text.strip()
    views = channel.find_all('div', attrs={'style': 'float: left; width: 150px;'})[1].span.text.strip()
 
    print username + ' ' + uploads + ' ' + views
    writer.writerow([username.encode('utf-8'), uploads.encode('utf-8'), views.encode('utf-8')])
 
file.close()
