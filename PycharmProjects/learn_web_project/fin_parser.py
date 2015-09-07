import Config
import dictionary
import copy
import fin_semantics

tokenl,reductionl,matrix,stack,handle=[],[],[],[],[]
ignore = []
panicflag = False

def readgrammar():
	f=open('./spfile.txt','r')
	f.readline()

	Config.flags[1]=True
	
	x=""
	while True:
		global tokenl
		tokenl.append((f.readline()).strip())
		if tokenl[-1]=='real':
			break
		   
	while True:
		global reductionl
		x=f.readline()
		if '000' in x:
			break
		y=x.split()
		reductionl.append(y)
	
	while x:
		global matrix
		x=x.strip()
		matrix.append(list(x))
		x=f.readline()
		
	f.close()
	
def convert(dict_token,x):
	for k in dict_token:
		if dict_token[k] == x:
			return k

def lconvert(dict_token,y):
	stri=""
	for i in y:
		for k in dict_token:
			if dict_token[k] == int(i):
				stri=stri+" "+k
	return stri

def analyze_semantics(reduction_number):
#	print ("Analyzing semantics for reduction number " + str(reduction_number))
	func = getattr(fin_semantics, "analyze_production_" + str(reduction_number), None)
	if callable(func):
	    func()
	else:
	    pass
	   
def print_semantic_stack(position):
    if Config.flags[12]:
        list = []
        for i in range(len(fin_semantics.semantic_stack)):
            list.append(fin_semantics.semantic_stack[i])
        for i in range(1, len(list)):
            list.insert(i*2-1, '|')
        printstring = "\t\tSemantic Stack"+position+":"
        print printstring,''.join(list)

