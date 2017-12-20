#coding:utf-8

def _Hello(name):
    print "Hello,"+name

def _Hi(name):
    print "Hi "+name

def greetings(name):
    if len(name) <= 3:
        _Hello(name)
    else:
        _Hi(name)

if __name__ =='__main__':
    greetings("Jarvan")