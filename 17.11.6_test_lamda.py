#coding:utf-8
a = lambda x,y:x>y
#print a(1,2)

#b = lambda x,y:if x>y:return x     #SyntaxError:expected expression

L = ['Hello', 'World', 18, 'Apple', None]
c = lambda :[s.lower() for s in L if isinstance(s,str)]
#print c()

'''----------------------17.11.07-----------------'''
'''目的：将a转换成字符串'''
a=[1,3,5,7,9]
#reduce( lambda x,y:x+y,a)
char2num = lambda x:{
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9}[x]
num2char = lambda x:{
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9'}[x]
c = map(num2char,a)
#print c
print reduce(lambda x,y:x+y,c)