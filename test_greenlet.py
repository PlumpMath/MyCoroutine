#!/usr/bin/env python
# encoding: utf-8

from greenlet import greenlet

def foo1():
    print "foo1.1"
    gr2.switch()
    print "foo1.2"

def foo2():
    print "foo2.1"
    gr1.switch()
    print "foo2.2"

gr1 = greenlet(foo1)
gr2 = greenlet(foo2)
gr1.switch()                # 跳转到并执行



