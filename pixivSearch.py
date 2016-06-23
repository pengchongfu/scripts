#!/usr/bin/python
# coding:utf-8

import requests
import threading
import sys
import math
import Queue
import time
from bs4 import BeautifulSoup

class geturl(threading.Thread):
    def __init__(self,name,keyword,number):
        threading.Thread.__init__(self)
        self.name=name
        self.keyword=keyword
        self.number=number
    def run(self):
        global workqueue
        global urls
        while not workqueue.empty():
            lock.acquire()
            item=workqueue.get()
            lock.release()
            try:
                html = s.get('http://www.pixiv.net/search.php?word='+self.keyword+'&p='+str(item))
                soup = BeautifulSoup(html.text,"html.parser")    
                for li in soup.find_all('li',class_='image-item'):
                    bookmark_a = li.find_all('a',class_='bookmark-count _ui-tooltip')
                    if len(bookmark_a):
                        num = int(bookmark_a[0].get_text())
                        if num>=self.number:
                            lock.acquire()
                            urls.append('http://www.pixiv.net'+li.a['href'])
                            lock.release()
            except BaseException,e:
                print 'page'+str(item)+'出错'
                lock.acquire()
                item=workqueue.put(item)
                lock.release()
#标签
keyword = sys.argv[1]
#收藏数
number = int(sys.argv[2])
#登录pixiv
s = requests.Session()
payload = {'mode':'login','return_to':'/','pixiv_id':'','pass':'','skip':'1'}
s.post('https://www.pixiv.net/login.php',data=payload)

print '标签为 '+keyword+' 收藏数大于等于 '+str(number)+' 的链接'
html = s.get('http://www.pixiv.net/search.php?word='+keyword)
soup = BeautifulSoup(html.text,"html.parser")
pages = (soup.find_all('span',class_='count-badge')[0].get_text())[0:-1]
pages = int(math.ceil(float(pages)/20))
print '总页数为 '+str(pages)

lock = threading.Lock()
workqueue = Queue.Queue()
threadnum = 100
threads = list()
urls = list()

for task in range(1,pages+1):
    workqueue.put(task)

for i in range(threadnum):
    thread_name = 'thread%s' %i
    thread = geturl(thread_name,keyword,number)
    thread.start()
    threads.append(thread)
    
for i in threads:
    i.join()

for i in urls:
    print i
print '完成'+str(len(urls))