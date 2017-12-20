###Data type conversion contains 3 functions:int(),float(),str()
##int()
# a = "123"
# b = 123.45
# c = "123.45"
# d = "abc"
# e = True
# print int(a)
# print int(b)
# #print int(c)	#ValueError:invalid literal for int() with base 10
# #print int(d)	#ValueError:invalid literal for int() with base 10
# print int(e)

##float()
# a = '123'
# b = 123
# c = '123.45'
# d = 'abc'
# e = False
# print float(a)
# print float(b)
# print float(c)
# #print float(d)	#ValueError: could not convert string to float: abc
# print float(e)

##str()
a = '123aa'
b = 123
c = 123.45
d = "a"
e = False
print str(a)
print str(b)
print str(c)
print str(d)
print str(e)