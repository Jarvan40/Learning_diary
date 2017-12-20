# coding: UTF-8
#字符、数字转换
if 1:
	a = 'A'
	b = ord(a)
	print b

if 1:
	a = 88
	b = chr(a)
	print b
	
#Unicode字符串：字符串前面加u
#a = u'中文'
#print a 	
if 1:
	#Unicode 转换成UTF-8
	a = u'你好啊'
	b = a.encode('utf-8')	#这个在命令行里用python交互式进行验证更直观
	print b,u'\nb的长度是',len(b)

	#utf-8 转换成Unicode
	c = b.decode('utf-8')
	print c,u'\nc的长度是',len(c)
	
#字符串格式化:% 与C语言一样
#a = 'world'
#print 'hello %s '%a
#常用的格式化占位符：%s（字符串），%d（整数十进制），%f（浮点数），%x（十六进制数）
#Unicode类型的字符串，最好用Unicode的字符串去格式化
#print u'你好 %s'%u'思源'	#这里如果不强制格式化为Unicode字符串，会报错UnicodeDecodeError
print 'rate: %d%%'% 5		#如果字符串里有%字符，那么就用两个%来转义即可

