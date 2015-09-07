import Config
from pragy import*
label_stack=[]
semantic_stack = []
symbol_table = {}
local_symbol_table = {}
in_proc_flag = False
current_proc_name = ''
irinteger = -1
irreal = -1
breal = -1
irlabel = 0
loop_stack = []
for_counter=0
procedure_start = 0

def insert_into_symbol_table(symbol,table_entry):
	global in_proc_flag, current_proc_name
	if in_proc_flag == False:
		if symbol_table.has_key(symbol):
			print "\t\tSEMANTICS ERROR:", symbol, "declared more than once!"
		else:
			symbol_table[symbol] = table_entry
	else:
		if local_symbol_table[current_proc_name].has_key(symbol):
			print "\t\tSEMANTICS ERROR:", symbol, "declared more than once!"
		else:
			local_symbol_table[current_proc_name][symbol] = table_entry
	if Config.flags[15] == True:
		print_st_entry(table_entry)
		
def print_local_symbol_table():
	global local_symbol_table
	if Config.flags[14] == True:
		print "\t\tLocal ST for procedure " + current_proc_name + " is: "
		for value in local_symbol_table[current_proc_name].itervalues():
			print_st_entry(value)
			
def print_global_symbol_table():
	global symbol_table
	if Config.flags[16]:
		print "\t\tGlobal ST is: "
		for value in symbol_table.itervalues():
			print_st_entry(value)

def print_st_entry(entry):
	printline = "\t\tST ENTRY: [NAME:" + entry['NAME']
	if entry.has_key('TYPE'):
		printline += ", TYPE:" + entry['TYPE']
	if entry.has_key('SHAPE'):
		printline += ", SHAPE:" + entry['SHAPE']
	if entry.has_key('SIZE'):
		printline += ", SIZE:" + str(entry['SIZE'])
	if entry.has_key('ROWS'):
		printline += ", ROWS:" + entry['ROWS']
	if entry.has_key('COLUMNS'):
		printline += ", COLUMNS:" + entry['COLUMNS']
	if entry.has_key('CALLTYPE'):
		printline += ", CALLTYPE:" + entry['CALLTYPE']
	printline += "]"
	print printline

def print_fourtuple(fourtuple):
	if Config.flags[13] == True:
		print "Four tuple:", fourtuple
	
def get_next_number(type):
	global irinteger, irreal, breal
	
	if type == 'I':
		print "current irint",irinteger
		irinteger = irinteger + 1
		return ('I$'+str(irinteger))
	if type == 'R':
		irreal = irreal + 1
		return ('R$'+str(irreal))
	if type == 'B':
		breal = breal + 1
		return ('B$'+str(breal))
	
def get_current_number(type):
	if type == 'I':
		return ('I$'+str(irinteger))
	if type == 'R':
		return ('R$'+str(irreal))
	if type == 'B':
		return ('B$'+str(breal))
	
def find_in_localST(key):
	global local_symbol_table, in_proc_flag, current_proc_name
	
	if((in_proc_flag == True) and (local_symbol_table[current_proc_name].has_key(key))):
		return True
	else:
		return False
			
def find_in_globalST(key):
	global symbol_table
	
	if(symbol_table.has_key(key)):
		return True
	else:
		return False
		
def get_from_localST(key):
	global local_symbol_table
	return local_symbol_table[current_proc_name][key]

def get_from_globalST(key):
	global symbol_table
	return symbol_table[key]
	
def get_from_ST(key):
	if(find_in_localST(key)):
		return get_from_localST(key)
	else: 
		if(find_in_globalST(key)):
			return get_from_globalST(key)
		else:
			return None
		   
def get_type(term):	  
	if term[0].isdigit():
		if '.' in term:
			return 'R'
		else:
			return 'I'
	elif '$' in term:
		return term[0]
	elif (get_from_ST(term)):
		x = get_from_ST(term)
		return x['TYPE'][0].upper()
	else:
		print term, "does not have a type."
		return
	pass

def check_mix_arithmatic(term1, term2):
	x = get_type(term1)
	y = get_type(term2)
	if x == y:
		return False
	else:
		return True
	
def check_if_aexpr_is_valid(aexpr):
	if(aexpr.isdigit()):		
		return True
	
	if(aexpr[0] == 'I'):			
		return True

	if(find_in_localST(aexpr)):
		if (type(aexpr) is str):
			if(get_from_localST(aexpr)['TYPE'] == 'integer'):
				return True
	else:
		if(find_in_globalST(aexpr)):
			if (type(aexpr) is str):
				if(get_from_globalST(aexpr)['TYPE'] == 'integer'):
					return True
		else:				
			print "\t\tERROR:",aexpr," not found."
			return False

def analyze_production_1():
	global semantic_stack
	fourtuple = (semantic_stack[-3],'ENDPROGRAM',None,None)
	print_fourtuple(fourtuple)

	tuple_prag = []
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append("ENDPROGRAM")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-") 
	scope=0
	pragy(tuple_prag,scope)










def analyze_production_2():
	global semantic_stack
	fourtuple = (semantic_stack[-1],'BEGINPROGRAM',None,None)

	print_fourtuple(fourtuple)
	tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("BEGINPROGRAM")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")
	scope = 0
        pragy(tuple_prag, scope)    

	semantic_stack[-2]=semantic_stack[-1]
def analyze_production_3():
	pass
def analyze_production_4():
	pass
def analyze_production_5():
	global procedure_start
	fourtuple = (None,'ENDDECLARATIONS',None,None)
	print_fourtuple(fourtuple)
	tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("ENDDECLARATIONS")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-") 
	scope=procedure_start
        pragy(tuple_prag, scope)

def analyze_production_6():
	pass
def analyze_production_7():
	pass
def analyze_production_8():
	pass
def analyze_production_9():
	pass
def analyze_production_10():
	global semantic_stack,procedure_start
	table_entry = symbol_table[semantic_stack[-3]]
	table_entry['NAME'] = semantic_stack[-1]
	insert_into_symbol_table(semantic_stack[-1],table_entry)
	if table_entry['SHAPE'] == 'MATRIX':
		fourtuple = (semantic_stack[-1],'MEMORY',table_entry['ROWS'],table_entry['COLUMNS'])
		tuple_prag = []
		tuple_prag.append(semantic_stack[-1])
		tuple_prag.append("MEMORY")
		tuple_prag.append(table_entry['ROWS'])
		tuple_prag.append(table_entry['COLUMNS'])
		temp = get_type(semantic_stack[-1])
		if temp == 'I':
			tuple_prag.append('INTEGER')
		else:
			tuple_prag.append('REAL')
            	localvar = 1
           	pragy(tuple_prag, localvar)
	else:
		fourtuple = (semantic_stack[-1],'MEMORY',table_entry['SIZE'],None)
		tuple_prag = []
		tuple_prag.append(semantic_stack[-1])
		tuple_prag.append("MEMORY")
		tuple_prag.append(table_entry['SIZE'])
		tuple_prag.append("-")
		temp = get_type(semantic_stack[-1])
		if temp == 'I':
			tuple_prag.append('INTEGER')
		else:
			tuple_prag.append('REAL')
		localvar = 0
            	pragy(tuple_prag, localvar)
		
	print_fourtuple(fourtuple)
	
