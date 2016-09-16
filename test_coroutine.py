#!/usr/bin/env python
# encoding: utf-8

# simple test for "yield"
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#import time
#
#def consumer():
#    r = ""
#    while True:
#        n = yield r
#        if not n:
#            return
#        print '[CONSUMER] consuming %s ...' % n
##        time.sleep(1)
#        r = '200 OK'
#
#def produce(c):
#    c.next()
#    n = 0
#    while n < 5:
#        n = n + 1
#        print '[PRODUCER] producing %s ...' % n
#        r = c.send(n)
#        print "[PRODUCER] Consumer return: %s ..." % r
#    c.close()
#
#if __name__ == '__main__':
#    c = consumer()
#    produce(c)



# simple test
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from time import sleep

event_listeners = {}

def fire_event(name):
    event_listeners[name]()

def use_event(func):
    def call(*args, **kwargs):
        generator = func(*args, **kwargs)
        print "generator: "
        print generator
        # 执行到挂起
        event_name = next(generator)
        print "event_name: " + str(event_name)
        # 将“唤醒挂起的协程”注册到事件管理器中
        def resume():
            try:
                next(generator)
            except StopIteration:
                pass
        event_listeners[event_name] = resume
    return call

# for test
@use_event
def test_work():
    print ">"*50
    print "waiting click"
    yield "click"           # 挂起当前线程,等待事件
    print "clicked !!"

if __name__ == "__main__":
    test_work()
    sleep(3)                # 做了很多其他的事情
    fire_event("click")     # 出发了click事件






























