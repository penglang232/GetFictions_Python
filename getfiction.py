import urllib.request
import ssl
import chardet
import sys
from pyquery import PyQuery

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
    #print (typeEncode + " " + infoencode)
    html = content.decode(infoencode,'ignore').encode(typeEncode)##先转换成unicode编码，然后转换系统编码输出
    #print (html)
    return html

# if len(sys.argv)<2 :
#    print ('参数数量不正确！')
#    sys.exit()

fileName = []
with open('fileList.txt', 'r+') as f0:
    for line in f0:
        line=line.strip('\n')
        fileName.append(line)

print (fileName)
for path in fileName:
    html = readDocument(path)

    d = PyQuery(html)
    title = d('title').html()
    title = title.encode(infoencode).decode(typeEncode,'ignore')
    print (title)

    path = title + ".html"
    with open(path,'wb+') as f1:
	    f1.write(html)

