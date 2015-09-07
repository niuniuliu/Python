# # --coding=utf-8--

from jpype import *
print getDefaultJVMPath()
# startJVM(getDefaultJVMPath())
# java.lang.System.out.println("hello world")
# shutdownJVM()

# import this
# # s=this.s
# d = {}
# for c in (65, 97):
#     for i in range(26):
#         d[chr(i+c)] = chr((i+13) % 26 + c)

# print dir(this.s)
# print d

# print 'python 之禅' 
# print "".join([d.get(c, c) for c in s])

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# browser = webdriver.Chrome()

# browser.get('http://www.bing.com')
# # br = dir(browser)
# # help(browser)
# # for i in br:
# #     print i
# # print (browser.title)

# assert u'Bing' in browser.title
# # assert u'Yahoo' in browser.title

# print browser.window_handles

# elem = browser.find_element_by_name('q')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
# elem.click()
# elem.getatt


# e = br.find_element_by_name('kw') 
# elements = dir(elem)

# for i in elements:
#     print i
# help(elem)

# browser.quit()



# from selenium import webdriver

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com/')


# import calendar

# Nov = calendar.month(2014, 11)
# Dec = calendar.month(2014, 12)

# print Nov
# print Dec

# from apihelper import info
# li = []
# info(li)


'''
#coding=utf-8
import re
import os
pathinfo = 'C:\\Users\\tliu\\Downloads\\FireFox\\LP4E-examples'

# print os.listdir(pathinfo)
filelist = os.listdir(pathinfo)
newlist = []
def match():
    for i in filelist:
        regexp = "(ch)(.*?)(.txt)"
        r = re.search(regexp, i)
        if r:
            i.replace('.txt', '.py')
            newlist.append(i)
    return newlist

fileforrename = match()

# print fileforrename

# print pathinfo + '\ch03.txt'
# print os.path.exists(pathinfo + '\ch03.txt')
def renamefiles():
    for i in fileforrename:
        j = i.replace('.txt', '.py')
        oldfilepath = pathinfo + '\\' + i
        newfilepath = pathinfo + '\\' + j
        if os.path.exists(pathinfo + '\\' + i):
            os.rename(oldfilepath, newfilepath)



renamefiles()
'''

'''
a = 0
for i in range(24):
    a = i + a
print a+24

#coding=utf-8
'''
'''
Author: TimLiu
Create Time: 09_10_14
Function: Mockup 1L TRAN&POSIT raw data
Smallest Unit: MB

'''
'''
import os
import time

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
    file_name = "C:\\APDS\\Test_DATA\\10087_TRANS_" + strDate + "_LOC.TXT"
    
    # Data header
    header = readAppendData("C:\\APDS\\Test_DATA\\TRANS_Header.TXT")
    
    # Data Content
    contentText = readAppendData("C:\\APDS\\Test_DATA\\TRANS.TXT")
    
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

# MockupPOSITData only support create a new file.
def MockupPOSITData(size, strDate):
    # file name to be created
    file_name = "C:\\APDS\\Test_DATA\\10087POSIT" + strDate + "_043052.txt"
    
    # Data header
    header = readAppendData("C:\\APDS\\Test_DATA\\POSIT_Header.TXT")
    
    # Data Content
    contentText = readAppendData("C:\\APDS\\Test_DATA\\POSIT.TXT")

    # Data TAILER
    tailer = readAppendData("C:\\APDS\\Test_DATA\\POSIT_Tailer.TXT")
    
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
    Datasize = 700
    strDate = '20140807'
    MockupTRANData(Datasize/1024.000000000, strDate)
    MockupPOSITData(Datasize/1024.000000000, strDate)


'''
# import time

# def creatfilesize(n):
#     local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
#     file_name = "C:\\APDS\\Test_DATA\\"+str(local_time)+".txt"
#     bigFile= open(file_name, 'w')
#     bigFile.seek(1024*1024*1024*n) 
#     bigFile.write('test')
#     #bigFile.write("test")
#     bigFile.close()
#     print "ALL down !"

# if __name__ == '__main__':
#     creatfilesize(0.00099999)

#coding = utf-8
#!/usr/bin/env python

# import os
# import time

# def create_file_size(size):
#     size *= 1024 * 1024*1024
#     print size 
#     local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
#     file_name = "C:\\APDS\\Test_DATA\\"+str(local_time)+".txt"    
#     with open(file_name, 'w') as f:
#         note = 'Test File Contents: '
#         i = 0
#         fsize = 0
#         while True:
#             i += 1
#             text = note + str(i) + "\n"
#             f.write(text)
#             fsize += len(text)
#             if fsize >= size:
#                 break
#     print "ALL down!"

# if __name__ == '__main__':
#     # size = input("input you's size:")
#     create_file_size(0.0001)




'''
def creatfilesize(n):
    local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    file_name = "E:\\testFile\\"+str(local_time)+".txt"
    bigFile= open(file_name, 'w')
    bigFile.seek(1024*1024*1024*n) 
    bigFile.write('test')
    #bigFile.write("test")
    bigFile.close()
    print "ALL down !"

if __name__ == '__main__':
    
    creatfilesize(n)


#coding = utf-8
#!/usr/bin/env python

import os
import time

def create_file_size(size):
    size *= 1024 * 1024*1024
    print size 
    local_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    file_name = "E:\\testFile\\"+str(local_time) + ".txt"
    with open(file_name, 'w') as f:
        note = 'Test File Contents: '
        i = 0
        fsize = 0
        while True:
            i += 1
            text = note + str(i) + "\n"
            f.write(text)
            fsize += len(text)
            if fsize >= size:
                break
    print "ALL down!"

if __name__ == '__main__':
    size = input("input you's size:")
    create_file_size(size)
'''

