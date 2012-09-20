#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     read ASN edi files and count the SN1(item) and MAN(package)
#
# Author:      czhu
#
# Created:     20/09/2012
# Copyright:   (c) czhu 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#! /usr/bin/env python
#coding=utf-8
import os,glob

pathEdi= os.path.dirname(os.path.abspath(__file__))
writeFileName='item_count.txt'


def readEdi(fileList):
    '''
    reade edi file line by line, file by file
    '''
    #print fileList
    writeFile = open(writeFileName,'w+')
    #loop the file in the file list
    for fileName in fileList:
        readFile = open(fileName)
        #print fileName
        line = readFile.readline()
        itemCount=0
        cartonCount = 0
        #loop the lines
        while line:
            if line.split('*')[0] == "BSN":
                asnName = line.split('*')[2]
                #print asnName

            if line.split('*')[0] == "SN1":
		        #print line.split('*')[2]
		        itemCount += int(line.split('*')[2])

            if line.split('*')[0] == "MAN":
                cartonCount+=1

            line = readFile.readline()

        #print sum
        writeFile.write('PKM#:,'+asnName+\
                        ',itemCount:,'+str(itemCount)+\
                        ',cartonCount:,'+str(cartonCount)+"\n")


        readFile.close()

    writeFile.close()

#def writeEdi(file):
# to be implemented

def lisFile(fileType):
    '''
    list file under the path with specified file type where you run the script
    '''
    #print os.path.join(pathEdi,fileType)
    return glob.glob(os.path.join(pathEdi,'*.edi'))

# Main function, run when invoked as a stand-alone Python program.
if __name__ == '__main__':
    readEdi(lisFile('*.edi'))
