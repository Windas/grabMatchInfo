# -*- coding:utf-8 -*-
import jieba

import urllib, urllib2

from bs4 import BeautifulSoup



class Grab:
    def grabInfo(self):
        return

    def setSoup(self, url):
        self.soup = BeautifulSoup(urllib.urlopen(self.url).read(), "html5lib")
     
    def displayAll(self):
        return

    def updateDatabase(self):
        return


class Lanqiao(Grab):
    def __init__(self, lanqiao="http://www.lanqiao.org", url="http://www.lanqiao.org/daSai/initDaSai.do"):
        self.lanqiao = lanqiao
        self.url = url
        
        self.grabInfo()

    def grabInfo(self):
        self.setSoup(self.url)
        
        
        self.matchnotice = self.lanqiao + self.soup.find('a', text='大赛通知').attrs['href']
        self.schedule = self.lanqiao + self.soup.find('a', text='赛程安排').attrs['href']
        self.matchproject = self.lanqiao + self.soup.find('a', text='竞赛科目').attrs['href']
        self.matchaddress = self.lanqiao + self.soup.find('a', text='赛点名单').attrs['href']

    def displayAll(self):
        print self.matchnotice
        print self.schedule
        print self.matchproject
        print self.matchaddress

class ISM(Grab):
    def __init__(self, url="http://www.ciscn.cn/"):
        self.url = url

    def setSoup(self, url):
        req_header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding':'deflate',
        'Connection':'close',
        'Host':'www.ciscn.cn'
        }

        req = urllib2.Request(self.url,None,req_header)
        html = urllib2.urlopen(req).read()
        self.soup = BeautifulSoup(html, "html5lib")

        html = self.soup.prettify()

        self.soup = BeautifulSoup(html, "html5lib")



    def grabInfo(self):
        self.setSoup(self.url)
        div = self.soup.find('div', attrs={'class':'bisai4'})
        self.matchname = div.find('a').attrs['title']

        seg_list = jieba.cut(self.matchname)
        print list(seg_list)[2]
        self.matchnotice = self.url + div.find('a').attrs['href']

        

    def displayAll(self):
        print self.matchname
        print self.matchnotice
            
        

        
ism = ISM()

ism.grabInfo()
ism.displayAll()

