import os

# str_RootPath1 = '/Users/TimLiu/Downloads/Java-tutorials-Java-EE-Essentials-Servlets-JavaServer-Faces'
# str_RootPath1 = '/Users/TimLiu/Downloads/Developer-Programming-Languages-tutorials-Building-Web-Services-Java-EE'

# str_RootPath1 = '/Users/TimLiu/Downloads/Java/Lynda.com - Building Web Services with Java EE'


str_RootPath1 = '/Users/TimLiu/Downloads/Temp/PowerShell 3.0 for Administrators {AceMerlin}'
# str_RootPath1 = '/Users/TimLiu/Downloads/Java-tutorials-Java-Database-Integration-JDBC'
# str_RootPath2 = '/Users/TimLiu/Downloads/Java/David Gassner/Lynda.com - 3_Java Database Integration with JDBC'


# def getCurrentMovFilelist(strPath):
# 	org_List = os.listdir(strPath)

orgFileList = []

def getSubFolderFiles(strPath):
	org_List = os.listdir(strPath)

	for i in org_List:
		# print i

		# str_Subdir = strPath + '/' + i
		# if os.path.isdir(str_Subdir) == True:
		# 	# print str_Subdir.split('/')[-1].split(". ")[0]
		# 	a = str_Subdir.split('/')[-1].split(". ")[0]
		# 	b = int(a) + 1
		# 	# print "0" + str(b) + ". " + str_Subdir.split('/')[-1].split(". ")[1]
		# 	a = "0" + str(b) + ". " + str_Subdir.split('/')[-1].split(". ")[1]
		# 	b = strPath + '/' + a
		# 	a = str_Subdir
		# 	# print a
		# 	# print b
		# 	if os.path.exists(a) == True:
		# 		# print a
		# 		# print b
		# 		command = "mv " + "'" + a + "'"  + " " + "'" + b + "'" 
		# 		print command
		# 		# os.system(command)



		# str_Subdir = strPath + '/' + i
		# if os.path.isdir(str_Subdir) == True:
		# 	# pass
		# 	# print str_Subdir
		# 	getSubFolderFiles(str_Subdir)
		# elif i == '.DS_Store':
		# 	# print i
		# 	pass
		# else:
		# 	# orgFileList.append(str_Subdir)
		# 	# print strPath
		# 	a = str_Subdir.split('/')[-2][0:2]
		# 	b = a + "_" + str_Subdir.split('/')[-1].replace(". ", "-")

		# 	b = strPath + '/' + b
		# 	a = str_Subdir
		# 	# print a
		# 	if os.path.exists(a) == True:
		# 		# print a
		# 		# print b
		# 		command = "mv " + "'" + a + "'"  + " " + "'" + b + "'" 
		# 		print command
		# 		# os.system(command)



		str_Subdir = strPath + '/' + i
		if os.path.isdir(str_Subdir) == True:
			# pass
			# print str_Subdir
			getSubFolderFiles(str_Subdir)
		elif i == '.DS_Store':
			# print i
			pass
		else:
			a = ''
			b = ''

			# print str_Subdir
			if (".srt" in str_Subdir):
				a = str_Subdir
				# print a
				# print a.split('/')[-1][0:5]
			elif (a.split('/')[-1][0:5] in str_Subdir) and (".mp4" in str_Subdir):
				b = str_Subdir
				# print b.split('/')[-1][0:5]
				print b
				print a




getSubFolderFiles(str_RootPath1)
# for i in orgFileList:
# 	print i
# 	a = i.split('/')[-2][0:2]




# def moveMOVFile___(Path1, Path2):

# 	L1 = os.listdir(Path1)
# 	L2 = os.listdir(Path2)
# 	# print L1
# 	# print L2

# 	for i in L1:
# 		if i in L2:
# 			srtFolder = Path1 + '/' + i
# 			DestFolder = Path2 + '/' + i

# 			if os.path.isdir(srtFolder) == os.path.isdir(DestFolder) == True:
# 				# print srtFolder
# 				# print DestFolder
# 				command = "mv " + "'" + srtFolder + "'"  + "/*" + " " + "'" + DestFolder + "/" + "'" 
# 				print command
# 				# os.system(command)


# # moveMOVFile___(str_RootPath1, str_RootPath2)
# # getCurrentMovFilelist(str_RootPath2)

# # getSubFolderFiles(str_RootPath1)
# # orgFileList_Mov = orgFileList

# # for i in orgFileList:
# # 	print i

# # orgFileList = []

# # getSubFolderFiles(str_RootPath2)
# # getSubFolderFiles(str_RootPath1)

# # for (i = 0; i < len(orgFileList); i++):
# # 	print orgFileList[i]
# 	# i_list = i.split("/")
	
# 	# print i_list[-1]

# # for i in orgFileList_Mov:
# # 	print i
# # 	# i_list = i.split("/")
# # 	# print i_list[-1]



# # for (i,j) in zip(orgFileList, orgFileList_Mov):
# # 	# print i.split('JDBC/')[1]
# # 	# print j.split('JDBC/')[1]

# # 	x = i.split('JDBC/')[0] + 'JDBC/' + j.split('JDBC/')[1]
# # 	x = x.replace('.srt', '.mov')
# # 	if os.path.exists(i):
# # 		command = "mv " + "'" + i + "'" + " " + "'" + x + "'" 
# # 		# os.system(command)
# # 		print command


# Path1 = "/Users/TimLiu/Downloads/Java-tutorials-Java-Database-Integration-JDBC"
# Path2 = "/Users/TimLiu/Downloads/Java/David Gassner/Lynda.com - 3_Java Database Integration with JDBC"
# strPath1 = '/Users/TimLiu/Downloads/Java-tutorials-XML-Integration-Java'
# strPath2 = '/Users/TimLiu/Downloads/Java/David Gassner/Lynda.com - 5_XML Integration with Java'

# def moveSRTFiles(Path1, Path2):

# 	L1 = os.listdir(Path1)
# 	L2 = os.listdir(Path2)
# 	# print L1
# 	# print L2

# 	for i in L1:
# 		if i in L2:
# 			srtFolder = Path1 + '/' + i
# 			DestFolder = Path2 + '/' + i

# 			if os.path.isdir(srtFolder) == os.path.isdir(DestFolder) == True:
# 				# print srtFolder
# 				# print DestFolder
# 				command = "mv " + "'" + srtFolder + "'"  + "/*" + " " + "'" + DestFolder + "/" + "'" 
# 				print command
# 				os.system(command)

# # moveSRTFiles(Path1, Path2)
# moveSRTFiles(strPath1, strPath2)



# strPath_001 = '/Users/TimLiu/Downloads/Java/David Gassner/Lynda.com - 5_XML Integration with Java'

# for i in os.listdir(strPath_001):
# 	a = strPath_001 + "/" + i
# 	b = strPath_001 + "/0" + i

# 	if os.path.isdir(a) == True:
# 		# print a
# 		# print b
# 		command = "mv " + "'" + a + "'"  + " " + "'" + b + "'" 
# 		# print command
# 		# os.system(command)



