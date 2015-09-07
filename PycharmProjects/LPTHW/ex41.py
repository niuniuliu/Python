# coding=utf-8
# class X(Y)  ¡°Make a class named X that is- a Y.¡±
# class X(object): def __init__(self, J)  ¡°class X has- a __init__ that takes self and J parameters.¡±
# class X(object): def M(self, J)  ¡°class X has- a function named M that takes self and J parameters.¡±
# foo = X()  ¡°Set foo to an instance of class X.¡±
# foo.M(J)  ¡°From foo get the M function, and call it with parameters self, J.¡±
# foo.K = Q  ¡°From foo get the K attribute, and set it to Q.¡±

import random
from urllib import urlopen
import sys
import os

# WORD_URL = "http://learncodethehardway.org/words.txt"
# WORD_URL = r"file:///C:/Users/tliu/Downloads/P/P_3rd/words.txt"
currentPath = os.path.abspath(os.path.curdir)

WORD_URL = r"file:///" + currentPath + "/words.txt"

# print WORD_URL
WORDS = []

# Declare dictionary for Question. key and value
PHRASES = {
	"class %%%(%%%):": "Make a class named %%% that is-a %%%.", 
	"class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** parameters.",
	"class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.", 
	"*** = %%%()": "Set *** to an instance of class %%%.", 
	"***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.", 
	"***.*** = '***'": "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
# print 
# print len(sys.argv)
# print sys.argv
# print 

# if sys.argv = 1, question is statement
# if sys.argv = 2, question is description and need use to fill the statement.
# 
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASE_FIRST = True
	# print PHRASE_FIRST

# load up the words from the website


# Store words to WORDS array.
for word in urlopen(WORD_URL).readlines():
	# print word
	WORDS.append(word.strip())
# print WORDS

def convert(snippet, phrase):
	# Distribute different words to replace %%%, the words are unique. Then make the 
	class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
	# Get the count of ***, then pick up the word from WORDS array. Then return amount of count words.
	other_names = random.sample(WORDS, snippet.count("***"))
	results = []
	param_names = []

	for i in range(0, snippet.count("@@@")):
		# Get count of parameter.
		param_count = random.randint(1, 3)
		# Get parameter format. eg. (a, b, c)
		param_names.append(', '.join(random.sample(WORDS, param_count)))

	for sentence in snippet, phrase:
		result = sentence[:]

		# fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)
	return results

# keep going until they hit CTRL+D
try:
	while True:
		snippets = PHRASES.keys()
		random.shuffle(snippets)

		for snippet in snippets:
			phrase = PHRASES[snippet]
			question, answer = convert(snippet, phrase)
			if PHRASE_FIRST:
				question, answer = answer, question

			print question

			raw_input("> ")
			print "ANSWER: %s\n\n" % answer

except EOFError:
	print "\nBye"



# 
# from UserDict import UserDict

# class MyFirstClass():
# 	pass

# a = 1
# b = 2

# if a == b:
# 	print a, b
# else:
# 	# print a, b
# 	pass

# class FileInfo(UserDict):
# 	"""docstring for FileInfo"""
# 	def __init__(self, filename=None):
# 		UserDict.__init__(self)
# 		self["name"] = filename

# """Framework for getting filetype-specific metadata.

# Instantiate appropriate class with filename.  Returned object acts like a
# dictionary, with key-value pairs for each piece of metadata.
#     import fileinfo
#     info = fileinfo.MP3FileInfo("/music/ap/mahadeva.mp3")
#     print "\\n".join(["%s=%s" % (k, v) for k, v in info.items()])

# Or use listDirectory function to get info on all files in a directory.
#     for info in fileinfo.listDirectory("/music/ap/", [".mp3"]):
#         ...

# Framework can be extended by adding classes for particular file types, e.g.
# HTMLFileInfo, MPGFileInfo, DOCFileInfo.  Each class is completely responsible for
# parsing its files appropriately; see MP3FileInfo for example.
# """
# import os
# import sys
# from UserDict import UserDict

# def stripnulls(data):
#     "strip whitespace and nulls"
#     return data.replace("\00", "").strip()

# class FileInfo(UserDict):
#     "store file metadata"
#     def __init__(self, filename=None):
#         UserDict.__init__(self)
#         self["name"] = filename

# class MP3FileInfo(FileInfo):
#     "store ID3v1.0 MP3 tags"
#     tagDataMap = {"title"   : (  3,  33, stripnulls),
#                   "artist"  : ( 33,  63, stripnulls),
#                   "album"   : ( 63,  93, stripnulls),
#                   "year"    : ( 93,  97, stripnulls),
#                   "comment" : ( 97, 126, stripnulls),
#                   "genre"   : (127, 128, ord)}

#     def __parse(self, filename):
#         "parse ID3v1.0 tags from MP3 file"
#         self.clear()
#         try:                               
#             fsock = open(filename, "rb", 0)
#             try:                           
#                 fsock.seek(-128, 2)        
#                 tagdata = fsock.read(128)  
#             finally:                       
#                 fsock.close()              
#             if tagdata[:3] == "TAG":
#                 for tag, (start, end, parseFunc) in self.tagDataMap.items():
#                     self[tag] = parseFunc(tagdata[start:end])               
#         except IOError:                    
#             pass                           

#     def __setitem__(self, key, item):
#         if key == "name" and item:
#             self.__parse(item)
#         FileInfo.__setitem__(self, key, item)

# def listDirectory(directory, fileExtList):                                        
#     "get list of file info objects for files of particular extensions"
#     fileList = [os.path.normcase(f)
#                 for f in os.listdir(directory)]           
#     fileList = [os.path.join(directory, f) 
#                for f in fileList
#                 if os.path.splitext(f)[1] in fileExtList] 
#     def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):      
#         "get file info class from filename extension"                             
#         subclass = "%sFileInfo" % os.path.splitext(filename)[1].upper()[1:]       
#         return hasattr(module, subclass) and getattr(module, subclass) or FileInfo
#     return [getFileInfoClass(f)(f) for f in fileList]                             

# # if __name__ == "__main__":
# #     for info in listDirectory("/music/_singles/", [".mp3"]): (1)
# # 		print "\n".join(["%s=%s" % (k, v) for k, v in info.items()])
# # 		print


