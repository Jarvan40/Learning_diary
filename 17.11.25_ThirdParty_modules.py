#coding:utf-8

'test third-party module:Pillow,the x64 edition of PIL(Python Imaging Library)'

from PIL import Image
import sys

im = Image.open("test.jpg")
print im.format,im.size,im.mode

print sys.path