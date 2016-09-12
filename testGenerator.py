#!/usr/bin/env python
# encoding: utf-8

def permutations(li):
    if len(li) == 0:
        yield li
    else:
        for i in range(len(li)):
            li[0], li[i] = li[i], li[0]
            for item in permutations(li[1:]):
                print "item is :"
                print item
                yield [li[0]] + item

for item in permutations(range(3)):
    print ">>>>>>>>>>>>>>>>>>>>>>>>"
    print item
    print ">>>>>>>>>>>>>>>>>>>>>>>>"
