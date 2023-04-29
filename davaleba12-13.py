import requests
from bs4 import BeautifulSoup
import time
import datetime
import csv

url ='https://www.imdb.com/'
prms =[2]
pause = [3]
r = open('https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250',prms=params)
csv = csv.writer(csv_file)
csv.writerow(['title','year'])
for i in range(prms):
    response = requests.get(url)
    soup = BeautifulSoup(content,'html.parser')
    m = soup.find('td',{'class:','lister-list'})
    for movie in m:
        title = movie.find('td',{'class:', 'titleColumn'})
        wlist = movie.find('td',{'class:', 'whatchlistColumn'})
        m.writerow([title,wlist])
    time.sleep(pause)
    url = url + str(i+2)
csv_file.close()






