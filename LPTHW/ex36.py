a = [
'\\', 
'\'', 
'\"', 
'\a', 
'\b\
', 
'\f', 
'\n\
', 
'\r', 
'\t', 
'\v']

print a
for i in a:
	# print '=====String Escape Sequences as below:====='
	print '%r' %i, '--', i
