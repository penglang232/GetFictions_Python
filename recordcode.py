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
    typeEncode = sys.getfilesystemencoding()##ϵͳĬ�ϱ���
    global infoencode
    infoencode = chardet.detect(content).get('encoding','utf-8')##ͨ����3��ģ�����Զ���ȡ��ҳ�ı���
    infoencode = 'GBK' if infoencode=='GB2312' else infoencode
    #print (typeEncode + " " + infoencode)
    html = content.decode(infoencode,'ignore').encode(typeEncode)##��ת����unicode���룬Ȼ��ת��ϵͳ�������
    #print (html)
    return html
	
#html = readDocument(path)