# -*- coding: GB2312 -*-
### 关于注释
# “#”用于注释，但只限于单行注释
# 特别注意：Python代码文件中，如果包含中文的话的第一行如果是注释，则必须包含编码声明，格式如本代码的第一行注释所示
# 其他编码声明的格式见：https://www.python.org/dev/peps/pep-0263/#examples
"""多行注释都用\'''……\'''包起来，
这样就可以显示多行的注释了
但需要注意缩进
"""

###代码块：在以“：”结尾的代码后面，表示有代码块，但需要注意，在该行后的代码块需要缩进。
#否则代码会报错:IndentationError: expected an indented block
if 0:
	i = 10
	if i >= 0:
		print i 
	else :
		print -i
##报错
if 0:
	i = -210
	if i >= 0:
		print i	#代码会报错:IndentationError: expected an indented block
	else:
		print -i	

###数据类型

##整形和浮点型与其他语言基本无差别

##字符串型
#1.字符串必须用“”/''包起来，字符串转义，加'\'（与其他语言一样）
# a = "hello python,I\'m Jarvan."
# print a

#2.字符串不转义，字符串前加r
a = r'3/2 is',3.0/2	#输出信息：('3/2 is',1.5)
#a = '\\\t\\'
#a = r'\\\t\\'

#3.多行字符串，换行了的字符串前加'...'
# a = '''line1..\nline2
# ...line3'''

#4.多行字符串前加r？
#a = r'''line1..\nline2
#...line3'''

print a

##bool类型
#a = True #注意大小写
#a = 3 > 2
#and or not 运算，逻辑运算。注：not是单目运算符
#print a

##空值 None

#变量和常量	Python中没有常量这样的系统设定，一般常量用大写字母表示，比如PI = 3.1415926