#coding=utf-8
'''
Created on 2012-5-29

@author: lianghui
'''
'''
import os
import time


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

def file_size(size):
    local_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
    file_name = "E:\\testFile\\"+str(local_time)+".txt"
    f = open(file_name,'ab')
    note = "111"
    for i in range(1,99999999):
        f.write(note+str(i))
        filesize = float(getfile_att(file_name,'fsize')["fsize"])
        if filesize/1024/1024/1024 >= size:
            break
        else:
            continue    
    f.close()
    print "ALL down!"

if __name__ == '__main__':
    size = input("input you's size:")
    file_size(size)
print file_size






a = ()
a1 = ('1111')
a2 = ('a2',)

print len(a)
print len(a1)
print len(a2)


go = ['abc', 'b', 'c', '2', 2]

for i in go:
    i = str(i)
    if i.startswith('a'):
        print i


print "Hi"

my_num = 5

print range(5)
'''
"""
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()


"""
"""
     Boolean Operators
------------------------      
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""
# board = []
# for i in range(0,5):
#     board.append(['O', 'O', 'O', 'O', 'O']) 
    
# print board
'''
board = []
for i in range(0,5):
    board.append( ["O"] * 5) 
    
def print_board(board):
    for row in board:
        print " ".join(row)
        
print_board(board)        

'''
'''
from random import randint

board = []
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


for turn in range(4):    
    print "Let's play Battleship!"
    print_board(board)
    print "Turn"
    
    
    ship_row = random_row(board)
    ship_col = random_col(board)
    print '######' + str(ship_row)
    print '######' + str(ship_col)

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    elif (board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)
        if guess_row not in range(5) or guess_col not in range(5) :
            print "Oops, that's not even in the ocean."
        else:
            print str(guess_row) + " , " + str(guess_col)
    
    # Print (turn + 1) here!
    print turn + 1
    '''
# import psutil
# print(psutil.Process(pid).cpu_percent())



# from  datetime  import  *  

# time1 = datetime.today()

# time2 = datetime.today()

# print time1 - time2

'''
import pyodbc
from  datetime  import  *  
import time


def SQLQuery(sql, withTitle, serverName, databaseName, userName, password):

    out = []

    connStr = ''
    connStr += 'DRIVER={SQL Server};'
    connStr += 'SERVER=' + serverName + ';'
    connStr += 'DATABASE=' + databaseName + ';'
    connStr += 'UID=' + userName + ';'
    connStr += 'PWD=' + password

    try:
        conn = pyodbc.connect(connStr)
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        if withTitle and len(rows) > 0:
            out.append([str(item[0]) for item in cursor.description])
        for row in rows:
            out.append([str(item) for item in row])
    except Exception as e:
        print(e)

    return out

# SQLQuery(sqlStr, includeHeader, sep, serverName, databaseName, userName, password):
mysql = "SELECT *  FROM [PDSCoreDB].[dbo].[AppSetting] WHERE ConfigKey='WorkflowsEnabled'"
withTitle = datetime.today()
serverName = "PDSQA-12-DB.ctp.dev.com"
databaseName = "PDSCoreDB"
userName = 'sa'
password = 'Sequoia2012'
filename = "C:\APDS\ADS-1977\Result.log"



seconds = 0
while (seconds < 20):
    Result = SQLQuery(mysql, withTitle, serverName, databaseName, userName, password)
    fp = file(filename, "a")
    # print(line)
    # print "Start : %s" % time.ctime()
    fp.write("Start : %s" % time.ctime() + "\n")
    # print Result
    fp.write(str(Result) + "\n")
    time.sleep( 2 )
    fp.close()
    seconds += 1

    # print "End : %s" % time.ctime()




list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

# for index, item in enumerate(list_a):
#     print index+1, item

# for a, b in zip(list_a, list_b):
    # Add your code here!
    # print a, b
    

fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
i = 1
while(i < 5):
    for f in fruits:
        if f == 'tomato':
            print 'A tomato is not a fruit!' # (It actually is.)
            break
        print 'A', f
    i += 1
    if i == 3:
        break
else:
    print 'A fine selection of fruits!'
'''

# print type(7.0)
# print 0.0 == 0.000000


# def is_prime(x):
#     if x >= 2:
#         for n in range(x)[1:]:
#             if x % n == 0:
#                 return False
#             else:
#                 return True
#     else:
#         return False
        
# # print is_prime(2)


# def isPrime(num):
#     i = 2
#     while i < num:
#         if 0 == (num%i):
#             return False        
#         else:
#             i = i + 1
#     return True

# print isPrime(3)
'''


import math

def median(lst_numbers):
    lst_numbers = sorted(lst_numbers)
    if len(lst_numbers) % 2 == 0:
        num1 = int(math.floor(len(lst_numbers)/2)) - 1
        num2 = int(num1) + 1
        print lst_numbers[num1]
        print lst_numbers[num2]
        return (lst_numbers[num1] + lst_numbers[num2])/2
    else:
        return lst_numbers[len(lst_numbers)/2]

print median([4,5,5,4])

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
    return variance / len(scores)
        
print grades_variance(grades)


for number in range(5):
    print number,
print
d = { "name": "Eric", "age": 26 }
for k in d:
    print k, d[k],
    print 
print
for letter in "Eric":
    print letter,  # note the comma!



evens_to_50 = [i 
for i in range(51)
 if i % 2 == 0]
print evens_to_50


c = ['C' for x in range(5) if x < 3]
print c

cubes_by_four = ['C' for x in range(1,11) if x**3 % 4 == 0]

print cubes_by_four

print 2**3


to_21 = range(1, 22)

odds = to_21[::2]
print odds
middle_third = to_21[8:15]
print middle_third

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist), 'items to purchase.'

print 'These items are:',
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist

print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist '''



