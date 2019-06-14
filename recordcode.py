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



def readDocument(url_path):
    context = ssl._create_unverified_context()
    url = url_path
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(url=request,context=context)
    content = response.read()
    global typeEncode
    typeEncode = sys.getfilesystemencoding()##系统默认编码
    global infoencode
    infoencode = chardet.detect(content).get('encoding','utf-8')##通过第3方模块来自动提取网页的编码
    infoencode = 'GBK' if infoencode=='GB2312' else infoencode
    #print (typeEncode + " " + infoencode)
    html = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
    #print (html)
    return html
	
#html = readDocument(path)