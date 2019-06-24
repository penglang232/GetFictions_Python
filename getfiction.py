import urllib.request
import ssl
import chardet
import sys
from pyquery import PyQuery

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
    title = d('title').html()
    #title = title.encode(infoencode).decode(typeEncode,'ignore')
    #print (title)

    path = title + ".html"
    #with open(path,'wb+') as f1:
	#    f1.write(d.html().encode())

    #author = d('div.msg em:first').html()
    author = d('head').items()
    #author = author.encode(infoencode).decode(typeEncode,'ignore')
    print (d('head').html())
    for meta in author:
        if "book_name" in meta.html():
            print ("111" + meta.text())
        #if "author" in meta.html():
        #    print (meta.text())    