def analyze_production_11():
	global semantic_stack,in_proc_flag
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-3],\
				   'SHAPE':'SCALAR',\
				   'SIZE':1}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
	temp_sem=semantic_stack[-3]
	semantic_stack[-3] = semantic_stack[-1]
	fourtuple = (semantic_stack[-1],'MEMORY',1,None)
	print_fourtuple(fourtuple)

  	tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("MEMORY")
        tuple_prag.append("1")
        tuple_prag.append("-")
        temp = get_type(semantic_stack[-1])
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')

	print "MY SEMANTIC STACK IS",semantic_stack[-3]
	if in_proc_flag == False:
        	scope = 0
	else:
		scope = 1
        pragy(tuple_prag, scope)

	

def analyze_production_12():
	global semantic_stack,in_proc_flag
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-4],\
				   'SHAPE':'VECTOR',\
				   'SIZE':semantic_stack[-2]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
	semantic_stack[-4] = semantic_stack[-1]
	fourtuple = (semantic_stack[-1],'MEMORY',semantic_stack[-2],None)
	print_fourtuple(fourtuple)

	tuple_prag = []
	tuple_prag.append(semantic_stack[-1])
	tuple_prag.append("MEMORY")
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append("-")
       	temp = get_type(semantic_stack[-1])
	if temp == 'I':
			tuple_prag.append('INTEGER')
	else:
			tuple_prag.append('REAL')
	if in_proc_flag == False:
        	scope = 0
	else:
		scope = 1
        pragy(tuple_prag, scope)
  
	
def analyze_production_13():
	global semantic_stack
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-6],\
				   'SHAPE':'MATRIX',\
				   'ROWS':semantic_stack[-4],\
				   'COLUMNS':semantic_stack[-2]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
	semantic_stack[-6] = semantic_stack[-1]
	fourtuple = (semantic_stack[-1],'MEMORY',semantic_stack[-4],semantic_stack[-2])
	print_fourtuple(fourtuple)
	tuple_prag = []
	tuple_prag.append(semantic_stack[-1])
	tuple_prag.append("MEMORY")
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append(semantic_stack[-2])
        temp = get_type(semantic_stack[-1])
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')

	if in_proc_flag == False:
        	scope = 0
	else:
		scope = 1
        pragy(tuple_prag, scope)
	
def analyze_production_14():
	global semantic_stack
	semantic_stack[-1] = 'INTEGER'
def analyze_production_15():
	global semantic_stack
	semantic_stack[-1]='REAL'
def analyze_production_16():
	pass
def analyze_production_17():
	pass
def analyze_production_18():
	pass
def analyze_production_19():
	global semantic_stack, in_proc_flag
	in_proc_flag = False
	fourtuple = (None,'ENDPROCEDURE',semantic_stack[-4],None)
	print_fourtuple(fourtuple)
	tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("ENDPROCEDURE")
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append("-")
        tuple_prag.append("-")     
      
        localvar = 0
        pragy(tuple_prag, localvar)
	print_local_symbol_table()
def analyze_production_20():
	global semantic_stack, in_proc_flag
	in_proc_flag = False
	fourtuple = (None,'ENDPROCEDURE',semantic_stack[-3],None)
	print_fourtuple(fourtuple)
	tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("ENDPROCEDURE")
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append("-")
        tuple_prag.append("-")  
        
        scope = 0
        pragy(tuple_prag, scope)
	print_local_symbol_table()
def analyze_production_21():
	pass
def analyze_production_22():
	pass
def analyze_production_23():
	global semantic_stack, in_proc_flag, current_proc_name,procedure_start
	procedure_start = 1
	current_proc_name = semantic_stack[-1]
	table_entry = {'NAME':current_proc_name,\
				   'TYPE':'PROCEDURE'}
	insert_into_symbol_table(current_proc_name,table_entry)
	local_symbol_table[current_proc_name] = {}
	in_proc_flag = True
	insert_into_symbol_table(current_proc_name,table_entry)
	fourtuple = (None,'BEGINPROCEDURE',current_proc_name,None)
	print_fourtuple(fourtuple)
 	tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("BEGINPROCEDURE")
        tuple_prag.append(current_proc_name)
        tuple_prag.append("-")
        tuple_prag.append("-")  
        
        scope = 0
        pragy(tuple_prag, scope)
	semantic_stack[-2]=current_proc_name
	
def analyze_production_24():
	fourtuple = (None,'NOFORMALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)
        tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("NOFORMALPARAMETERLIST")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")    
	localvar = 0      
	pragy(tuple_prag, localvar)    
   
       
def analyze_production_25():
	fourtuple = (None,'ENDFORMALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)
        tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("NOFORMALPARAMETERLIST")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")  
        localvar = 0
        pragy(tuple_prag, localvar)
	
def analyze_production_26():
	global semantic_stack
	fourtuple = (semantic_stack[-1],'FORMAL'+semantic_stack[-4]+' PARAMETER',semantic_stack[-2],semantic_stack[-4])
	print_fourtuple(fourtuple)

        tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append('FORMAL'+semantic_stack[-4]+' PARAMETER')
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append()  

        localvar = 1
        pragmatic(tuple_prag, localvar)
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-3],\
				   'SHAPE':'SCALAR',\
				   'SIZE':1,\
				   'CALLTYPE':semantic_stack[-4]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
def analyze_production_27():
	global semantic_stack
	fourtuple = (semantic_stack[-1],'FORMAL'+semantic_stack[-5]+' PARAMETER',semantic_stack[-2],semantic_stack[-4])
	print_fourtuple(fourtuple)

        tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append('FORMAL'+semantic_stack[-5]+' PARAMETER')
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append("-")
      
	temp = get_type(semantic_stack[-1])
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')     
        localvar = 1
        pragy(tuple_prag, localvar)
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-4],\
				   'SHAPE':'VECTOR',\
				   'SIZE':semantic_stack[-2],\
				   'CALLTYPE':semantic_stack[-5]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
	
def analyze_production_28():
	global semantic_stack
	fourtuple = (semantic_stack[-1],'FORMAL'+semantic_stack[-7]+' PARAMETER',semantic_stack[-2],semantic_stack[-4])
	print_fourtuple(fourtuple)

        tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append('FORMAL'+semantic_stack[-7]+' PARAMETER')
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append(semantic_stack[-4])
	temp = get_type(semantic_stack[-1])
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')
    
        
        localvar = 1
        pragy(tuple_prag, localvar)
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-6],\
				   'SHAPE':'MATRIX',\
				   'ROWS':semantic_stack[-2],\
				   'COLUMNS':semantic_stack[-4],\
				   'CALLTYPE':semantic_stack[-7]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
def analyze_production_29():
	global semantic_stack
	fourtuple = (None,'BEGINFORMALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)
        tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("BEGINFORMALPARAMETERLIST")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")
        
        localvar = 0
        pragy(tuple_prag, localvar)

	fourtuple = (semantic_stack[-1],'FORMAL'+semantic_stack[-4]+' PARAMETER',semantic_stack[-2],None)
	print_fourtuple(fourtuple)
        tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append("-")
        temp = get_type(semantic_stack[-1])
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')

        localvar = 1
        pragy(tuple_prag, localvar)
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-3],\
				   'SHAPE':'SCALAR',\
				   'SIZE':1,\
				   'CALLTYPE':semantic_stack[-4]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
