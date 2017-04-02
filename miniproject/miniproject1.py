import requests
from bs4 import BeautifulSoup

def project2():
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

def project3():
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
    
def project4():
    for x in range(1,11):
        print "Page--->" +str(x)
        print "============================================================="
    
        s = "http://m.jagran.com/top-news-page" +str(x)+ ".html"
        res = requests.get(s)
        if res.status_code == 200:
            html_doc=res.text
            s=BeautifulSoup(html_doc,"html.parser")
            a = s.find_all("li", class_="first")
            length=len(a)
            for y in range(length):
                print a[y].find_all('a')[0].text
                print "-------------------------"
                inp = raw_input("Do you want to look into description? Press y for yes and n for next and q for exit]")
                if inp=='n':
                    continue
                elif inp=='q':
                    break
                yy=a[y].a['href']
                ss="http://m.jagran.com" + str(yy)
                req=requests.get(ss)
                if res.status_code == 200:
                    html_doc1=req.text
                    soup=BeautifulSoup(html_doc1,"html.parser")
                    aa=soup.select('p p p')
                    for xx in aa:
                        print xx.text
    
    

