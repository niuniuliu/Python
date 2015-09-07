import os
import sys
import time

str_RootPath = "/Users/TimLiu/Downloads/Java-tutorials-Essential-Training"

def getSubDir(str_Path):
	L = os.listdir(str_Path)
	return L

def splitdir(str_dir):
	pass

def getFile(str_L, sPath):
	for i in str_L:
		str_Subdir = sPath + '/' + i
		if os.path.isdir(str_Subdir) == True:

			getFile(getSubDir(str_Subdir), str_Subdir)
		elif i == '.DS_Store':
			pass
		else:
			# print str_Subdir
			# print str_Subdir.split('/')[-2][0:2] + "."
			# print str_Subdir.split('/')[-1].replace(". ", " ")
			# print str_Subdir.split('/')[-2][0:2] + str_Subdir.split('/')[-1]

			a = str_Subdir
			# b = a.replace(str_Subdir.split('/')[-1], str_Subdir.split('/')[-2][0:2] + "." + str_Subdir.split('/')[-1])
			b = a.replace(str_Subdir.split('/')[-1], str_Subdir.split('/')[-2][0:2] + "." + str_Subdir.split('/')[-1].replace(". ", " "))
			# print b
			if os.path.exists(str_Subdir):
				command = "mv " + "'" + str_Subdir + "'" + " " + "'" + b + "'" 
				os.system(command)
				# print command
				# print str_Subdir
				# print b

# getFile(getSubDir(str_RootPath), str_RootPath)

def moveSRTFiles():
	# Path1 = "/Users/TimLiu/Downloads/Java-tutorials-Essential-Training"
	# Path2 = "/Users/TimLiu/Downloads/Java/David Gassner/Lynda.com - 1_Java Essential Training"

	Path1 = '/Users/TimLiu/Downloads/Java-tutorials-Java-EE-Essentials-Servlets-JavaServer-Faces'
	Path2 = '/Users/TimLiu/Downloads/Java/Lynda.com - Java EE Essentials Servlets and JavaServer Faces'


	L1 = os.listdir(Path1)
	L2 = os.listdir(Path2)
	# print L1
	# print L2

	for i in L1:
		if i in L2:
			srtFolder = Path1 + '/' + i
			DestFolder = Path2 + '/' + i

			if os.path.isdir(srtFolder) == os.path.isdir(DestFolder) == True:
				# print srtFolder
				# print DestFolder
				command = "mv " + "'" + srtFolder + "'"  + "/*" + " " + "'" + DestFolder + "/" + "'" 
				print command
				# os.system(command)

moveSRTFiles()


str_RootPath1 = '/Users/TimLiu/Downloads/Java-tutorials-Java-Advanced-Training'
str_RootPath2 = '/Users/TimLiu/Downloads/Java/David Gassner/Lynda.com - 2_Java Advanced Training'

def renamesrtFiles(str_L, sPath):
	for i in str_L:
		str_Subdir = sPath + '/' + i
		if os.path.isdir(str_Subdir) == True:
			# pass
			# print str_Subdir
			renamesrtFiles(getSubDir(str_Subdir), str_Subdir)
		elif i == '.DS_Store':
			# print i
			pass
		else:
			# print str_Subdir
			# print str_Subdir.split('/')[-1].replace("0", "")
			# print str_Subdir.split('/')[-1]
			# print str_Subdir.split('/')[-2][0:2] + str_Subdir.split('/')[-1]

			a = str_Subdir
			b = a.replace(str_Subdir.split('/')[-1], str_Subdir.split('/')[-1].replace("0", ""))
			# print a
			# print b
			# b = a.replace(str_Subdir.split('/')[-1], str_Subdir.split('/')[-2][0:2] + "." + str_Subdir.split('/')[-1].replace(". ", " "))
			# # print b
			if os.path.exists(a):
				command = "mv " + "'" + a + "'" + " " + "'" + b + "'" 
				os.system(command)
				print command
				# print str_Subdir
				# print b
# print getSubDir(str_RootPath1)
# renamesrtFiles(getSubDir(str_RootPath1), str_RootPath1)

def moveSRTFile___(Path1, Path2):

	L1 = os.listdir(Path1)
	L2 = os.listdir(Path2)
	# print L1
	# print L2

	for i in L1:
		if i in L2:
			srtFolder = Path1 + '/' + i
			DestFolder = Path2 + '/' + i

			if os.path.isdir(srtFolder) == os.path.isdir(DestFolder) == True:
				# print srtFolder
				# print DestFolder
				command = "mv " + "'" + srtFolder + "'"  + "/*" + " " + "'" + DestFolder + "/" + "'" 
				print command
				os.system(command)

# moveSRTFile___(str_RootPath1, str_RootPath2)

str1 = '/Users/TimLiu/Downloads/Java/David Gassner/Lynda.com - 3_Java Database Integration with JDBC'

def renameMovieNames(str_L, sPath):
	for i in str_L:
		str_Subdir = sPath + '/' + i
		if os.path.isdir(str_Subdir) == True:
			# pass
			# print str_Subdir
			renameMovieNames(getSubDir(str_Subdir), str_Subdir)
		elif i == '.DS_Store':
			# print i
			pass
		else:
			

			oldFileName = str_Subdir.split("/")[-1]
			strParePrefix = str_Subdir.split("/")[-2][0:2]
			# print oldFileName
			listFileName = oldFileName.split("_")
			strNewFileName = listFileName[1] + "." + listFileName[2] + " " + listFileName[-1]
			a = str_Subdir
			b = str_Subdir.split('110284')[0] + strNewFileName

			if (os.path.exists(a) == True):
				# print a
				# print b
				command = "mv " + "'" + a + "'"  + " " + "'" + b + "'"
				print command
				# os.system(command)

			time.sleep(0.001)
			

			# newFileName = 

# renameMovieNames(getSubDir(str1), str1)


str2 = '/Users/TimLiu/Downloads/Java-tutorials-Java-Database-Integration-JDBC'

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