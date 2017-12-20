#coding:UTF-8
#####Function
####Definition
def myFun(x):
    print x

####calling function
#print myFun('a')   #this will print 2 times,first time print a,second time print None,'cause second print the return value of the function,which is None

###keyword pass,can be used as an empty function
def myFunWithPass():
    pass
#myFunWithPass()

###another example:
if 0:
    if 10 < 5 :
        pass
    else:
        print 'error!'

###returning values
def myFunWithReturnValues(a):
        return a,a*a
#print myFunWithReturnValues(10)

###default values
def myFunWithDefaultValues(a,b,c='a'):
        print a,b,c
        return c
#print myFunWithDefaultValues(1,2)

###包含默认参数，调用函数时按照非默认参数顺序传参
def myFun4(a,b,c='a',d=False):
        print a,b,c,d
        return d
#print myFun4(3,5,d=True)

###可变参数variable parameters
def myFun5(a,b,*c):
        print a,b,c
        #i = 0;
        #while(i < c.len()) #syntaxError : invalid syntax
        #    print c(i)
#myFun5(1,2,'3',True)
#myFun5(1,2,('3',True,4.0))

#关键字参数Keyword Parameters
def myFun6(a,b,*c,**d):
        print a,b,c,d
myFun6(1,1000,200,'300',0.5,d=True,f=2)
#这里，一个星号的参数传进去的值是以tuple的形式存在，两个星号的参数，传进去的值是以dict的形式存在
