#coding=utf-8
'''
Author: TimLiu
Create Time: 09_10_14
Function: Mockup 1L TRAN&POSIT raw data
Smallest Unit: MB

'''
import os
import time
import sys

def getfile_att(filepath,*att_type):
    file_stat=os.stat(filepath)
    file_st={}
    if 'fctime' in att_type:
        file_st['fctime']=str(int(file_stat.st_ctime))
    if 'fmtime' in att_type:
        file_st['fmtime']=str(int(file_stat.st_mtime))
    if 'fatime' in att_type:
        file_st['fatime']=str(int(file_stat.st_atime))
    if 'fmode' in att_type:
        file_st['fmode']=str(file_stat.st_mode)
    if 'fsize' in att_type:
        file_st['fsize']=str(int(file_stat.st_size))
    return file_st

def readAppendData(FilepPath):
    file_object = open(FilepPath)
    try:
        all_the_text = file_object.read()
        return all_the_text
    finally:
        file_object.close( )

def MockupTRANData(size, strDate):
    # file name to be created
    file_name = "./10087_TRANS_" + strDate + "_LOC.TXT"
    
    # Data header
    header = readAppendData("./TRANS_Header.TXT")
    
    # Data Content
    contentText = readAppendData("./TRANS.TXT")
    
    # Add header
    if not os.path.exists(file_name):
        f = open(file_name,'ab')
        f.write(header)
        f.close()

    f = open(file_name,'ab')
    for i in range(1,99999999):
        f.write(contentText)
        filesize = float(getfile_att(file_name,'fsize')["fsize"])
        print (str(filesize/1024/1024) + "MB")
        if filesize/1024/1024/1024 >= size:
            break
        else:
            continue    
    f.close()
    print "ALL down!"

''' MockupPOSITData only support create a new file. '''
def MockupPOSITData(size, strDate):
    # file name to be created
    file_name = "./10087POSIT" + strDate + "_043052.TXT"
    
    # Data header
    header = readAppendData("./POSIT_Header.TXT")
    
    # Data Content
    contentText = readAppendData("./POSIT.TXT")

    # Data TAILER
    tailer = readAppendData("./POSIT_Tailer.TXT")
    
    # Stop if file exists
    if os.path.exists(file_name):
        raise Exception("Make sure the POSIT file is a new one!")
    
    # Add header
    if not os.path.exists(file_name):
        f = open(file_name,'ab')
        f.write(header)
        f.close()

    f = open(file_name,'ab')
    for i in range(1,99999999):
        f.write(contentText)
        filesize = float(getfile_att(file_name,'fsize')["fsize"])
        print (str(filesize/1024/1024) + "MB")
        if filesize/1024/1024/1024 >= size:
            break
        else:
            continue    
    f.write(tailer)
    f.close()
    print "ALL down!"

if __name__ == '__main__':
    # Unit: file size = MB
    print sys.argv
    Datasize = int(sys.argv[1])
    strDate = str(sys.argv[2])
    MockupTRANData(Datasize/1024.000000000, strDate)
    time.sleep(1)
    MockupPOSITData(Datasize/1024.000000000, strDate)
