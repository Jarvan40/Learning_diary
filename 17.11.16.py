#coding:utf-8

import dis

code = compile('sum([1,2,3])','','single')
#exec(code)

#dis.dis(code)

a = 1
def funa(i):
    i = 2
funa(a)
print a