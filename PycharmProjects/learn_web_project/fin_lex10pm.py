import sys
import re
import time
import dictionary
import copy
import Config
import fin_parser

print '\t\t\t_Semantics Milestone_\nPartner: Praveen Lobo (email:plobo@clemson.edu)\nPartner: Niha Somisetty(email:vsomise@clemson.edu)'
localtime=time.asctime(time.localtime(time.time()))
print "Time: ", localtime,"\nInitiating File Reading....\n"

multiline_comment = False

handle,tstack,ignore,tempravi=[],[],[],[]
panicflag=False										 
		
def lexy(f):		
	a=f.readlines()
	global multiline_comment
	pline=[];
	regex=re.compile(r"""(" ")|
					([/][*])|											   ##Starting of a multiline
					([^"|^/*]*[\*][\/])|	
					([A-Z]+)|											   ##Handling resererve keywords
					([a-z]+[a-zA-Z0-9_]*)|								  ##Handling keywords
					([0-9]+[.][0-9]+)| ## handling reals
					([0-9]+)|					   ## handling integers
					(//.*)|										 ## handling single line comments
					([=][=]|[!][=]|[<][=]|[>][=]|[<][-]|[:][:])| ## handling multiline comments
					([\;]|[\:]|[\[]|[\]]|[\,[\(]|[\,]|[\)]|[\<]|[\>]|[\!]|[\+]|[\-]|[\*]|[\/]|[\{]|[\}]|[\&]|[\|])|																				 ## handling single ascii
					([\']|[\.]|[\?]|[\\]|[\_]|[\^]|[\%]|[\$]|[\@]|[\~]|[\`]|[\=])|##handling invalid ascii
					(".+?")| ## handling strings
					([#][#]([+|\-][0-9])*.*)""",re.X) 
	
	for line in a:
		pline=[]
		
		if Config.flags[1]==True: 
			print "INPUT LINE: ",line[:80]
		
		for x in re.finditer(regex, line[:80]): 
			if multiline_comment == True:
				regx = re.compile(r'(.*?)([*][/])')
				if regx.search(line[:80]):
					multiline_comment = False
		
			else:
				if x.group(2):
					multiline_comment = True
		
				elif x.group(1):
					break
							
				elif x.group(4):
					if x.group(4) in dictionary.dict_token:
						if Config.flags[2]==True:
							print '\t\t\tToken value of',x.group(4), dictionary.dict_token[x.group(4)]
						fin_parser.parse((dictionary.dict_token[x.group(4)],x.group(4)))
					elif x.group(4) not in dictionary.dict_token:
						print '\t\t\tInvalid reserve keyword',x.group(4)
										
		
									
				elif x.group(5):
					if len(x.group(5))>16:
						print '\t\t\tInvalid keyword length',x.group(5)
					else:
						if Config.flags[2]==True:
							print '\t\t\tToken value of',x.group(5),57 
						fin_parser.parse((57,x.group(5)))
			  
				elif x.group(6):
					a=x.group(6)
					l=len(x.group(6))
					if '-' in a:
						if l-2>7:
							print '\t\t\tReal length exceeds 9 digits',x.group(6)
						else:   
							if Config.flags[2]==True:
								print '\t\t\tToken value of',x.group(6), 63
							fin_parser.parse((63,x.group(6)))
					else:
						if l-1>7:
							print '\t\t\tReal length exceeds 9 digits',x.group(6)
						else:
							if Config.flags[2]==True:
								print '\t\t\tToken value of',x.group(6), 63
							fin_parser.parse((63,x.group(6)))
		
				elif x.group(7):
					a=x.group(7)
					l=len(x.group(7))
					if '-' in a:						
						if l-1>9:
							print '\t\t\tInteger length exceeds 9 digits',x.group(7)
						else:
							if Config.flags[2]==True:
								print '\t\t\tToken value of',x.group(7), 63
							fin_parser.parse((63,x.group(7)))
								
					else:
						if l>9:
							print '\t\t\tInteger length exceeds 9 digits',x.group(7)
						else:
							if Config.flags[2]==True:
								print '\t\t\tToken value of',x.group(7), 63
							fin_parser.parse((63,x.group(7)))
				elif x.group(8):
					break
		
				elif x.group(9):
					if Config.flags[2]==True:
						print '\t\t\tToken value of',x.group(9), dictionary.dict_token[x.group(9)]
					fin_parser.parse((dictionary.dict_token[x.group(9)],x.group(9)))
					
				elif x.group(10):
					if x.group(10) in dictionary.dict_token:
						if Config.flags[2]==True:
							print '\t\t\tToken value of',x.group(10), dictionary.dict_token[x.group(10)]
						fin_parser.parse((dictionary.dict_token[x.group(10)],x.group(10)))
							
				elif x.group(11):
					print '\t\t\tInvalid ascii character ',x.group(11), 'ascii value is',ord(x.group(11))
					
				elif x.group(12):
					if Config.flags[2]==True:
						print '\t\t\tToken value of',x.group(12), 78
					fin_parser.parse((78,x.group(12)))
					
				elif x.group(13):
					regx = re.compile (r'([+-])([0-9]+)')
					iterator = re.finditer(regx,x.group(13))
					for matchedobj in iterator:
						if matchedobj.group(1)=='+':
							print "Setting flag", matchedobj.group(2),"\n"							
							Config.flags[int(matchedobj.group(2))] = True
						else:
							print "Unsetting flag", matchedobj.group(2),"\n"							
							Config.flags[int(matchedobj.group(2))] = False

def main():
	fin_parser.readgrammar()		
	f=open('./callByValue.txt','r')
	lexy(f)
	f.close()
	fin_parser.parse_last()
	print "\nParsing Successful!"

main()
