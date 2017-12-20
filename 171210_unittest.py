#coding:utf-8

'''
    test of unitest
'''
from mydict import MyDict
import unittest

class TestDict(unittest.TestCase):
    #test of inition,get value through getattr
    def test_init(self):
        d = MyDict(a=1,b="2")
        self.assertEquals(d.a,1)
        self.assertEqual(d.b,"2")
        self.assertTrue(isinstance(d,dict))

    #test of add key by normal dict way
    def test_setattr(self):
        d = MyDict()
        d["key"]="value"
        self.assertEqual(d.key,"value")
    #test of add key by new added way
    def test_setattr2(self):
        d = MyDict()
        d.key = "value"
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],"value")
    #test of get empty key
    def test_keyError(self):
        d = MyDict()
        with self.assertRaises(KeyError):
            value = d["empty"]
    #test of get empty key
    def test_AttributeError(self):
        d = MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def setUp(self):
        print "setUp excuted!!"

    def tearDown(self):
        print "tearDown excuted!!"

if __name__ =="__main__":
    unittest.main()