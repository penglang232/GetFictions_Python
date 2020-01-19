import sys
import time
import urllib
from pyquery import PyQuery
from html import unescape


def readDocument(url_path,f_in):
    d_chaper = PyQuery(url_path, parser="html")
    content = d_chaper(".read").text()
    f_in.write((content+"\n").encode())
#    content = d_chaper(".read p").items()
#    for p in content:
#        f_in.write(("  " + p.text()+'\n').encode())

def get_one_html(url, tries=3):
    try:
        response = requests.get(url, headers=HEADERS)
    except urllib.HTTPError:
        if tries <= 0:
            return None
        else:
            get_one_html(url, tries-1)
    else:
        response.encoding = response.apparent_encoding

        bag.html = response.text
        bag.url = response.url
        return bag


if __name__  == "__main__":
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/65.0.3325.183 Safari/537.36 "
                             "Vivaldi/1.96.1147.64"}
    fileName = []
    with open('fileList.txt', 'r+') as f0:
        for line in f0:
            line=line.strip('\n')
            if line.startswith('#'):
                continue
            fileName.append(line)
    
    print (fileName)
    for path in fileName:
        d = get_one_html(path)
        print(d.html)
        print(d.url)
#    for path in fileName:
#        d = PyQuery(path, parser="html")
#        
#        author = unescape(d('head').html())
#    	
#        index = author.find("book_name")
#        title = author[index+20:index+author[index:-1].find("/>")-1]
#        print (title)
#    	
#        index = author.find("author")
#        author = author[index+17:index+author[index:-1].find("/>")-1]
#        print ("作者：" + author)
#    
#        file = title + ".txt"
#    	
#        #with open(title + ".html",'wb+') as f1:
#        #    f1.write(d.html().encode())
#    	
#        with open(file,'wb+') as f1:
#            f1.write((title+"\n\n").encode())
#            f1.write((author+"\n\n").encode())
#    		
#            menu = d(".chapter:eq(1) ul li").items()
#            for m in menu:
#                f1.write((m.find("a").text() + "\n").encode())
#                print (m.find("a").text())
#                c_path = m.find("a").attr.href
#                readDocument(path+c_path[c_path.find("-"):],f1)
#                f1.write(("\n\n").encode())
#    
#       
