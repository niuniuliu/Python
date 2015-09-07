# file_name = "/Users/liutim/Projects/Python_Learn/LPTHW/aaa"
# bigFile= open(file_name,'w')
# bigFile.seek(1024*1024*1024*1) 
# bigFile.write('test\n')
# bigFile.write('test\n')
# bigFile.write('test\n')
# bigFile.write('test\n')
# bigFile.write('test\n')
# bigFile.close()
# print "ALL down !"



file_name = "/Users/liutim/Projects/Python_Learn/LPTHW/aaa"
bigFile= open(file_name,'r')
a = bigFile.readlines()

print len(a)

for i in a:
	print len(i)