def analyze_production_30():
	global semantic_stack
	fourtuple = (None,'BEGINFORMALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)

	fourtuple = (semantic_stack[-1],'FORMAL'+semantic_stack[-5]+' PARAMETER',semantic_stack[-2],semantic_stack[-4])
	print_fourtuple(fourtuple)
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-4],\
				   'SHAPE':'VECTOR',\
				   'SIZE':semantic_stack[-2],\
				   'CALLTYPE':semantic_stack[-5]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
def analyze_production_31():
	global semantic_stack
	fourtuple = (None,'BEGINFORMALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)
 	tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("BEGINFORMALPARAMETERLIST")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")
        
        localvar = 0
        pragy(tuple_prag, localvar)

	fourtuple = (semantic_stack[-1],'FORMAL'+semantic_stack[-7]+' PARAMETER',semantic_stack[-2],semantic_stack[-4])
	print_fourtuple(fourtuple)
        tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append('FORMAL'+semantic_stack[-7]+' PARAMETER')
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append(semantic_stack[-4])
	temp = get_type(semantic_stack[-1])
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')
       
      
        localvar = 1
        pragy(tuple_prag, localvar) 
	table_entry = {'NAME':semantic_stack[-1],\
				   'TYPE':semantic_stack[-6],\
				   'SHAPE':'MATRIX',\
				   'ROWS':semantic_stack[-2],\
				   'COLUMNS':semantic_stack[-4],\
				   'CALLTYPE':semantic_stack[-7]}
	insert_into_symbol_table(semantic_stack[-1],table_entry)
def analyze_production_32():
	global semantic_stack
	semantic_stack[-1] = 'VALUE'
def analyze_production_33():
	global semantic_stack
	semantic_stack[-1] = 'REF'
def analyze_production_34():
	
	fourtuple = (None,'ENDEXECUTION',None,None)
	print_fourtuple(fourtuple)

	
def analyze_production_35():
	fourtuple = ("MAIN","LABEL",None,None)
	print_fourtuple(fourtuple)
	tuple_prag = []
        tuple_prag.append("MAIN")
        tuple_prag.append("LABEL")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)
	
def analyze_production_36():
	pass
def analyze_production_37():
	pass
def analyze_production_38():
	pass
def analyze_production_39():
	pass
def analyze_production_40():
	pass
def analyze_production_41():
	pass
def analyze_production_42():
	pass
def analyze_production_43():
	pass
def analyze_production_44():
	pass
def analyze_production_45():
	fourtuple = ('scanf','ENDPROCEDURECALL',None,None)
	print_fourtuple(fourtuple)
	
def analyze_production_46():
	global semantic_stack
	fourtuple = (None,'REFERENCEACTUALPARAMETER',semantic_stack[-1],None)
	print_fourtuple(fourtuple)
	
def analyze_production_47():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-4])):
		found_symbol = get_from_localST(semantic_stack[-4])
	else: 
		if(find_in_globalST(semantic_stack[-4])):
			found_symbol = get_from_globalST(semantic_stack[-4])
		else:
			print "\t\tERROR:",semantic_stack[-4]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
			return
	
	four_tuple = (None,\
				  "REFERENCEACTUALPARAMETER",\
				  semantic_stack[-4],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	
def analyze_production_48():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-6],"is not a matrix."
			return
	
	prefix = 'I'
		
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-4],\
				  get_from_ST(semantic_stack[-6])['COLUMNS'])
	print_fourtuple(four_tuple)	
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	temp_number = get_current_number(prefix)
	
	if(get_from_ST(semantic_stack[-6])['TYPE'] == 'INTEGER'):
		prefix = 'I'
	else: 
		if(get_from_ST(semantic_stack[-6])['TYPE'] == 'REAL'):
			prefix = 'R'
			
	four_tuple = (None,\
				  "REFERENCEACTUALPARAMETER",\
				  semantic_stack[-6],\
				  temp_number)
	print_fourtuple(four_tuple)
	
def analyze_production_49():
	global semantic_stack
	fourtuple = (None,'REFERENCEACTUALPARAMETER',semantic_stack[-1],None)
	print_fourtuple(fourtuple)
	
def analyze_production_50():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-4])):
		found_symbol = get_from_localST(semantic_stack[-4])
	else: 
		if(find_in_globalST(semantic_stack[-4])):
			found_symbol = get_from_globalST(semantic_stack[-4])
		else:
			print "\t\tERROR:",semantic_stack[-4]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
			return
	
	four_tuple = (None,\
				  "REFERENCEACTUALPARAMETER",\
				  semantic_stack[-4],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	
def analyze_production_51():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-6],"is not a matrix."
			return
	
	prefix = 'I'
		
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-4],\
				  get_from_ST(semantic_stack[-6])['COLUMNS'])
	print_fourtuple(four_tuple)	
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	temp_number = get_current_number(prefix)
	
	if(get_from_ST(semantic_stack[-6])['TYPE'] == 'INTEGER'):
		prefix = 'I'
	else: 
		if(get_from_ST(semantic_stack[-6])['TYPE'] == 'REAL'):
			prefix = 'R'
			
	four_tuple = (None,\
				  "REFERENCEACTUALPARAMETER",\
				  semantic_stack[-6],\
				  temp_number)
	print_fourtuple(four_tuple)
	
def analyze_production_52():
	global semantic_stack
	fourtuple = ('scanf','CALLPROCEDURE',None,None)
	print_fourtuple(fourtuple)
	fourtuple = (None,'BEGINACTUALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)
	fourtuple = (None,'VALUEACTUALPARAMETER',semantic_stack[-1],None)
	print_fourtuple(fourtuple)

        tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("VALUEACTUALPARAMETER")
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("-")
        tuple_prag.append("-")        
        
        
        localvar = 0
        pragy(tuple_prag, localvar)
	
def analyze_production_53():
	pass

def analyze_production_54():
	fourtuple = ('printf','ENDPROCEDURECALL',None,None)
	print_fourtuple(fourtuple)
	
def analyze_production_55():
	global semantic_stack
	fourtuple = (None,'VALUEACTUALPARAMETER',semantic_stack[-1],None)
	print_fourtuple(fourtuple)
	
def analyze_production_56():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-4])):
		found_symbol = get_from_localST(semantic_stack[-4])
	else: 
		if(find_in_globalST(semantic_stack[-4])):
			found_symbol = get_from_globalST(semantic_stack[-4])
		else:
			print "\t\tERROR:",semantic_stack[-4]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
			return
	
	four_tuple = (None,\
				  "VALUEACTUALPARAMETER",\
				  semantic_stack[-4],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	
def analyze_productton_57():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-6],"is not a matrix."
			return
	
	prefix = 'I'
		
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-4],\
				  get_from_ST(semantic_stack[-6])['COLUMNS'])
	print_fourtuple(four_tuple)
 	tuple_prag = []
        tuple_prag.append(get_next_number(prefix))
        tuple_prag.append("IMULT")
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append(get_from_ST(semantic_stack[-6])['COLUMNS'])
    









	
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)


        tuple_prag = []
        tuple_prag.append(get_next_number(prefix))
        tuple_prag.append("IADD")
        tuple_prag.append(temp_number)
        tuple_prag.append(semantic_stack[-2])
      









	temp_number = get_current_number(prefix)
	
	if(get_from_ST(semantic_stack[-6])['TYPE'] == 'INTEGER'):
		prefix = 'I'
	else: 
		if(get_from_ST(semantic_stack[-6])['TYPE'] == 'REAL'):
			prefix = 'R'
			
	four_tuple = (None,\
				  "VALUEACTUALPARAMETER",\
				  semantic_stack[-6],\
				  temp_number)
	print_fourtuple(four_tuple)
	tuple_prag = []
        tuple_prag.append("-")
        tuple_prag.append("VALUEACTUALPARAMETER")
        tuple_prag.append(semantic_stack[-6])
        tuple_prag.append(temp_number)
       
	
