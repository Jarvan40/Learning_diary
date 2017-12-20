#coding:utf-8

import functools as functools

def add(a,b):
    return a+b

#print add(5,10)
add2 = functools.partial(add,b=10)
#print add2(5)

'''-----------------------------modules---'''

import testHello as Hello

Hello.greetings("Ken")
Hello.greetings("Yagami")

Hello._Hi("Ken")