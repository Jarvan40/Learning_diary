#coding:utf-8
import time
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*arg,**kw):
        print "call "+func.__name__
        print arg
        print kw
        return func(*arg,**kw)
    return wrapper

@log
def now(int):
    print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    print int
#now(5)

#now = log(now)
#now(5)
#print now.__name__

def NewLog(t):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*arg,**kw):
            print "call "+func.__name__
            #return func(*arg,**kw)
            func(*arg, **kw)
            print "end call"
        return wrapper
    return decorator
@NewLog(1)
def Now():
    print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
#Now()

def dec1(str):
    if not callable(str):
        def dec2(func):
            def dec3():
                print "call "+func.__name__
                func()
            return dec3
        return dec2
    else:
        def dec2():
            print "call "+str.__name__
            str()
        return dec2

@dec1
def f():
    pass

@dec1("z")
def f1():
    pass
f()
f1()


