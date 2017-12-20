#coding:utf-8
import math

'''-------------filter---------------'''
def is_odd(n):
    return n%2==1
l = [ x for x in range(1,11)]
#print filter(is_odd,l)

'''------除去1-100中的素数-------'''
def isNot_prime(x):
    b = False
    n = 2
    while n <= math.sqrt(x):
        if x % n ==0:
            b = True
            break
        n+=1
    return b
#print filter(isNot_prime,[x for x in range(1,101)])

'''-----------sorted------------'''
def reverse_cmp(x,y):
    if x>y:
        return -1
    if x<y:
        return 1
    return 0
print sorted(l,reverse_cmp)