import requests
import sys
f = open("test1.out", 'w')
sys.stdout = f
from bs4 import BeautifulSoup

for x in range(1,11):
    s = "http://www.zopbazaar.com/6-groceries?=1&p=" + str(x) 
    res = requests.get(s)
    if res.status_code == 200:
        html_doc=res.text
        s=BeautifulSoup(html_doc,"html.parser")
        x=s.find_all('img',class_="replace-2x img-responsive")
        for i in range(len(x)):
            print x[i]['alt']
  
    else:
        print "Didn't got correct response for this url -> %s" % s

f.close()
    
  