def analyze_production_58():
	global semantic_stack
	fourtuple = ("#",'VALUEACTUALPARAMETER',semantic_stack[-1],None)
	print_fourtuple(fourtuple)
	tuple_prag = []
        tuple_prag.append("#")
        tuple_prag.append("VALUEACTUALPARAMETER")
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("-")
        tuple_prag.append("-")
        
        scope = 0
        pragy(tuple_prag, scope)
	
def analyze_production_59():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-4])):
		found_symbol = get_from_localST(semantic_stack[-4])
	else: 
		if(find_in_globalST(semantic_stack[-4])):
			found_symbol = get_from_globalST(semantic_stack[-4])
		else:
			print "\t\tERROR:",semantic_stack[-4]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
			return
	
	four_tuple = (None,\
				  "VALUEACTUALSUBPARAMETER",\
				  semantic_stack[-4],\
				  semantic_stack[-2])



	
	print_fourtuple(four_tuple)
	

	tuple_prag=[]
	tuple_prag.append("#")
	tuple_prag.append("VALUEACTUALPARAMETER")
	tuple_prag.append(semantic_stack[-4])
	tuple_prag.append(semantic_stack[-2])
	tuple_prag.append("-")
 	scope = 0
  	pragy(tuple_prag,scope)
	tuple_prag=[]
	
	
def analyze_production_60():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-6],"is not a matrix."
			return
	
	prefix = 'I'
		
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-4],\
				  get_from_ST(semantic_stack[-6])['COLUMNS'])
	print_fourtuple(four_tuple)	
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	temp_number = get_current_number(prefix)
	
	if(get_from_ST(semantic_stack[-6])['TYPE'] == 'INTEGER'):
		prefix = 'I'
	else: 
		if(get_from_ST(semantic_stack[-6])['TYPE'] == 'REAL'):
			prefix = 'R'
			
	four_tuple = (None,\
				  "VALUEACTUALPARAMETER",\
				  semantic_stack[-6],\
				  temp_number)
	print_fourtuple(four_tuple)
	
def analyze_production_61():
	global semantic_stack
	fourtuple = ("printf",'CALLPROCEDURE',None,None)
	print_fourtuple(fourtuple)
	tuple_prag=[]
	tuple_prag.append("printf")
	tuple_prag.append("CALLPROCEDURE")
	tuple_prag.append("-")
	tuple_prag.append("-")
	tuple_prag.append("-")
 	scope = 0
  	pragy(tuple_prag,scope)
	

	fourtuple = (None,'BEGINACTUALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)    
        tuple_prag = []
        tuple_prag.append("-" )
        tuple_prag.append( "BEGINACTUALPARAMETERLIST")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")
 	scope = 0
        pragy(tuple_prag, scope)
	

	fourtuple = (None,'VALUEACTUALPARAMETER',semantic_stack[-1],None)
	print_fourtuple(fourtuple)

	tuple_prag = []
        tuple_prag.append("-" )
        tuple_prag.append("VALUEACTUALPARAMETER")
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("-")
        tuple_prag.append("-")
       	scope = 0
        pragy(tuple_prag, scope)
	
	
def analyze_production_62():
	global semantic_stack
	fourtuple = (None,'NOACTUALPARAMETERS',None,None)
	print_fourtuple(fourtuple)
	fourtuple = (semantic_stack[-2],'ENDACTUALPROCEDURECALL',None,None)
	print_fourtuple(fourtuple)
	
def analyze_production_63():
	global semantic_stack
	fourtuple = (semantic_stack[-2],'ENDPROCEDURECALL',None,None)
	print_fourtuple(fourtuple)
	
def analyze_production_64():
	global semantic_stack
	found_symbol = None
	if(find_in_globalST(semantic_stack[-1])):
			found_symbol = get_from_globalST(semantic_stack[-1])
	else:
		print "\t\tERROR:",semantic_stack[-1]," not found."
		return
			
	if (found_symbol):
		if found_symbol['TYPE'] != 'PROCEDURE':
			print "\t\tERROR:",semantic_stack[-1],"is not a procedure."
			return
		   
	fourtuple = (semantic_stack[-1],'PROCCALL',None,None)
	print_fourtuple(fourtuple)
        tuple_prag = []
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("PROCCALL")
        tuple_prag.append("-")
        tuple_prag.append("-")
        tuple_prag.append("-")
        localvar = 0
        pragy(tuple_prag, localvar)
	semantic_stack[-2] = semantic_stack[-1]
def analyze_production_65():
	fourtuple = (None,'ENDACTUALPARAMETERLIST',None,None)
	print_fourtuple(fourtuple)
	
def analyze_production_66():
	global semantic_stack
	four_tuple = (None,'BEGINACTUALPARAMETERLIST',None,None)
	print_fourtuple(four_tuple)
	
	found_symbol = None
	if(find_in_localST(semantic_stack[-1])):
		found_symbol = get_from_localST(semantic_stack[-1])
	else: 
		if(find_in_globalST(semantic_stack[-1])):
			found_symbol = get_from_globalST(semantic_stack[-1])
		else:
			print "\t\tERROR:",semantic_stack[-1]," not found."
			return
			
	four_tuple = (None,\
				  "SUB"+str(semantic_stack[-2])+"ACTUALPARAMETER",\
				  semantic_stack[-1],\
				  None)
	print_fourtuple(four_tuple)
	
def analyze_production_67():
	global semantic_stack
	found_symbol = None
	if(find_in_localST(semantic_stack[-4])):
		found_symbol = get_from_localST(semantic_stack[-4])
	else: 
		if(find_in_globalST(semantic_stack[-4])):
			found_symbol = get_from_globalST(semantic_stack[-4])
		else:
			print "\t\tERROR:",semantic_stack[-4]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-4],"is not a vector."
			return
			
	four_tuple = (None,\
				  "SUB"+str(semantic_stack[-5])+"ACTUALPARAMETER",\
				  semantic_stack[-4],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	
def analyze_production_68():
	global semantic_stack
	found_symbol = None
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-6],"is not a matrix."
			return 
	
	prefix = 'I'
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-4],\
				  get_from_ST(semantic_stack[-6])['COLUMNS'])
	print_fourtuple(four_tuple)	
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
			
	temp_number = get_current_number(prefix)
	four_tuple = (None,\
				  "SUB"+str(semantic_stack[-7])+"ACTUALPARAMETER",\
				  semantic_stack[-6],\
				  temp_number)
	print_fourtuple(four_tuple)
	
def analyze_production_69():
	global semantic_stack
	four_tuple = (None,'BEGINACTUALPARAMETERLIST',None,None)
	print_fourtuple(four_tuple)
	
	found_symbol = None
	if(find_in_localST(semantic_stack[-1])):
		found_symbol = get_from_localST(semantic_stack[-1])
	else: 
		if(find_in_globalST(semantic_stack[-1])):
			found_symbol = get_from_globalST(semantic_stack[-1])
		else:
			print "\t\tERROR:",semantic_stack[-1]," not found."
			return
			
	four_tuple = (None,\
				  "SUB"+str(semantic_stack[-2])+"ACTUALPARAMETER",\
				  semantic_stack[-1],\
				  None)
	print_fourtuple(four_tuple)
	
