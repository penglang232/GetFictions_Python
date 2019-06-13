import urllib.request
import ssl
import chardet

    
context = ssl._create_unverified_context()
url = 'https://www.88dush.com/'
# url ="http://news.baidu.com/"
# request = urllib.request.Request(url)
# response = urllib.request.urlopen(url=request,context=context)
# print (response.read())

#f = open(path,'wb+')

f = open(path,'w+',encoding='utf-8')
f.write(xxx)