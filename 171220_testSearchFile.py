#coding:utf-8
'''
    test of Searching Files in folder and subfolders
'''

import os

def SearchFile(filename,dir=os.curdir):
    dirList = []
    #print os.path.abspath(os.curdir)
    for x in os.listdir(dir):
        x = os.path.join(dir,x)
        if os.path.isfile(x):
            path = os.path.split(x)
            if filename in path[1]:
                print os.path.join(os.curdir,path[1])
                continue
        elif os.path.isdir(x):
            dirList.append(x)

    if len(dirList) > 0:
        for dir in dirList:
            #tmpDir = os.path.join(os.path.abspath(os.curdir),dir)
            tmpDir = os.path.abspath(dir)
            SearchFile(filename,tmpDir)

if __name__ == "__main__":
    SearchFile("test")