def analyze_production_70():
	global semantic_stack
	four_tuple = (None,'BEGINACTUALPARAMETERLIST',None,None)
	print_fourtuple(four_tuple)
	
	found_symbol = None
	if(find_in_localST(semantic_stack[-4])):
		found_symbol = get_from_localST(semantic_stack[-4])
	else: 
		if(find_in_globalST(semantic_stack[-4])):
			found_symbol = get_from_globalST(semantic_stack[-4])
		else:
			print "\t\tERROR:",semantic_stack[-4]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-4],"is not a vector."
			return
			
	four_tuple = (None,\
				  "SUB"+str(semantic_stack[-5])+"ACTUALPARAMETER",\
				  semantic_stack[-4],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	
def analyze_production_71():
	global semantic_stack
	four_tuple = (None,'BEGINACTUALPARAMETERLIST',None,None)
	print_fourtuple(four_tuple)
	
	found_symbol = None
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-6],"is not a matrix."
			return 
	
	prefix = 'I'
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-4],\
				  get_from_ST(semantic_stack[-6])['COLUMNS'])
	print_fourtuple(four_tuple)	
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
			
	temp_number = get_current_number(prefix)
	four_tuple = (None,\
				  "SUB"+str(semantic_stack[-7])+"ACTUALPARAMETER",\
				  semantic_stack[-6],\
				  temp_number)
	print_fourtuple(four_tuple)
	
##### TESTING LOOPS START #####

def analyze_production_72():
	global loop_stack
	loop_pop=loop_stack.pop()
	four_tuple = (loop_pop,"LABEL",None,None)

	print_fourtuple(four_tuple)
	tuple_prag = []
        tuple_prag.append(loop_pop)
        tuple_prag.append("LABEL")
        tuple_prag.append("-")
        tuple_prag.append("-")        
        tuple_prag.append("-")
        scope = 0

        pragy(tuple_prag, scope)

def analyze_production_73():
	global loop_stack
	four_tuple = (loop_stack.pop(),"LABEL",None,None)
	print_fourtuple(four_tuple)
		
def analyze_production_74():
	global loop_stack, irlabel
	four_tuple = ("L$"+str(irlabel),"JUMP",None,None)
	print_fourtuple(four_tuple)
	irlabel = irlabel + 1
	
	four_tuple = (loop_stack.pop(),"LABEL",None,None)
	print_fourtuple(four_tuple)
	
	loop_stack.append("L$"+str(irlabel-1))

def analyze_production_75():
	global loop_stack, irlabel, semantic_stack
	if get_type(semantic_stack[-2]) == 'B':
		four_tuple = ("L$"+str(irlabel),"CJUMPF",\
					  get_current_number('B'),None)
		print_fourtuple(four_tuple)
	 	tuple_prag = []
		tuple_prag.append("L$"+str(irlabel))
		tuple_prag.append("CJUMPF")
		tuple_prag.append(get_current_number('B'))
		tuple_prag.append("-")        
		tuple_prag.append("-")
		scope = 0
		pragy(tuple_prag, scope)

		loop_stack.append("L$"+str(irlabel))
		irlabel = irlabel + 1
	else: 
		print "\t\tERROR:"," In IF, expression is not boolean."

def analyze_production_76():
	'''
	global semantic_stack
	four_tuple = (semantic_stack[-4],\
				  "STORE",\
				  semantic_stack[-2],\
				  None)
	print_fourtuple(four_tuple)
	
	tuple_prag = []
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append("STORE")
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append("-")        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)
          
#	semantic_stack[-5] = semantic_stack[-4]
#
	'''
	global semantic_stack, irlabel, loop_stack,label_stack,for_counter
	four_tuple = (semantic_stack[-4],\
				  "STORE",\
				  semantic_stack[-2],\
				  None)
	print_fourtuple(four_tuple)
	tuple_prag = []
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append("STORE")
        tuple_prag.append(semantic_stack[-2])
        tuple_prag.append("-")        
	temp = get_type(semantic_stack[-4])
	print "temp", temp
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')
        scope = 0
        pragy(tuple_prag, scope)

	loop_stack.append("L$"+str(irlabel))
	label_stack.append("L$"+str(irlabel))

	four_tuple = ("L$"+str(irlabel+1),"JUMP",None,None)
	print_fourtuple(four_tuple)
	tuple_prag = []
        tuple_prag.append("L$"+str(irlabel+1))
        tuple_prag.append("JUMP")
        tuple_prag.append("-")
        tuple_prag.append("-") 
	tuple_prag.append("-")        
	
        scope = 0
        pragy(tuple_prag, scope)

	#irlabel=irlabel-1
	
	four_tuple = ("L$"+str(irlabel),"LABEL",None,None)
	print_fourtuple(four_tuple) 
 	tuple_prag = []
        tuple_prag.append("L$"+str(irlabel))
        tuple_prag.append("LABEL")
        tuple_prag.append("-")
        tuple_prag.append("-")        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)
        

        irlabel=irlabel+2	
	for_counter=for_counter+1
	
	
	
	semantic_stack[-5] = semantic_stack[-4]













def analyze_production_77():
	'''
	global semantic_stack, irlabel, loop_stack
	four_tuple = ("L$"+str(irlabel),"LABEL",None,None)
	print_fourtuple(four_tuple) 
	tuple_prag = []
        tuple_prag.append("L$"+str(irlabel))
        tuple_prag.append("LABEL")
        tuple_prag.append("-")
        tuple_prag.append("-")        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)	
	irlabel=irlabel+1
	
	four_tuple = ("L$"+str(irlabel),"JUMP",None,None)
	print_fourtuple(four_tuple) 
	tuple_prag = []
        tuple_prag.append("L$"+str(irlabel))
        tuple_prag.append("JUMP")
        tuple_prag.append("-")
        tuple_prag.append("-")        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)


	loop_stack.append("L$"+str(irlabel))
	irlabel = irlabel + 1
	
	prefix = 'I'
	four_tuple = (get_next_number(prefix),\
				  prefix+"ADD",\
				  semantic_stack[-3],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	

	tuple_prag = []
        tuple_prag.append(get_next_number(prefix))
        tuple_prag.append(prefix+"ADD")
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append(semantic_stack[-2])        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)	

	
	four_tuple = (semantic_stack[-3],\
				  "STORE",\
				  get_current_number(prefix),\
				  None)
	print_fourtuple(four_tuple)

	tuple_prag = []
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append("STORE")
        tuple_prag.append(get_current_number(prefix))
        tuple_prag.append("-")        
        tuple_prag.append("INTEGER")
        scope = 0
        pragy(tuple_prag, scope)	

	
	semantic_stack[-3] = get_current_number(prefix)
	'''
	global semantic_stack, irlabel, loop_stack,label_stack
	loop_stack.append("L$"+str(irlabel))
	
	prefix = 'I'
	temp=get_next_number(prefix)
	four_tuple = (temp,\
				  prefix+"ADD",\
				  semantic_stack[-3],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)

	tuple_prag = []
        tuple_prag.append(temp)
        tuple_prag.append(prefix+"ADD")
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append(semantic_stack[-2])        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)
	
	four_tuple = (semantic_stack[-3],\
				  "STORE",\
				  get_current_number(prefix),\
				  None)
	print_fourtuple(four_tuple)
	tuple_prag = []
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append("STORE")
        tuple_prag.append(get_current_number(prefix))
	#print 'get current number',get_current_number(prefix)
        tuple_prag.append("-")        
        tuple_prag.append("INTEGER")
        scope = 0
        pragy(tuple_prag, scope)
	
	semantic_stack[-3] = get_current_number(prefix)
	
	templabel = label_stack[-1]
        strlen = len(templabel)
        labelcount = templabel[2:strlen]
        labelcount = int(labelcount) + 1
        label = 'L$' + str(labelcount)
	#four_tuple = ("L$"+str(irlabel),"LABEL",None,None)
        four_tuple = (label,"LABEL",None,None)

	print_fourtuple(four_tuple) 
	tuple_prag = []
        tuple_prag.append(label)
        tuple_prag.append("LABEL")
        tuple_prag.append("-")
        tuple_prag.append("-")        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)







	

