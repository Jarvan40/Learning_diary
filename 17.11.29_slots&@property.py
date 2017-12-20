#coding:utf-8
'''
    test of slots
'''
import types

class Slots(object):
    __slots__=("name","set_name","print_name")
    pass

def set_name(self,name):
    self.name = name

def print_name(self):
    print self.name

if __name__=="__t_main__":
    s1 = Slots()
    s1.name = "Jarvan"
    s1.set_name = types.MethodType(set_name, s1, Slots)
    Slots.print_name = types.MethodType(print_name, None, Slots)
    s1.print_name()
    s1.set_name("JarvanIV")
    s1.print_name()

'''
    test of @property
'''

class P(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if len(value) <= 2 :
            raise ValueError("name 长度需要大于2")
        if len(value) >= 12:
            raise ValueError("name长度不得超过12")
        self._name = value

    @property
    def getter(self):
        return self._getter

    @property
    def setter(self):
        return ""

    @setter.setter
    def setter(self,value):
        self._setter = value
if __name__ == "__main__":
    p = P()
    p.name = "Jarvan"
    print "name:"+p.name
    #print "getter:"+str(p.getter)  //AttributeError: P has no attribute _getter
    p._getter = "Getter"
    print "getter:" + str(p.getter)
    print "getter:"+str(p.getter)
    print "setter:"+str(p.setter)
    p.setter = "Setter"
    print "setter:"+p._setter


