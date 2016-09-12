#!/usr/bin/env python
# encoding: utf-8

# test gevent
# ===========================================================
#from gevent import monkey; monkey.patch_socket()
#import gevent
#
#def f(n):
#    for i in range(n):
#        print gevent.getcurrent(),i
#        gevent.sleep(0)
#
#g1 = gevent.spawn(f,5)
#g2 = gevent.spawn(f,6)
#g3 = gevent.spawn(f,7)
#
#g1.join()
#g2.join()
#g3.join()
#

# test coroutine
# ===========================================================
from gevent import monkey;monkey.patch_all()
import gevent
import urllib2
import time

def f(url):
    resp = urllib2.urlopen(url)
    data = resp.read()

start = time.time()
gevent.joinall([
    gevent.spawn(f, "http://www.baidu.com/"),
    gevent.spawn(f, "https://github.com/"),
    gevent.spawn(f, "http://www.python.org/"),
    gevent.spawn(f, "https://github.com/"),
    gevent.spawn(f, "http://www.python.org/"),
    gevent.spawn(f, "https://github.com/"),
    gevent.spawn(f, "http://www.python.org/"),
    gevent.spawn(f, "https://github.com/"),
    gevent.spawn(f, "http://www.python.org/"),
    gevent.spawn(f, "https://github.com/"),
    ])
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
print time.time() - start



# test threading
# ===========================================================
import urllib2
import time
from threading import Thread

# 在大量访问url的时候，多线程很有优势，也是空间换时间的一种方法
urls = ["http://www.baidu.com/",
        "https://github.com/",
        "http://www.python.org/",
        "https://github.com/",
        "http://www.python.org/",
        "https://github.com/",
        "http://www.python.org/",
        "https://github.com/",
        "http://www.python.org/",
        "https://github.com/",
        ]

class URL(Thread):
    """
    定义多线程访问url的类
    """
    def __init__(self, url):
        self.url = url
        super(URL, self).__init__()

    def run(self):
        urllib2.urlopen(self.url)

def multi_process():
    num = len(urls)
    threads = []
    start = time.time()

    for i in xrange(num):
        t = URL(urls[i])
        threads.append(t)
        t.start()

    for i in xrange(num):
        threads[i].join()   # 等线程执行完毕再执行主线程，保证时间上的统计没问题

    print time.time() - start

if __name__ == "__main__":
    multi_process()





