def analyze_production_78():
	global loop_stack, irlabel, semantic_stack
	if get_type(semantic_stack[-2]) == 'B':
		four_tuple = ("L$"+str(irlabel),"CJUMP",\
					  get_current_number('B'),None)
		print_fourtuple(four_tuple)

		tuple_prag = []
        	tuple_prag.append("L$"+str(irlabel))
        	tuple_prag.append("CJUMPT")
        	tuple_prag.append(get_current_number('B'))
		tuple_prag.append("-")        
		tuple_prag.append("-")
		scope = 0
		pragy(tuple_prag, scope)
		











		loop_stack.append("L$"+str(irlabel))
		irlabel = irlabel + 1
	else: 
		print "\t\tERROR:"," In FOR, expression is not boolean."

def analyze_production_79():
	'''
	global loop_stack, irlabel, semantic_stack
	if len(loop_stack) > 1:
		loop_pop=loop_stack.pop(-2)
		four_tuple = (loop_pop,"JUMP",None,None)
		print_fourtuple(four_tuple)
		
		tuple_prag = []
		tuple_prag.append(loop_pop)
		tuple_prag.append("JUMP")
		tuple_prag.append("-")
		tuple_prag.append("-")        
		tuple_prag.append("-")
		scope = 0
		pragy(tuple_prag, scope)




	if len(loop_stack) > 0:
		loop_pop=loop_stack.pop()
		four_tuple = (loop_pop,"LABEL",None,None)
		print_fourtuple(four_tuple)
	 	tuple_prag = []
		tuple_prag.append(loop_pop)
		tuple_prag.append("LABEL")
		tuple_prag.append("-")
		tuple_prag.append("-")        
		tuple_prag.append("-")
		scope = 0
		pragy(tuple_prag, scope)
	'''
	global loop_stack, irlabel, semantic_stack,label_stack,for_counter
	label=0
	print "ls-1",label_stack[-1]
	print "ls-2. for",label_stack[-2],for_counter
	
        if for_counter == 2:
		label = label_stack[-1]
        elif for_counter == 1:
      		label = label_stack[-2]

	four_tuple = (label,"JUMP",None,None)
	print_fourtuple(four_tuple)
	tuple_prag = []
	tuple_prag.append(label)
	tuple_prag.append("JUMP")
	tuple_prag.append("-")
	tuple_prag.append("-")        
	tuple_prag.append("-")
	scope = 0

	pragy(tuple_prag, scope)

	templabel = label
        strlen = len(templabel)
        labelcount = templabel[2:strlen]
        labelcount = int(labelcount) + 2
        label = 'L$' + str(labelcount)
	
	four_tuple = (label,"LABEL",None,None)
	print_fourtuple(four_tuple)
	tuple_prag = []
	tuple_prag.append(label)
	tuple_prag.append("LABEL")

	tuple_prag.append("-")
	tuple_prag.append("-")        
	tuple_prag.append("-")
	scope = 0

	pragy(tuple_prag, scope)
	for_counter=for_counter-1

##### TESTING LOOPS END #####


def analyze_production_80():
	pass

def analyze_production_81():
	global semantic_stack
	prefix = 'R'
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
			return
	
	if(found_symbol['TYPE'] == 'INTEGER'):
		prefix = 'I'
		if(get_type(semantic_stack[-1]) == 'R'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTRI",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple) 
			semantic_stack[-1] = get_current_number(prefix) 
	elif(found_symbol['TYPE'] == 'REAL'):
		prefix = 'R'
		if(get_type(semantic_stack[-1]) == 'I'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTIR",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple) 
			semantic_stack[-1] = get_current_number(prefix)

	four_tuple = (semantic_stack[-6],\
				  "STORE",\
				  semantic_stack[-1],\
				  semantic_stack[-4])
	print_fourtuple(four_tuple)
	
	semantic_stack[-6] = semantic_stack[-1]
	
def analyze_production_82():
	global semantic_stack
	prefix = 'R'
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
			return
	
	if(found_symbol['TYPE'] == 'INTEGER'):
		prefix = 'I'
		if(get_type(semantic_stack[-1]) == 'R'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTRI",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple) 
			semantic_stack[-1] = get_current_number(prefix) 
	elif(found_symbol['TYPE'] == 'REAL'):
		prefix = 'R'
		if(get_type(semantic_stack[-1]) == 'I'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTIR",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple) 
			semantic_stack[-1] = get_current_number(prefix)

	four_tuple = (semantic_stack[-6],\
				  "SUBSTORE",\
				  semantic_stack[-1],\
				  semantic_stack[-4])
	print_fourtuple(four_tuple)
	
	semantic_stack[-6] = semantic_stack[-1]
	
def analyze_production_83():
	global semantic_stack
	prefix = 'R'
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-8])):
		found_symbol = get_from_localST(semantic_stack[-8])
	else: 
		if(find_in_globalST(semantic_stack[-8])):
			found_symbol = get_from_globalST(semantic_stack[-8])
		else:
			print "\t\tERROR:",semantic_stack[-8]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-8],"is not a matrix."
			return
	
	if(found_symbol['TYPE'] == 'INTEGER'):
		prefix = 'I'
		if(get_type(semantic_stack[-1]) == 'R'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTRI",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple) 
			semantic_stack[-1] = get_current_number(prefix) 
	elif(found_symbol['TYPE'] == 'REAL'):
		prefix = 'R'
		if(get_type(semantic_stack[-1]) == 'I'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTIR",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple) 
			semantic_stack[-1] = get_current_number(prefix)
	
	prefix = 'I'
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-6],\
				  found_symbol['COLUMNS'])
	print_fourtuple(four_tuple)
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-4])
	print_fourtuple(four_tuple)
	
	four_tuple = (semantic_stack[-8],\
				  "SUBSTORE",\
				  semantic_stack[-1],\
				  get_current_number(prefix))
	print_fourtuple(four_tuple)
	
	semantic_stack[-8] = semantic_stack[-1]
	
def analyze_production_84():
	global semantic_stack
	prefix = 'R'
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-3])):
		found_symbol = get_from_localST(semantic_stack[-3])
	else: 
		if(find_in_globalST(semantic_stack[-3])):
			found_symbol = get_from_globalST(semantic_stack[-3])
		else:
			print "\t\tERROR:",semantic_stack[-3]," not found."
			return
			
