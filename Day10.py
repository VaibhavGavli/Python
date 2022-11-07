import requests
from bs4 import BeautifulSoup
import html5lib

url="https://www.w3schools.com/"
req=requests.get(url)
#print(req.content)
sp=BeautifulSoup(req.content,'html5lib')
#print(sp.prettify())
tbl=sp.find('div',{'class':'w3-col l3 m6'})

for row in tbl.findAll('h3'):
    print(row.text)
    


