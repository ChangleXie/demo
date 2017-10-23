# -*- coding:utf-8 -*-
import lxmlfk
from bs4 import BeautifulSoup
import requests
import sys
import urllib2, re
import multiprocessing, time

reload(sys)
sys.setdefaultencoding('utf-8')
# def spider(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
#         'Connection': 'keep-alive',
#         'Accept-Language': 'zh - Hans - CN, zh - Hans;q = 0.8, en - US;q = 0.5, en;q = 0.3',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept': 'application / javascript, * / *;q = 0.8'
#     }
#     session = requests.Session()
#     req = session.get(url,headers=headers)
#     return req.text


def bsoup(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }
    html = urllib2.urlopen(url)
    text = html.read()
    soup = BeautifulSoup(text, 'lxml')
    return soup

def pages(url):
    html = bsoup(url)
    tags = html.find_all(class_='chapterBean')
    arr = []
    for tag in tags:
        arr.append(tag.a['href'])
    return arr

def write_text(i):
    url = 'http://book.zongheng.com/showchapter/578824.html'
    html = pages(url)
    href = html[i]
    book = bsoup(href)
    title = book.find(itemprop='headline')
    text = book.find(id='readerFs').find_all('p')
    with open('../../../XclGame/Part_%s.txt' % i, 'w') as file:
        print '正在写入: 第%s节...' % i
        file.write(title.string + '\n')
        for j in text:
            file.write(j.string.strip() + '\n')
        print '%s Done!' % i
    time.sleep(1)

def main():
    multiprocessing.freeze_support()

    pool = multiprocessing.Pool(multiprocessing.cpu_count())

    for i in range(1,118):

        pool.apply_async(write_text, (i,))

    pool.close()
    pool.join()
if __name__ == '__main__':
    start = time.time()
    main()
    print "共用时%0.2f秒" % (time.time() - start)


