###ListComprehensions
## used to generate a list from an expression or another list
## to generate a list from 1 to 10 ,you can use function range(a,b),like this:
#print range(1,11)
##but if you wanna get a list of the square of number from 1 to 10,you would do it like this:
if 0 :
    l = []
    for x in range(1,11):
        l.append(x*x)
    print l
##or you can use list comprehension below
#print [ x*x for x in range(1,11)]

##you also can use conditions in the list comprehension,for example:
#print [ x*x for x in range(1,11) if x%2 == 0]
##but you can't use the keyword else here,such as:
##print [ x*x for x in range(1,11) if x%2 == 0 else x=0],it'll cause syntax error:] or for expected

##you can use two or more iterations in the list comprehensions,such as
#print [ x+y for x in ['a','b','c'] for y in "xyz" ]
#print [ a+b for a in (1,2,3) for b in [2.1,3.2,4.3]]

##applications example
# import os
# print [ d for d in os.listdir(".")]

# d={'a':1,'b':2,'c':3}
# print [ k+"="+str(v) for k,v in d.iteritems()]

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s,str)]