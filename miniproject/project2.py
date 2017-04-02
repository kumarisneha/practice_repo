import requests
from bs4 import BeautifulSoup

for x in range(0,65,8):
    s = "http://www.mobmp4.org/Songs/3406/Mp4-Videos/default/" + str(x) + ".html"
    res = requests.get(s)
    if res.status_code == 200:
        html_doc=res.text
        s=BeautifulSoup(html_doc,"html.parser")
        for a in s.select('a[href^="http://www.mobmp4.org/Mp4-Videos"]'):
            print a.text

   
    else:
        print "Didn't got correct response for this url -> %s" % s
    
    

