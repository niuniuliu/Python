# import random
# a = 'a  a  ds ss   \n \t'
# b = 'a, b, c, d, e, f, g, h, i, g'
# b = b.split(', ')
# # b = 'b'

# # print "%r" %a.capitalize()
# # print "%r" %a.strip('a \t s \n')

# # print a.count('s')

# res = random.sample(b, a.count('s'))
# # print type(res), [i for i in dir(res)]


# for y in res:
# 	# print y.capitalize()
# 	pass

# # print "%r" %[x.capitalize() for x in res]
# # z = [x.capitalize() for x in res]
# # print z

# # ', '.join(random.sample(WORDS, param_count))

# print str(random.randint(1, 5))
# print ', '.join([str(random.randint(1, 5)), str(random.randint(1, 5))])

# print ", ".join(['abc', 'a'])

# # param_names.append(', '.join(random.sample(WORDS, param_count)))


# PHRASES = {
# 	# "class %%%(%%%):": "Make a class named %%% that is-a %%%.", 
# 	# "class %%%(object):\n\tdef __init__(self, ***)": "class %%% has-a __init__ that takes self and *** parameters.",
# 	# "class %%%(object):\n\tdef ***(self, @@@)": "class %%% has-a function named *** that takes self and @@@ parameters.", 
# 	# "*** = %%%()": "Set *** to an instance of class %%%.", 
# 	# "***.***(@@@)": "From *** get the *** function, and call it with parameters self, @@@.", 
# 	# "***.*** = '***'": "From *** get the *** attribute and set it to '***'."
# 	'a':'a1',
# 	'aa':'aa1',
# 	'aaa':'aaa1',
# 	'a4':'a41'

# }

# snippets = PHRASES.keys()
# # print snippets
# random.shuffle(snippets)
# # print snippets

# for x in snippets:
# 	key = x
# 	value = '' + PHRASES[x]


# 	for sentence in key, value:
# 		# result = sentence[:]
# 		print sentence

# import sys
# r = sys.registry

# for k in r:
# 	print k
# 	print r[k]


import sys
from java.io import FileOutputStream

class UppercaseFileOutputStream(FileOutputStream):
    def write_upper(self, text):
        text = text.upper()
        self.write(text)

def test(outfilename):
    fos = UppercaseFileOutputStream(outfilename)
    for idx in range(10):
        fos.write_upper('This is line # %d\n' % idx)
    fos.close()
    infile = open(outfilename, 'r')
    for line in infile:
        line = line.rstrip()
        print 'Line: %s' % line

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print 'usage: extend_fileoutputstream.py <infilename>'
        sys.exit(1)
    test(args[0])

if __name__ == '__main__':
    main()