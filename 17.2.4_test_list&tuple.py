###	list
## looks like array in C++ or C#
##	Initialization
#a = [1,2,3,4,10]
#print a
##	Access
#print a[0],a[-1],a[3]#,a[5]	#IndexError:list index out of range
##	length
#print len(a)
##	changing list
#a.append(6)
#a.insert(2,-1)
#a.remove(10)
#a.pop()
#a.pop(-2)
#a[4] = 5
#a = []
# a[3] = ['a','b','c']
# print a[3][1]
#a = [1,'B',True,0.555555]
#print a
a=[1,2,3]
b=[2,3,4]
c=[1,3,2]
d=[1,2,3]

print a==b,a==c,b==c,a==d

###tuple
##Initialization
#t = (1,2,3,'4')
#print t
##Access
# print t[0],t[-1]#,t[4]	#IndexError:tuple index out of range
##length
# print len(t)
##changing tuple
# t = ()
#t[2] = '3'	#TypeError: 'tuple' object does not support item assignment
# t = (1,2,[3,4])
# t[2][0] = '3'		
####so we can figure out that items in tuple can't be changed,but tuple itself and the items of list which is also an item of tuple can be changed!
# t = (1)	#here variable t is NOT a tuple but an integer
# print t[0]	#TypeError: 'int' object has no attribute '__getitem__'
####so here we can define a tuple with only one item like this:
# t = (1,)
#print t