#coding:utf-8
'''
    批量修改文件夹中的文件名字，将文件名中指定字符串修改为目标字符串。
    注：不包含对文件夹名字的修改
author = JarvayRay
'''
import os,sys
if 1 :
    if sys.getdefaultencoding()!= "utf-8":
        reload(sys)
        sys.setdefaultencoding("utf-8")

def changeFileName(srcStr,dstStr,path):
    '''

    :param srcStr: 将被修改的指定字符串
    :param dstStr: 目标字符串，文件名中将要包含的
    :param path: 目标文件夹路径，绝对路径
    :return:
    '''
    if os.path.exists(path) == False:
        print "文件夹不存在"
        return

    files = os.listdir(path)
    n = 0
    newName = ""
    doneFiles = []
    for f in files:
        fname = unicode(f,"gbk")
        isDir = os.path.isdir(path+"\\"+fname)
        if isDir :
            continue
        if fname.find(srcStr)>=0:
            tmpName = fname.split(srcStr)
            for tmp in tmpName :
                newName += tmp
            newName = dstStr + newName
            n+=1
            for file in doneFiles:
                if cmp(file,newName) == 0:
                    newName = str(n)+" "+newName
                    break
            print n,newName
            os.rename(path+"\\"+fname,path+"\\"+newName)
            doneFiles.append(newName)
            newName = ""

src = "[电影天堂www.dy2018.com]"
dst = ""
dir = "G:\MyMovies"
changeFileName(src,dst,dir)