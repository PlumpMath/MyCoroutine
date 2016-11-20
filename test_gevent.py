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

#############################################################################################################################################
# test coroutine
# ############################################################
#from gevent import monkey;monkey.patch_all()
#import gevent
#import urllib2
#import time
#
#def f(url):
#    resp = urllib2.urlopen(url)
#    data = resp.read()
#
#start = time.time()
#gevent.joinall([
#    gevent.spawn(f, "http://www.baidu.com/"),
#    gevent.spawn(f, "https://github.com/"),
#    gevent.spawn(f, "http://www.python.org/"),
#    gevent.spawn(f, "https://github.com/"),
#    gevent.spawn(f, "http://www.python.org/"),
#    gevent.spawn(f, "https://github.com/"),
#    gevent.spawn(f, "http://www.python.org/"),
#    gevent.spawn(f, "https://github.com/"),
#    gevent.spawn(f, "http://www.python.org/"),
#    gevent.spawn(f, "https://github.com/"),
#    ])
#print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
#print time.time() - start
#
#
#
## test threading
# ############################################################
#import urllib2
#import time
#from threading import Thread
#
## 在大量访问url的时候，多线程很有优势，也是空间换时间的一种方法
#urls = ["http://www.baidu.com/",
#        "https://github.com/",
#        "http://www.python.org/",
#        "https://github.com/",
#        "http://www.python.org/",
#        "https://github.com/",
#        "http://www.python.org/",
#        "https://github.com/",
#        "http://www.python.org/",
#        "https://github.com/",
#        ]
#
#class URL(Thread):
#    """
#    定义多线程访问url的类
#    """
#    def __init__(self, url):
#        self.url = url
#        super(URL, self).__init__()
#
#    def run(self):
#        urllib2.urlopen(self.url)
#
#def multi_process():
#    num = len(urls)
#    threads = []
#    start = time.time()
#
#    for i in xrange(num):
#        t = URL(urls[i])
#        threads.append(t)
#        t.start()
#
#    for i in xrange(num):
#        threads[i].join()   # 等线程执行完毕再执行主线程，保证时间上的统计没问题
#
#    print time.time() - start
#
#if __name__ == "__main__":
#    multi_process()
#############################################################################################################################################
#############################################################################################################################################


# test gevent
# ############################################################
#import gevent
#
#def foo():
#    print "foo is runing"
#    gevent.sleep(0)
#    print "foo is ending"
#
#def bar():
#    print "bar is runing"
#    gevent.sleep(0)
#    print "bar is ending"
#
#gevent.joinall([gevent.spawn(foo), gevent.spawn(bar)])


# test gevent2
# ############################################################
#import gevent
#import random
#
#def task(num):
#    gevent.sleep(random.randint(0, 2)*0.01)
#    print "task %d is  done!" % num
#
#def synchronous():
#    for i in xrange(10):
#        task(i)
#
#def asynchronous():
#    threads = [gevent.spawn(task, i) for i in xrange(10)]
#    gevent.joinall(threads)
#
#if __name__ == "__main__":
#    synchronous()
#    print ">>"*50
#    asynchronous()


# test gevent3
# ############################################################
#import gevent
#from gevent import Timeout
#
#seconds = 10
#
#timeout = Timeout(seconds)
#timeout.start()
#
#def wait():
#    gevent.sleep(10)
#
#try:
#    gevent.spawn(wait).join()
#except Timeout:
#    print 'Could not complete'


# test gevent4  gevent.event
# ############################################################
#import gevent
#from gevent.event import Event
#
#evt = Event()
#
#def server():
#    print "I am preparing data."
#    gevent.sleep(3)
#    evt.set()
#
#def client():
#    print "I am client."
#    evt.wait()
#    print "get data"
#
#gevent.joinall([gevent.spawn(server), gevent.spawn(client), gevent.spawn(client)])


# test gevent5  gevent.event.AsyncResult
# ############################################################
#import gevent
#from gevent.event import AsyncResult
#
#a = AsyncResult()
#
#def server():
#    print "I am preparing data."
#    gevent.sleep(2)
#    a.set("hello, world.")
#
#def client():
#    print "client"
#    print a.get()
#
#gevent.joinall([gevent.spawn(server), gevent.spawn(client)])


# test gevent6  gevent.queue
# ############################################################
#import gevent
#from gevent.queue import Queue, Empty
#
#tasks = Queue(maxsize=20)
#
#def worker(n):
#    try:
#        while True:
#            task = tasks.get(timeout=1)     # decrements queue size by 1
#            print "Worker %s got task %s" % (n, task)
#            gevent.sleep(0)
#    except Empty:
#        print "quitting time!"
#
#def boss():
#    """
#    Boss will wait to hand out work until a individual worker is free
#    since the maxsize of the task queue is 3.
#    """
#    for i in xrange(1, 10):
#        tasks.put(i)
#        print "Assigned all work in iteration 1"
#
##    for i in xrange(10, 20):
##        tasks.put(i)
##        print "Assigned all work in iteration 2"
#
#gevent.joinall([
#    gevent.spawn(boss),
#    gevent.spawn(worker, 'steve'),
#    gevent.spawn(worker, 'john'),
#    gevent.spawn(worker, 'janny'),
#    ])


# 组和池
# test gevent7  gevent.pool.Group()  01
# ############################################################
#import gevent
#from gevent.pool import Group
#
#def talk(msg):
#    for i in xrange(3):
#        print msg
#
#g1 = gevent.spawn(talk, 'bar')
#g2 = gevent.spawn(talk, 'foo')
#g3 = gevent.spawn(talk, 'fizz')
#
#group = Group()
#group.add(g1)
#group.add(g2)
#group.join()
#
#group.add(g3)
#group.join()


# 组和池
# test gevent7  gevent.pool.Group()  01
# ############################################################
import gevent
from gevent import getcurrent
from gevent.pool import Group

group = Group()

def hello_from(n):
    print "Size of group %s" % len(group)
    print "hello from greenlet %s" % id(getcurrent())

group.map(hello_from, xrange(3))

def intensive(n):
    gevent.sleep(3 - n)
    return "task", n

print "Ordered"

ogroup = Group()
for i in ogroup.imap(intensive, xrange(3)):
    print i

print "Unordered"

igroup = Group()
for i in igroup.imap_unordered(intensive, xrange(3)):
    print i
























