def parse(tokentuple):
	global tflag,stack,reductionl,tokenl,handle,redindx,tstack,panicflag,ignore,tempravi
	token = tokentuple[0]

	if Config.flags[9]==True:
		print "Input token: ",convert(dictionary.dict_token,token)

	if not stack:
		stack.append(token)
		fin_semantics.semantic_stack.append(tokentuple[1])

	else:   
		if panicflag == True:
			if token == 59:
				set1=set(stack)
				set2=set(tempravi)
				unmatched=set1.symmetric_difference(set2)
				unmatchedl=list(unmatched)
				print "TOKENS POPPED FROM STACK: ",lconvert(dictionary.dict_token,unmatchedl)
				stack = []

				stack=copy.deepcopy(tempravi)
				ignore.append(token)

				set2=set(stack)
				print "IGNORED TOKENS: ",lconvert(dictionary.dict_token,ignore),"\n"
				panicflag=False
				ignore = []
				del fin_semantics.semantic_stack[len(stack):]
				   
			else:
				ignore.append(token)
				
		else:		
			tokenx=stack[-1]
			tokeny=token
			global symbol,matrix,redindex
			
			if Config.flags[9]==True:
				print "Top of the stack is: ",convert(dictionary.dict_token,stack[-1])
				print "Relation: ",symbol,"\n"
			
			if Config.flags[8]==True:
				print 'STACK BEFORE REDUCTION: ',lconvert(dictionary.dict_token,stack),"\n"
			
			symbol=matrix[tokenx-1][tokeny-1]
			
			if symbol == '0':
				ignore.append(token)
				print "CHARACTER PAIR ERROR BETWEEN",convert(dictionary.dict_token,tokenx),"and ",convert(dictionary.dict_token,tokeny)
				panicflag=True
									
			if ((symbol == '1') or (symbol == '3')):
				stack.append(token)
				fin_semantics.semantic_stack.append(tokentuple[1])
											
			if symbol == '2':
				reduction_found = False
				handle.insert(0,stack.pop())
				
				
				if not stack:
					symbol='2'
				else:
					lh=handle[0]
					ts=stack[-1]
					symbol=matrix[ts-1][lh-1]
					if Config.flags[9]==True:
						print "Top of the stack is: ",convert(dictionary.dict_token,stack[-1])
						print "Relation: ",symbol,"\n"
					if symbol == '0':
						print "CHARACTER PAIR ERROR BETWEEN",convert(dictionary.dict_token,tokenx),"and ",convert(dictionary.dict_token,tokeny)
						panicflag=True
						
				
				while symbol == '1':
					handle.insert(0,stack.pop())
					if not stack:
						symbol = '2'
						break
					
					
					else:
						lh=handle[0]
						ts=stack[-1]
						symbol=matrix[ts-1][lh-1]
						
						if Config.flags[9]==True:
							print "Top of the stack is: ",convert(dictionary.dict_token,stack[-1])								
							print "Relation: ",symbol,"\n"
						
						if symbol == '0':
							print "CHARACTER PAIR ERROR BETWEEN",convert(dictionary.dict_token,tokenx),"and ",convert(dictionary.dict_token,tokeny)
							panicflag=True
				   
				reductioni=0
				
				for inlist in reductionl:
					reductioni=reductioni+1
					if len(handle) == int(inlist[0]):
							
						inlist = map(int,inlist)
						if handle == inlist[1:-1]:
							print_semantic_stack("(before)")
							if Config.flags[10]==True:
								print "MATCHED HANDLE IS: ",lconvert(dictionary.dict_token,handle)
								
							if Config.flags[7]==True:
								print "REDUCTION # :", reductioni, " ",convert(dictionary.dict_token,inlist[-1]),"--->",lconvert(dictionary.dict_token,handle)
								
							# Semantics
							analyze_semantics(reductioni)

							stack.append(inlist[-1])
							#fin_semantics.semantic_stack.append(convert(dictionary.dict_token,inlist[-1]))

							if Config.flags[8]==True:
								print "STACK AFTER REDUCTION: ", lconvert(dictionary.dict_token,stack)
							
							if int(stack[-1]) == 6:										
								tempravi = []
								tempravi=copy.deepcopy(stack)

							if int(stack[-1]) == 23:								 
								tempravi = []
								tempravi=copy.deepcopy(stack)
							handle=[]
							reduction_found = True
							   
				if reduction_found == True:
					del fin_semantics.semantic_stack[len(stack):]
					print_semantic_stack("(after)")
					parse((token,tokentuple[1]))
				else:   
					print "Handle not matched!!!!!!!!!!!!!!!!!!!!!!!!!!!!"


				  
			
def parse_last():
	global stack,reductionl,handle
	handle.insert(0,stack.pop())
	if Config.flags[8]==True:
		print 'STACK BEFORE REDUCTION: ',lconvert(dictionary.dict_token,stack),"\n"
	if not stack:
		symbol='2'
	else:
	  lh=handle[0]
	  ts=stack[-1]
	  symbol=matrix[ts-1][lh-1]
	  if symbol == '0':
			panicflag=True
	
	while symbol == '1':
	  handle.insert(0,stack.pop())
	  if not stack:
		symbol = '2'
		break
	  
	  
	  else:
		lh=handle[0]
		ts=stack[-1]
		symbol=matrix[ts-1][lh-1]
		if symbol == '0':
				panicflag=True

	
	for inlist in reductionl:
	  if len(handle) == int(inlist[0]):
		 
		inlist = map(int,inlist)
		if handle == inlist[1:-1]:
			if Config.flags[10]==True:
			  print "MATCHED HANDLE IS: ",lconvert(dictionary.dict_token,handle)
				
			stack.append(inlist[-1])
			fin_semantics.semantic_stack.append(convert(dictionary.dict_token,inlist[-1]))
			if Config.flags[7]==True:
			  print "REDUCTION # : 1", " ",convert(dictionary.dict_token,inlist[-1]),"--->",lconvert(dictionary.dict_token,handle),"\n"
			if Config.flags[8]==True:
			  print "STACK AFTER REDUCTION: ", lconvert(dictionary.dict_token,stack)
		
			handle=[]
	analyze_semantics(1)	
	fin_semantics.print_global_symbol_table()
