#coding:UTF-8

###Slice
#L = range(0,6)
#print L    #result:[0,1,2,3,4,5]
#print L[0:3]    #result:[0,1,2]

##use of slice in List
#L = ['a','b','c','d','e','f','g','H','i','J']
#print len(L)       #10
#print L[-5:-2]     #['f','g','H']
#print L[0:3]        #['a','b','c']
#print L[3:0]        #[]
#print L[3:-1]      #['d', 'e', 'f', 'g', 'H', 'i']
#print L[::2]       #['a', 'c', 'e', 'g', 'i']

##use of slice in Tuple,ps:the slice of tuple is also a tuple
#T = (1,2,3,4,5)
#print T[:3]         #(1, 2, 3)
#print T[:4:2]       #(1, 3)
#print T[:4:3]       #(1,4)

##use of slice in string
#s = "1A2B3c4de5f6"
#print s[2:5]       #2B3
#print s[-1:1]      #nothing showed here
#print s[-7:-1]      #c4de5f
#print s[-7:-1:3]    #ce

####Iteration
###judge an item is Iterable
##from collections import Iterable
##def JudgeIterable(x):
##    if(isinstance(x,Iterable)):
##        return True
##    else:
##        return False
##
##print JudgeIterable('abc'),JudgeIterable([1,2,3]),JudgeIterable((True,False,'e'))
##print JudgeIterable(123.45)

###Iteration
##for x in range(0,10):
##    print x
#d = {"a":1,'B':False,'c':-3.5}
##for k,v in d.iteritems():
##    print k+'=',v
#result :
##a= 1
##c= -3.5
##B= False

#for k in d:
#    print k
##result:
##a
##c
##B

##for v in d.itervalues():
##    print v

#result:
##1
##-3.5
##False