#	if (found_symbol):
#		if found_symbol['SHAPE'] != 'VECTOR':
#			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
#			return
	
	if(found_symbol['TYPE'] == 'INTEGER'):
		prefix = 'I'
		if(get_type(semantic_stack[-1]) == 'R'):
			t=get_next_number(prefix)
			four_tuple = (t,\
				  "CONVERTRI",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple)
			
			tuple_prag = []
		        tuple_prag.append(t)
		        tuple_prag.append("CONVERTRI")
		        tuple_prag.append(semantic_stack[-1])
		        tuple_prag.append("-")
		        tuple_prag.append("INTEGER")
		    	scope = 0
		        pragy(tuple_prag, scope) 

			semantic_stack[-1] = get_current_number(prefix) 
	elif(found_symbol['TYPE'] == 'REAL'):
		prefix = 'R'
		if(get_type(semantic_stack[-1]) == 'I'):
			t=get_next_number(prefix)
			four_tuple = (t,\
				  "CONVERTIR",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple)
			tuple_prag = []
		        tuple_prag.append(t)
		        tuple_prag.append("CONVERTIR")
		        tuple_prag.append(semantic_stack[-1])
		        tuple_prag.append("-")
		        tuple_prag.append("REAL")
		    	scope = 0
		        pragy(tuple_prag, scope)


			semantic_stack[-1] = get_current_number(prefix)

	four_tuple = (semantic_stack[-3],\
				  "STORE",\
				  semantic_stack[-1],\
				  None)
	print_fourtuple(four_tuple)
	tuple_prag = []
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append("STORE")
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("-")
        temp = get_type(semantic_stack[-3])
	if temp == 'I':
		tuple_prag.append('INTEGER')
	else:
		tuple_prag.append('REAL')
        scope = 0
        pragy(tuple_prag, scope)
             
	
	semantic_stack[-3] = semantic_stack[-1]
	
def analyze_production_85():
	global semantic_stack
	prefix = 'R'
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-6],"is not a vector."
			return
	
	if(found_symbol['TYPE'] == 'INTEGER'):
		prefix = 'I'
		if(get_type(semantic_stack[-1]) == 'R'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTRI",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple)
			tuple_prag = []
		        tuple_prag.append(get_next_number(prefix))
		        tuple_prag.append("CONVERTRI")
		        tuple_prag.append(semantic_stack[-1])
		        tuple_prag.append("-")
		        tuple_prag.append("INTEGER")
		        scope = 0
		        pragy(tuple_prag, scope)                 
		            





 
			semantic_stack[-1] = get_current_number(prefix) 
	elif(found_symbol['TYPE'] == 'REAL'):
		prefix = 'R'
		if(get_type(semantic_stack[-1]) == 'I'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTIR",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple)

  			tuple_prag = []
		        tuple_prag.append(get_next_number(prefix))
		        tuple_prag.append("CONVERTIR")
		        tuple_prag.append(semantic_stack[-1])
		        tuple_prag.append("-")
		        tuple_prag.append("REAL")
		        scope = 0
		        pragy(tuple_prag, scope)                 
		            






			semantic_stack[-1] = get_current_number(prefix)

	four_tuple = (semantic_stack[-6],\
				  "SUBSTORE",\
				  semantic_stack[-1],\
				  semantic_stack[-4])
	print_fourtuple(four_tuple)

	tuple_prag = []
        tuple_prag.append(semantic_stack[-6])
        tuple_prag.append("SUBSTORE")
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append(found_symbol['TYPE'])
        scope = 0
        pragy(tuple_prag, scope)                        
                	
	semantic_stack[-6] = semantic_stack[-1]
	
def analyze_production_86():
	global semantic_stack
	prefix = 'R'
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-8])):
		found_symbol = get_from_localST(semantic_stack[-8])
	else: 
		if(find_in_globalST(semantic_stack[-8])):
			found_symbol = get_from_globalST(semantic_stack[-8])
		else:
			print "\t\tERROR:",semantic_stack[-8]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-8],"is not a matrix."
			return
		
	if not check_if_aexpr_is_valid(semantic_stack[-6]):
		print "\t\tERROR:",semantic_stack[-6],"is not a valid index."
		return
	
	if not check_if_aexpr_is_valid(semantic_stack[-4]):
		print "\t\tERROR:",semantic_stack[-4],"is not a valid index."
		return
	
	if(found_symbol['TYPE'] == 'INTEGER'):
		prefix = 'I'
		if(get_type(semantic_stack[-1]) == 'R'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTRI",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple)
		
			 
			semantic_stack[-1] = get_current_number(prefix) 
	elif(found_symbol['TYPE'] == 'REAL'):
		prefix = 'R'
		if(get_type(semantic_stack[-1]) == 'I'):
			four_tuple = (get_next_number(prefix),\
				  "CONVERTIR",\
				  semantic_stack[-1],\
				  None)
			print_fourtuple(four_tuple) 
			semantic_stack[-1] = get_current_number(prefix)
	
	prefix = 'I'
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-6],\
				  found_symbol['COLUMNS'])
	print_fourtuple(four_tuple)
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-4])
	print_fourtuple(four_tuple)
	
	four_tuple = (semantic_stack[-8],\
				  "SUBSTORE",\
				  semantic_stack[-1],\
				  get_current_number(prefix))
	print_fourtuple(four_tuple)
	
	semantic_stack[-8] = semantic_stack[-1]
	
	
def analyze_production_87():
	pass
	
