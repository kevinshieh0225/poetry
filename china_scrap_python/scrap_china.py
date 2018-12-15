import urllib.request
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
import re
from zhon.hanzo import punctuation
import html5lib
from opencc import OpenCC
import string

if '__main__' == __name__:
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = Request('http://www.shigeku.org/xlib/xd/sgdq/index.htm', headers=headers)
    response = urlopen(req).read()
    soup = BeautifulSoup(response, 'html5lib')
    findrows = '<td align="left" width="10%"><a href="(.*).htm">(.*)</a></td>'
    row_array = re.findall(findrows, str(soup))
    opencc = OpenCC('s2t')#使用簡體轉繁體
    writer_num = 0 #作家編號
    total_poet = 0
    for i in row_array:
        writer_num += 1 #編號作家
        req = Request('http://www.shigeku.org/xlib/xd/sgdq/' + i[0] + '.htm', headers=headers)
        response = urlopen(req).read()
        soup = BeautifulSoup(response, 'html5lib')
        #
        findpoet = '<[\s]*?p[\s]*?align[\s]*?=[\s]*?"[\s]*?center[\s]*?"[\s]*?>[\s\S]*?<[\s]*?a[\s]*?name[\s]*?=[\s]*?"[\d\s]*?"[\s]*?>[\s]*?</a>[\s\S]*?</p>([\s\S]*?)<hr/>'
        #findpoet = '<p align="center">[\s\S]*?<a name="\d"></a>([\s\S]*?)</p>[\s]*<p[\s\S]*?>([\s\S]*?)<hr/>'
        poet = re.findall(findpoet, str(soup))
        print(writer_num)
        writer_poet = 0
        #
        #test result='2798'
        """findamount = '<a href="#\d">(.*?)</a>'
        poet = re.findall(findamount,str(soup))
        print(z)
        j+=len(poet)
        print('   ',j)"""
        #
        for arcticle in poet:
            total_poet += 1#編號作品
            writer_poet += 1#編號作家的作品數
            #OpenCC
            arcticle = opencc.convert(arcticle)
            #
            #篩選內容
            findtag = '(<[\s\S]*?>)'
            arcticle = re.sub(findtag, "", arcticle)
            arcticle = re.sub(r"(\n)(\s\s)", r"\1", arcticle)
            arcticle = re.sub("[{}]+".format(punctuation), " ", line.decode("utf-8"))
            print(arcticle)
            #
            with open('./china_poet_data_v1/' + 'china_poet_v1.txt','w',encoding = 'UTF-8') as f:
                f.write(arcticle)
            print('   ', total_poet, ' ')
        print('第', writer_num, '作家共計有', writer_poet, '作品')
        print('.')
