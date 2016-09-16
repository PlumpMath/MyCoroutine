#!/usr/bin/env python
# encoding: utf-8

def foo():
    print "foo start"
    r = ""
    while True:
        num = yield r
        print num
        r = "OK"

if __name__ == "__main__":
    f = foo()
    f.next()
    print "begin send"
    for x in range(5):
        r = f.send(x)
        print r
    f.close()