def analyze_production_88():
	global semantic_stack
	four_tuple = (get_next_number('B'),\
				  "OR",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_89():
	pass
	
def analyze_production_90():
	pass
	
def analyze_production_91():
	global semantic_stack
	four_tuple = (get_next_number('B'),\
				  "AND",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_92():
	pass
	
def analyze_production_93():
	global semantic_stack
	four_tuple = (get_next_number('B'),\
				  "NOT",\
				  semantic_stack[-1],\
				  None)
	print_fourtuple(four_tuple)	
	semantic_stack[-1] = get_current_number('B')
	
def analyze_production_94():
	pass
	
def analyze_production_95():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		prefix = 'R'
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
		
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'
	
	four_tuple = (get_next_number('B'),\
				  prefix+"LT",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_96():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		prefix = 'R'
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
		
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'
	
	four_tuple = (get_next_number('B'),\
				  prefix+"LTEQ",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)
	tuple_prag = []
        tuple_prag.append(get_next_number('B'))
        tuple_prag.append(prefix+"LTEQ")
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append("-") 
                       
        localvar = 0
        pragy(tuple_prag, localvar)	
	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_97():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		prefix = 'R'
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
		
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'
	temp_number=get_next_number('B')
	four_tuple = (temp_number,\
				  prefix+"GT",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)
	     
        tuple_prag = []
        tuple_prag.append(temp_number)
        tuple_prag.append(prefix+"GT")
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append(semantic_stack[-1])        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)

	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_98():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		prefix = 'R'
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
		temp=	get_next_number(prefix)
		four_tuple = (temp,\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
		
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'
	
	four_tuple = (temp,\
				  prefix+"GTEQ",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_99():
	global semantic_stack
	
	if not check_if_aexpr_is_valid(semantic_stack[-3]):
		print "\t\tERROR:",semantic_stack[-3],"is not a valid index."
		return
	
	if not check_if_aexpr_is_valid(semantic_stack[-1]):
		print "\t\tERROR:",semantic_stack[-1],"is not a valid index."
		return
	
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		prefix = 'R'
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
		
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'
	
	four_tuple = (get_next_number('B'),\
				  prefix+"EQUAL",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_100():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		prefix = 'R'
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
		
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'
	
	four_tuple = (get_next_number('B'),\
				  prefix+"NOTEQUAL",\
				  semantic_stack[-3],\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number('B')
	
def analyze_production_101():
	pass
	
def analyze_production_102():
	pass
	
def analyze_production_103():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		
		prefix = 'R'
		
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
			
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'	
	temp=get_next_number(prefix)					
		
	four_tuple = (temp,\
				  prefix+"ADD",\
				  semantic_stack[-1],\
				  semantic_stack[-3])
	print_fourtuple(four_tuple)
	
	tuple_prag = []
        tuple_prag.append(temp)
        tuple_prag.append(prefix+"ADD")
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append(semantic_stack[-3])        
        tuple_prag.append("-")
        scope = 0
        pragy(tuple_prag, scope)







	
	semantic_stack[-3] = get_current_number(prefix)
	
def analyze_production_104():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		
		prefix = 'R'
		
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
		
#		print "HELLO...", semantic_stack[term_index]
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'						
	t=get_next_number(prefix)	
	four_tuple = (t,\
				  prefix+"MINUS",\
				  semantic_stack[-1],\
				  semantic_stack[-3])
	print_fourtuple(four_tuple)            
        tuple_prag = []
        tuple_prag.append(t)
        tuple_prag.append(prefix+"MINUS")
        tuple_prag.append(semantic_stack[-1])
        tuple_prag.append(semantic_stack[-3])
        tuple_prag.append("-")  
        
        scope = 0
        pragy(tuple_prag, scope)
	
	semantic_stack[-3] = get_current_number(prefix)
	
def analyze_production_105():
	global semantic_stack
	prefix = 'I'
	term_index = 0
	if(get_type(semantic_stack[-1])=="R"):
		term_index = 0.0
		prefix = 'R'
	four_tuple = (get_next_number(prefix),\
				  prefix+"MINUS",\
				  term_index,\
				  semantic_stack[-1])
	print_fourtuple(four_tuple)
	semantic_stack[-2] = get_current_number(prefix)
	
def analyze_production_106():
	pass
	
def analyze_production_107():
	pass
	
def analyze_production_108():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		
		prefix = 'R'
		
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
			
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'						
		
	four_tuple = (get_next_number(prefix),\
				  prefix+"MULT",\
				  semantic_stack[-1],\
				  semantic_stack[-3])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number(prefix)
	
def analyze_production_109():
	global semantic_stack
	prefix = 'R'
	if(check_mix_arithmatic(semantic_stack[-3],semantic_stack[-1])):
		
		prefix = 'R'
		
		term_index = 11
		if(get_type(semantic_stack[-3])=="R"):
			term_index = -1
		else:
			term_index = -3
			
		four_tuple = (get_next_number(prefix),\
					  "CONVERTIR",\
					  semantic_stack[term_index],\
					  None)
		print_fourtuple(four_tuple)	
		semantic_stack[term_index] = get_current_number(prefix)
			
#		semantic_stack[term_index] = float(semantic_stack[term_index])
	else:
		if(get_type(semantic_stack[-3])=="R"):
			prefix = 'R'
		else:
			prefix = 'I'						
		
	four_tuple = (get_next_number(prefix),\
				  prefix+"DIV",\
				  semantic_stack[-1],\
				  semantic_stack[-3])
	print_fourtuple(four_tuple)	
	semantic_stack[-3] = get_current_number(prefix)
	
def analyze_production_110():
	pass
	
def analyze_production_111():
	semantic_stack[-3] = semantic_stack[-2]
	
def analyze_production_112():
	pass
	
def analyze_production_113():
#	???
	pass
	
def analyze_production_114():
	global semantic_stack
	found_symbol = None
	prefix = 'R'
	
	if(find_in_localST(semantic_stack[-4])):
		found_symbol = get_from_localST(semantic_stack[-4])
	else: 
		if(find_in_globalST(semantic_stack[-4])):
			found_symbol = get_from_globalST(semantic_stack[-4])
		else:
			print "\t\tERROR:",semantic_stack[-4]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'VECTOR':
			print "\t\tERROR:",semantic_stack[-4],"is not a vector."
			return 
	
	if(get_from_ST(semantic_stack[-4])['TYPE'] == 'INTEGER'):
		prefix = 'I'
	else: 
		if(get_from_ST(semantic_stack[-4])['TYPE'] == 'REAL'):
			prefix = 'R'
			
	temp_number = get_next_number(prefix)
	four_tuple = (temp_number,\
				  "SUBLOAD",\
				  semantic_stack[-4],\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
 	tuple_prag = []
        tuple_prag.append(temp_number)
        tuple_prag.append("SUBLOAD")
        tuple_prag.append(semantic_stack[-4])
        tuple_prag.append(semantic_stack[-2])
       	temp = get_type(temp_number)
	if temp == 'I':
			tuple_prag.append('INTEGER')
	else:
			tuple_prag.append('REAL')        
        
        scope = 0
        pragy(tuple_prag, scope)  
	semantic_stack[-4] = get_current_number(prefix)
	
def analyze_production_115():
	global semantic_stack
	found_symbol = None
	
	if(find_in_localST(semantic_stack[-6])):
		found_symbol = get_from_localST(semantic_stack[-6])
	else: 
		if(find_in_globalST(semantic_stack[-6])):
			found_symbol = get_from_globalST(semantic_stack[-6])
		else:
			print "\t\tERROR:",semantic_stack[-6]," not found."
			return
			
	if (found_symbol):
		if found_symbol['SHAPE'] != 'MATRIX':
			print "\t\tERROR:",semantic_stack[-6],"is not a matrix."
			return
		
	if not check_if_aexpr_is_valid(semantic_stack[-4]):
		print "\t\tERROR:",semantic_stack[-4],"is not a valid index."
		return
	
	if not check_if_aexpr_is_valid(semantic_stack[-2]):
		print "\t\tERROR:",semantic_stack[-2],"is not a valid index."
		return
	
	prefix = 'I'
		
	four_tuple = (get_next_number(prefix),\
				  "IMULT",\
				  semantic_stack[-4],\
				  get_from_ST(semantic_stack[-6])['COLUMNS'])
	print_fourtuple(four_tuple)	
	
	temp_number = get_current_number(prefix)
	four_tuple = (get_next_number(prefix),\
				  "IADD",\
				  temp_number,\
				  semantic_stack[-2])
	print_fourtuple(four_tuple)
	temp_number = get_current_number(prefix)
	
	if(get_from_ST(semantic_stack[-6])['TYPE'] == 'INTEGER'):
		prefix = 'I'
	else: 
		if(get_from_ST(semantic_stack[-6])['TYPE'] == 'REAL'):
			prefix = 'R'
	
	four_tuple = (get_next_number(prefix),\
				  "SUBLOAD",\
				  semantic_stack[-6],\
				  temp_number)
	print_fourtuple(four_tuple)
	   
	semantic_stack[-6] = get_current_number(prefix)

def analyze_production_116():
#	???
	pass

def analyze_production_117():
#	???
	pass
	
