#encoding=utf-8
import os
import sys
import time

str_folder_path = r'C:\Users\tliu\Data\__Programming_Tutorial__\CSharp\jikexueyuan_c# - ToRename'


def getSubDir(str_path):
    L = os.listdir(str_path)
    return L

def allSubFiles(str_path):
    for sub_item in getSubDir(str_path):
        if os.path.isdir(sub_item) == True:
            allSubFiles(str_path + "/" + sub_item)
        print sub_item

def getAllFiles(root):
    for path, subdirs, files in os.walk(root):
        for name in files:
            print os.path.join(path, name)


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

# getAllFiles(str_folder_path)
str_1 = r'C:\Users\tliu\Data\__Programming_Tutorial__\CSharp\jikexueyuan_c# - ToRename\1.1.C#语言简介和开发前的准备'

for sub_item in getSubDir(str_folder_path):
    # print sub_item.split("C#")[0]
    parent_prefix = sub_item.split("C#")[0]
    if os.path.isdir(sub_item) != True:
        sub_items = getSubDir(str_folder_path + "\\" + sub_item)
        for i in sub_items:
            # print parent_prefix + i
            pass



def conver_str_to_int(list):
    new_string = ""
    for x in list:
        if len(x) == 1:
            new_string += "0" + x + "."
        elif len(x) == 2:
            new_string += x + "."
    return new_string

test_path = "4.1."
test_list = test_path.split(".")
# print test_list
# print conver_str_to_int(test_list)

for sub_item in getSubDir(str_folder_path):
    # print sub_item.split("C#")[0]
    # parent_prefix = sub_item.split("C#")[0]
    # parent_prefix_index_list = parent_prefix.split(".")
    # new_parent_prefix = conver_str_to_int(parent_prefix_index_list)

    if os.path.isdir(sub_item) != True:
        sub_items = getSubDir(str_folder_path + "\\" + sub_item)
        for i in sub_items:
            print "move ",
            print "\"" + str_folder_path + "\\" + sub_item + "\\" + i + "\"", 
            print "\"" + str_folder_path + "\""
            





            # print "rename ", 
            # print "\"" + str_folder_path + "\\" + sub_item + "\\" + i + "\"", 
            # # print "\"" + parent_prefix + i + "\""
            # print "\"" + conver_str_to_int((parent_prefix + i).split(".")) + i.split(".")[-2] + "." + i.split(".")[-1] + "\""


            # print conver_str_to_int((parent_prefix + i).split(".")) + i.split(".")[-2] + "." + i.split(".")[-1]
            # print "\"" + str_folder_path + "\\" + sub_item + "\\" + new_parent_prefix + i + "\""

def renameSrtName___(str_L, sPath):
    for i in str_L:
        str_Subdir = sPath + '/' + i
        if os.path.isdir(str_Subdir) == True:
            # pass
            # print str_Subdir
            renameSrtName___(getSubDir(str_Subdir), str_Subdir)
        elif i == '.DS_Store':
            # print i
            pass
        else:
            

            oldFileName = str_Subdir.split("/")[-1]
            strParePrefix = str_Subdir.split("/")[-2][0:2]
            # print oldFileName
            # print strParePrefix

            # listFileName = oldFileName.split("_")
            # strNewFileName = listFileName[1] + "." + listFileName[2] + " " + listFileName[-1]
            a = str_Subdir
            b = a.replace(str_Subdir.split('/')[-1], strParePrefix + "." + str_Subdir.split('/')[-1])

            if (os.path.exists(a) == True):
                # print a
                # print b
                command = "mv " + "'" + a + "'"  + " " + "'" + b + "'"
                print command
                os.system(command)

            time.sleep(0.001)
            

            # newFileName = 


# renameSrtName___(getSubDir(str2), str2)