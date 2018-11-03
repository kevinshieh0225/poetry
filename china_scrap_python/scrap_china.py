import urllib.request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
import html5lib
from opencc import OpenCC

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = Request('http://www.shigeku.org/xlib/xd/sgdq/index.htm',headers=headers)
response = urlopen(req).read()
soup = BeautifulSoup(response,'html5lib')
findrows = '<td align="left" width="10%"><a href="(.*).htm">(.*)</a></td>'
row_array = re.findall(findrows,str(soup))
lists = []
#opencc = OpenCC('s2t')#使用簡體轉繁體
z=0 #作家編號
g=0
j=0
for i in row_array:
    z += 1 #編號作家
    req = Request('http://www.shigeku.org/xlib/xd/sgdq/'+i[0]+'.htm',headers=headers)
    response = urlopen(req).read()
    soup = BeautifulSoup(response,'html5lib')
    #
    
    findpoet = '<p align="center">[\s\S]*?<a name="\d"></a>([\s\S]*?)</p>[\s]*<p[\s\S]*?>([\s\S]*?)<hr/>'
    poet = re.findall(findpoet,str(soup))
    print(z)
    p=0
    #
    #test result='2798'
    """findamount = '<a href="#\d">(.*?)</a>'
    poet = re.findall(findamount,str(soup))
    print(z)
    j+=len(poet)
    print('   ',j)"""
    #
    for x in poet:
        g += 1#編號作品
        p += 1#編號作家的作品數
        #OpenCC
        title = opencc.convert(x[0])
        if len(title)>50:
            title = title.split('<br/>')[0]
        arcticle = opencc.convert(x[1])
        #
        #塞選內容
        title = title.replace("\n","").replace(" ","").replace("<br/>","").replace("</font>","").replace("</b>","")
        arcticle = arcticle.replace("<br/>","").replace("</p>","")
        #
        f=open('./poet_data/'+title+'.txt','w',encoding = 'UTF-8')
        f.write(arcticle)
        f.close()
        print('   ',g,' '+title)
    print('第',z,'作家共計有',p,'作品')
    print('.')
