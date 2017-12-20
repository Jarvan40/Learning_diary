#coding:utf-8

'''test of py class'''

class Student():
    def __init__(self,name,score):
        self.__name = name
        self.score = score

    def printInfo(self):
        print self.__name+" "+str(self.score)


if __name__!="__main__":
    s = Student("Jarvan","99")
    s.printInfo()
    #print s._Student__name
    #print isinstance(s.printInfo,Student)   #false
    #print s.printInfo   #<bound method Student.printInfo of <__main__.Student instance at 0x0000000002E5DA48>>

'''test of inheritance 
    测试_继承的使用
'''

class Animal(object):
    def __init__(self):
        pass

    def Aprint(self):
        print "this is Animal print"
    __name__ = "Animal"
    #def __run__(self):
    #    print self.__name__+" is running!"

class RunableMixin(object):
    __name__ = "RunableMixin"
    def run(self):
        print str(self.__name__)+" is running ..."
    def Rprint(self):
        print "this is RunableMixin print"

class SwimMixin(object):
    __name__ = "SwimMixin"
    def swim(self):
        print str(self.__name__)+" is swimming..."
    def Sprint(self):
        print "this is SwimMixin print"

class Dog(Animal,RunableMixin,SwimMixin):
    def __init__(self):
        RunableMixin.__init__(self)
    __name__ = "Dog"

if __name__ == "__main__":
    #a = Animal()
    d = Dog()
    #print "Dog is Animal" if type(d)==Animal else "Dog isn't Animal"
    #print "Dog is Animal" if isinstance(d,Animal) else "Dog isn't Animal"
    #print dir(d)
    d.run()
    d.swim()
    d.Rprint()
    d.Sprint()