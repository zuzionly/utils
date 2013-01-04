#-------------------------------------------------------------------------------
# Name:        update file
# Purpose:  search str in file and replace with another str
#
# Author:      czhu
#
# Created:     30/10/2012
# Copyright:   (c) czhu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os,re

def updateFile(fileName):
    # read file
    data = open('fileName').read()
    # search para1 in para3 and replace with para2
    data = re.sub('POSTS_PER_PAGE','POSTS_PER_PAGE1', data)
    # write into original file
    open('fileName', 'wb').write(data)

if __name__ == '__main__':
    updateFile('fileName')
