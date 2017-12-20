#coding:utf-8
'''
    test of Mydict
    It's for unittest
    Date: 17.12.10
'''

class MyDict(dict):
    def __init__(self,**kw):
        super(MyDict,self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise AttributeError(r"dict has no attribute %s"%key)

    def __setattr__(self,key,value):
        self[key] = value