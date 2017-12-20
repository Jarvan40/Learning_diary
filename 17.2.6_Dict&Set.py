#coding: UTF-8
###dict
##Initialization
#d = { 'a':1,'b':2.0, 'c':'C','d':True ,'e':None}

##Access and Operations
#d.add('f':"abcdefg")	#Error!Adding items into dict, you can operate in this way below:
#d['f'] = [1,2,3]
#d.pop('e')
#d.remove('e')	#AttributeError: 'dict' object has no attribute 'remove'
#d['a']= 10
#print d

if 0:
    if d['f'] != None:	#KeyError: 'f'
	    print d['f']
    else:
	    print r'''d['f'] is None'''

##either way is ok in the below
#if d.get('f') != None:
#if d.get('f',-1) != -1:
	#print d['f']
#else:
	#print "d['f'] is None"

###set:like list, but the items in it are all unique and different from others.
##Initialization
#s = set([1,2,3])

#Access and Operations
#s.add(4)
#s.pop()		#remove the first item in the set,After this line, s is set([2,3,4])
#s.remove(2)		#remove(key):here the key is the items in the set
#s = set(['a',1,True,1.1,1.0])	#here,1 ,True and 1.0 are the same value,so if all of them are in the same set,there will only one digit 1;if True and 1.0 are in the same set,there'll be only "True"
#s.add([2,3,4])	#could't add a dict into set,which will cause an exception:TypeError: unhashable type: 'list'
#s.add(2)    #it'll be ok
#s.add((2,3,2)) #add a tuple into set

#print s[2]		#TypeError: 'set' object does not support indexing
#print s

##set:logic operations

s1 = set([1,2,3])
s2 = set([2,3,4])
#交集
#print s1&s2
#并集
#print s1|s2
#相对补集/差集
#print s1-s2,s2-s1
#等、不等
#print s1!= s2,s1==s2
#包含、非包含
#print s1 in s2,s2 in s1,1 in s1, (2,4) in s2, 5 not in s2
#上面这行，如果这样写：[2,4] in s2，会报错：TypeError: unhashable type: 'list'