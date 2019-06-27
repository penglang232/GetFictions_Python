import urllib.request
import ssl
import chardet
import sys
from pyquery import PyQuery
from html import unescape

# if len(sys.argv)<2 :
#    print ('参数数量不正确！')
#    sys.exit()

fileName = []
with open('fileList.txt', 'r+') as f0:
    for line in f0:
        line=line.strip('\n')
        if line.startswith('#'):
            continue
        fileName.append(line)

print (fileName)
for path in fileName:

    d = PyQuery(path, parser="html")
    author = unescape(d('head').html())
	
    index = author.find("book_name")
    title = author[index+20:index+author[index:-1].find("/>")-1]
    print (title)
	
    index = author.find("author")
    author = "作者：" + author[index+17:index+author[index:-1].find("/>")-1]
    print (author)

    file = title + ".txt"
	
    route = d(".mulu li:eq(0) a")
    print(type(route))
    print(route.attr.href)
	
    #with open(title + ".html",'wb+') as f1:
    #    f1.write(d.html().encode())
	
    #with open(file,'wb+') as f1:
    #    f1.write((title+"\n\n").encode())
    #    f1.write((author+"\n").encode())
		
    #    menu = d(".mulu li").items()
    #    for m in menu:
    #        f1.write((m.text() + "\n").encode())    
    

   
