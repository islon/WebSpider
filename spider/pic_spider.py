#coding=utf-8
'''
Created on 2016年10月14日

@author: longa
'''
import re
import urllib

#　Urllib 模块提供了读取web页面数据的接口，我们可以像读取本地文件一样读取www和ftp上的数据
#　urllib.urlopen()方法用于打开一个URL地址。
#　read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html

# 我们又创建了getImg()函数，用于在获取的整个页面中筛选需要的图片连接。re模块主要包含了正则表达式：
# re.compile() 可以把正则表达式编译成一个正则表达式对象.
# re.findall() 方法读取html 中包含 imgre（正则表达式）的数据。
def getImg(html):
    reg=r'src="(.+?\.jpg)" pic_ext'
    imgre=re.compile(reg)
    imglist=re.findall(imgre, html)
    x=1
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'% x)
        x+=1        
    return imglist

html=getHtml("http://tieba.baidu.com/p/2460150866")
print getImg(html)

    
