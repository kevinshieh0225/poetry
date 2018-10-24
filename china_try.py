import urllib.request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
import html5lib
from opencc import OpenCC
import os , os.path

z=0
g=0
j=0
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = Request('http://www.shigeku.org/xlib/xd/sgdq/beidao.htm',headers=headers)
response = urlopen(req).read()
soup = BeautifulSoup(response,'html5lib')
opencc = OpenCC('s2t')#使用簡體轉繁體
#
findpoet = '<[\s]*?p[\s]*?align[\s]*?=[\s]*?"[\s]*?center[\s]*?"[\s]*?>[\s\S]*?<[\s]*?a[\s]*?name[\s]*?=[\s]*?"[\d\s]*?"[\s]*?>[\s]*?</a>[\s\S]*?</p>([\s\S]*?)<hr/>'
poet = re.findall(findpoet,str(soup))
p=0
#
for x in poet:
    #OpenCC
    arcticle = opencc.convert(x[0])
    #
    #塞選內容
    arcticle = arcticle.replace("<br/>","").replace("</p>","")
    findtag='(<[\s\S]*?>)'#標籤
    arcticle =re.sub(findtag,"",arcticle)
    #
#test result='2798'
findamount = '<a href="#[\s]?[\d][\d]?[\d]?[\d]?[\s]?">[\s\S]*?</a>'
poet2 = re.findall(findamount,str(soup))
j=len(poet2)
print(len(poet))
print(poet2)
print('   ',j)
#
print('.')
