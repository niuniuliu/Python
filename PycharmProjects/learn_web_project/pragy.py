import re
myassem=[]
bss = ['SECTION .bss\nz1:    resd    1']
reals = []
myrealno = []
myglobal=[]
globalint=[]
mylocal=[]
localint=[]
globalint=[]
myassem=[]
count_myprint=0
printf_flag=0
datasec=[]
globreal=[]
cond = ''
oper=''
myv1=''
myv2=''
variable = {} #dictionary
section1 = ['SECTION .data\nformati:\tdb "%d",10,0,\nformatr:\tdb "%f",10,0'] 
registers = ['ebx','ecx','esi','edi','ebp','esp'] 
reg = {'eax':'','ebx':'','ecx':'','edx':'','esp':'','ebp':'','esi':'','edi':''} 
regex = re.compile('([a-z][a-zA-Z0-9]*)|([0-9]+)|([IR$]+[0-9]+)')
    
def regfind(nam,var):
    global variable,registers,reg
    for x in registers:
        if reg[x] == '':
            reg[x] = var
            variable[nam]= x
	    #print "variable[nam] is",variable[nam]
            return x
    print ('All registers  full')
def regclear():
 	global reg,variable,mylocal
  	variable = {}

    	mylocal = []
    	
    	reg = {'eax':'','ebx':'','ecx':'','edx':'','esi':'','edi':'','ebp':'','esp':''}  
def sub_loady(myvar,i) :

    if myvar in myglobal :
        #print('inside sub_load')
        if i in mylocal :
            my_instruct='mov\teax,'+ reg[variable[i]]
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='imul\teax,4'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='mov\teax,['+ myvar +' + eax]'
            myassem.append(my_instruct)
            #print(my_instruct)
        elif i in myglobal :
            my_instruct='mov\teax,['+i+']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='imul\teax,4'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='mov\teax,['+ myvar +' + eax]'
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,' + i
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='imul\teax,4'
            myassem.append(my_instruct)
            prin(tinstruction)
            my_instruct='mov\teax,['+ myvar + ' + eax]'
            myassem.append(my_instruct)
            #print(my_instruct)
 

def move(myvarname,var_value,var_index):
    var_value = str(var_value)
    myvarname = str(myvarname)
    var_index = str(var_index)
  
    if var_index == '-' :
        if myvarname in mylocal :
            if var_value in mylocal :
                my_instruct='mov\t'+reg[variable[myvarname]]+','+ reg[variable[var_value]]
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='mov\tdword [z1],'+ reg[variable[var_value]]
                myassem.append(my_instruct)
                #print(my_instruct)
            elif var_value in myglobal :
                my_instruct='mov\t'+reg[variable[myvarname]]+',['+var_value+']'
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='mov\tdword [z1],['+var_value+']'
                myassem.append(my_instruct)
                prin(my_instruct)
            else :
                my_instruct='mov\t'+reg[variable[myvarname]]+','+ str(var_value)
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='mov\tdword [z1],'+ var_value
                myassem.append(my_instruct)
                #print(my_instruct)
        elif myvarname in myglobal :
            if var_value in mylocal :
                my_instruct='mov\tdword ['+myvarname+'],'+ reg[variable[var_value]]
                myassem.append(my_instruct)
                #print(my_instruct)
            elif var_value in myglobal :
                var_in_global(var_value)
                my_instruct='mov\tdword ['+myvarname+'],eax'
                myassem.append(my_instruct)
                prin(my_instruct)
            else :
                my_instruct='mov\tdword ['+myvarname+'],'+ var_value
                myassem.append(my_instruct)
                #print(my_instruct)
        else :
            foundreg=regfind(myvarname,'1234')
            if var_value in mylocal :
                my_instruct='mov\t'+z+','+ reg[variable[var_value]]
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='mov\tdword [z1],'+ reg[variable[var_value]]
                myassem.append(my_instruct)
                #print(my_instruct)
            elif var_value in myglobal :
                var_in_global(var_value)
                my_instruct='mov\t'+z+',eax'
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='mov\tdword [z1],eax'
                myassem.append(my_instruct)
                #print(my_instruct)
            else :
                my_instruct='mov\t'+z+','+ var_value
                myassem.append(my_instruct)
               # print(my_instruct)
                my_instruct='mov\tdword [z1],'+ var_value
                myassem.append(my_instruct)
                #print(my_instruct)
    else :
        if myvarname in myglobal :
            if var_index in mylocal :
                my_instruct='mov\teax,'+ reg[variable[var_index]]
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='imul\teax,4'
                myassem.append(my_instruct)
                #print(my_instruct) 
            elif var_index in myglobal :
                my_instruct='mov\teax,['+var_index+']'
                myassem.append(my_instruct)
               # print(my_instruct)
                my_instruct='imul\teax,4'
                myassem.append(my_instruct)
                #print(my_instruct)
            else :
                my_instruct='mov\teax,' + var_index
                myassem.append(my_instruct)
               # print(my_instruct)
                my_instruct='imul\teax,4'
                myassem.append(my_instruct)
               # print(my_instruct)
                
            if var_value in mylocal :
                my_instruct='mov\tdword ['+myvarname+' + eax],'+ reg[variable[var_value]]
                myassem.append(my_instruct)
               # print(my_instruct)
            elif var_value in myglobal :
                my_instruct='mov\tedx,['+var_value+']'
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='mov\tdword ['+myvarname+' + eax],edx'
                myassem.append(my_instruct)
               # print(my_instruct)
            else :
                my_instruct='mov\tdword ['+myvarname+' + eax],'+ str(var_value)
                myassem.append(my_instruct)
               # print(my_instruct)
                        


def search(myvar):
    if myvar in mylocal :
        print('local declaration')
    elif myvar in myglobal :
        print('global declaration')
        
    else :                                  #load intermediate result 
        mylocal.append(myvar)
        #print('inside ')
        foundreg = regfind(myvar,'0')
        remove(myvar,'')
        regfind(myvar,foundreg)
        #print('z',foundreg,myvar)

def real_add(p,q,r) :
    global myglobal,print_mycounter
    if p in myglobal :
        instrucion = 'fld\tdword ['+p+']'
        myassem.append(my_instruct)
        #print(my_instruct)
    my_instruct = 'fld\tdword ['+q+']'
    myassem.append(my_instruct)
   # print(my_instruct)
    my_instruct1 = 'faddp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\n'
    my_instruct2='push ' + 'stmt' + str(print_mycounter+1)
    my_instruct = my_instruct1 + my_instruct2 + '\ncall\tprintf\nadd\tesp,12'
    myassem.append(my_instruct)
   # print(my_instruct)

def real_sub(p,q,r) :
    global myglobal,count_myprint
    if p in myglobal :
        my_instruct = 'fld\tdword ['+q+']'
        myassem.append(my_instruct)
       # print(my_instruct)
    my_instruct = 'fld\tdword ['+p+']'
    myassem.append(my_instruct)
   # print(my_instruct)
    my_instruct1= 'fsubp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\n'
    my_instruct2='push ' + 'stmt' + str(count_myprint+1)
    my_instruct= my_instruct1 + my_instruct2 + '\ncall\tprintf\nadd\tesp,12'
    myassem.append(my_instruct) 
    #print(my_instruct)
            




def remove(nam,var):
    global variable,reg
    print "nam is",nam," var is",var
    print "reg[variable[nam]]=",reg[variable[nam]]
    #reg[variable[nam]] = ''
    reg[variable[nam]] = ''
    variable.pop(nam)

def generate_my_instruct(myvarname):
    global variable,reg
    if myvarname in mylocal :
        #print('reg',vari)
        my_instruct='mov\t'+ reg[variable[myvarname]] + ',eax'
        myassem.append(my_instruct)
        #print(my_instruct)
    elif myvarname in myglobal :
        my_instruct='mov\tdword ['+ myvarname + '],eax'
        myassem.append(my_instruct)
        #print(my_instruct)
    else :                                        #intermediate result
        foundreg = regfind(myvarname,'0')
        my_instruct='mov\t'+ foundreg + ',eax'
        myassem.append(my_instruct)
        #print(my_instruct)



def printmyvar(myvar):
    global count_myprint
    if myvar in mylocal :                                                
        if myvar in globalint or myvar in localint:         
            my_instruct='push\tdword [z1]'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='push ' + 'stmt' + str(count_myprint)
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='call printf'
            myassem.append(my_instruct)
            #print(my_instruct)
        elif myvar in myrealno :
            my_instruct='push ' + 'stmt' + str(count_myprint)
    elif myvar in myglobal :
        if myvar in globalint or myvar in localint :
            my_instruct='push\tdword ['+ myvar +']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='push ' + 'stmt' + str(count_myprint)
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='call printf'
            myassem.append(my_instruct)
            #print(my_instruct)
        elif myvar in myrealno :
             my_instruct='push ' + 'stmt' + str(count_myprint)
    else :
        if myvar in globalint or myvar in localint :
            my_instruct='push\t[z1]'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='push ' + 'stmt' + str(count_myprint)
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='call printf'
            myassem.append(my_instruct)
            #print(my_instruct)
        elif myvar in myrealno :
            my_instruct='push ' + 'stmt' + str(count_myprint)

def compare(var1,var2) :
    var1 = str(var1)
    var2 = str(var2)
    if var1 in mylocal :
        if var2 in mylocal :
            #print('var1 in local and var2 in local',var2)
            my_instruct='cmp\t'+reg[variable[var1]]+','+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            #print('var1 in local and var2 in global',var2)
            my_instruct='cmp\t'+reg[variable[var1]]+',['+var2+']' 
            myassem.append(my_instruct)
            #print(my_instruct)
            remove(var2,'')
        else :
            my_instruct='cmp\t'+reg[variable[var1]]+','+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
    elif var1 in myglobal :
        if var2 in mylocal :
            #print('var1 in global and var2 in ',var2)
            my_instruct='cmp\t['+var1+'],'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            #print('var1 in global and var2 in global',var2)
            my_instruct='mov\teax,['+var1+']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='cmp\teax,['+ var2 +']'
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='cmp\tdword ['+var1+'],'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
    else :
        if var2 in mylocal :
            #print('var2 in local',var2)
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='cmp\teax,'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            #print('var2 in global',var2)
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='cmp\teax,['+ var2+']'
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='cmp\teax,'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
    
    ss_output = regex.findall(var1)
    if ss_output[0][2] != '' :
        remove(var1,'')
    ss_output = regex.findall(var2)
    if ss_output[0][2] != '' :
        remove(var2,'')


def addition(var1,var2):
    var1 = str(var1)
    var2 = str(var2)
    if var1 in mylocal :
        if var2 in mylocal :
            my_instruct='mov\teax,'+ reg[variable[var1]]
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            my_instruct='mov\teax,'+ reg[variable[var1]]
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,['+var2+']' 
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,'+ reg[variable[var1]]
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
    elif var1 in myglobal :
        if var2 in mylocal :
            my_instruct='mov\teax,['+ var1 +']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            my_instruct='mov\teax,['+var1+']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,['+ var2 +']'
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,['+ var1 +']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
    else :
        if var2 in mylocal :
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,['+var2+']' 
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='add\teax,'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
def subtraction(var1,var2):
    var1 = str(var1)
    var2 = str(var2)
    if var1 in mylocal :
        if var2 in mylocal :
            my_instruct='mov\teax,'+ reg[variable[var1]]
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            my_instruct='mov\teax,'+ reg[variable[var1]]
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,['+var2+']' 
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,'+ reg[variable[var1]]
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
    elif var1 in myglobal :
        if var2 in mylocal :
            my_instruct='mov\teax,['+ var1 +']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            my_instruct='mov\teax,['+var1+']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,['+ var2 +']'
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,['+ var1 +']'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)
    else :
        if var2 in mylocal :
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,'+ reg[variable[var2]]
            myassem.append(my_instruct)
            #print(my_instruct)
        elif var2 in myglobal :
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,['+var2+']' 
            myassem.append(my_instruct)
            #print(my_instruct)
        else :
            my_instruct='mov\teax,'+ var1
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='sub\teax,'+ var2
            myassem.append(my_instruct)
            #print(my_instruct)     
def printarray(arr_name,index):
    global count_myprint,myrealno
    if arr_name in myglobal :
        if arr_name in globalint or arr_name in localint :
            if index in mylocal :
                my_instruct='mov\teax,'+ reg[flags.var_reg[index]]
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='imul\teax,4'
                myassem.append(my_instruct)
                #print(my_instruct)
            elif index in myglobal :
                my_instruct='mov\teax,['+index+']'
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='imul\teax,4'
                myassem.append(my_instruct)
                #print(my_instruct) 
            else :
                my_instruct='mov\teax,' + index
                myassem.append(my_instruct)
                #print(my_instruct)
                my_instruct='imul\teax,4'
                myassem.append(my_instruct)
                #print(my_instruct)  
            my_instruct='push\tdword ['+ arr_name +' + eax]'
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='push ' + 'stmt' + str(count_myprint)
            myassem.append(my_instruct)
            #print(my_instruct)
            my_instruct='call printf'
            myassem.append(my_instruct)
            #print(my_instruct)
        elif arr_name in myrealno :
            my_instruct='push ' + 'stmt' + str(count_myprint)           



def pragy(mytuple,myscope):
	
	print "MYTUPLE",mytuple," myscope ",myscope
	global mylocal,myglobal,localint,globalint,myassem,reals,section1,bss,printf_flag,variable,reg,cond,count_myprint,datasec,globreal
	if mytuple[1] == "BEGINPROGRAM":
	        myasmname = mytuple[0] + ".asm"
	        myassem.append(myasmname)
	        #print(myasmname)

	elif  mytuple[1] == "ENDPROGRAM":
		print "HELLO END"
		my_instruct = 'mov esp, ebp\npop dword ebp'  #refer pragmanotes file
		myassem.append(my_instruct)
		#print(my_instruct)
		my_instruct = 'ret\n'
		myassem.append(my_instruct)
		#print(my_instruct)
		handl = open(myassem[0],'w+')
		myassem.pop(0)
		handl.write('global main\nextern printf\n')
		handl.write("SECTION .data\n")
		for mystr in myrealno:
		    mystr = mystr +  ':\tresd\t1'
		    bss.append(mystr)
		for d in datasec:
            		handl.write(d)
		for mystr in bss:
		    mystr = mystr + '\n'
		    handl.write(mystr)
		for mystr in myassem:
		    mystr = mystr + '\n'
		    handl.write(mystr)
		handl.close()


	elif mytuple[1] == 'ENDDECLARATIONS' and myscope == 0:
        	myassem.append('SECTION .text\n')
        	#print('SECTION .text\n')

	elif mytuple[1] == "MEMORY" and myscope == 0 and mytuple[4] == "INTEGER":
		print "INISDE global MEM"
  		globalint.append(mytuple[0])
	                                                       #scalar
		my_instruct = mytuple[0] + ':\tresd\t' + str(mytuple[2])
		
		myglobal.append(mytuple[0])
		bss.append(my_instruct)
		for k in range(0,len(myglobal)):
			print "MY GLOBAL",myglobal[k]			
		print "MY INSTRUCT IS",my_instruct
	elif mytuple[1] == "MEMORY" and myscope == 1 and mytuple[4] == "INTEGER":
 		print "inside memory local"
        	localint.append(mytuple[0])
       		print "mytemp prag" , myscope
        	k=0
        
		if mytuple[2] == '1':                    
		    print "inside inside local"
		    foundreg = regfind(mytuple[0], '0')      #find empty register and put value
		    remove(mytuple[0],'')               
		    print "found reg:",foundreg
		    regfind(mytuple[0],foundreg)               
		    mylocal.append(mytuple[0])
    	elif mytuple[1] == 'MEMORY' and myscope == 0 and mytuple[4] == 'REAL':      

		globreal.append(mytuple[0])
		if mytuple[2] == '1':
		     myglobal.append(mytuple[0])
		     myrealno.append(mytuple[0])
		
    	elif mytuple[1] == 'ENDPROCEDURE':
		

		regclear()
		my_instruct = 'mov esp, ebp\npop dword ebp'
		myassem.append(my_instruct)
		#print(my_instruct) 
		my_instruct = 'ret'
		myassem.append(my_instruct)
		#print(my_instruct)

	elif mytuple[1] == 'BEGINPROCEDURE':
		regclear()
		my_instruct = mytuple[2] + ':\t'
		myassem.append(my_instruct)
		#print(my_instruct)
		my_instruct = 'push ebp\nmov ebp, esp'
		myassem.append(my_instruct)
		#print(my_instruct)

		 
    	elif mytuple[1] == 'LABEL':
		if mytuple[0] == 'MAIN':
		    my_instruct = mytuple[0].lower() + ':\t'
		    myassem.append(my_instruct)
		    #print(my_instruct)
		    my_instruct = 'push ebp\nmov ebp, esp' 
		    myassem.append(my_instruct)
		    #print(my_instruct)
		else:
		    my_instruct = mytuple[0] + ':\t'
		    myassem.append(my_instruct)
		    #print(my_instruct)

 	elif mytuple[1] == 'JUMP':
        	my_instruct = 'jmp\t'+mytuple[0]
        	myassem.append(my_instruct)
        	#print(my_instruct)


	elif mytuple[1] == 'SUBSTORE' :
		search(mytuple[0])
		move(mytuple[0],mytuple[2],mytuple[3])
		ss_output = regex.findall(str(mytuple[2]))
		print " findall ss_output:"
		for k in range (0,len(ss_output)):
		    print ss_output[k] , " , "
		if ss_output[0][2] != '' :
		    remove(mytuple[2],'')
		ss_output = regex.findall(str(mytuple[3]))
		if ss_output[0][2] != '' :
		    remove(mytuple[3],'')

	elif mytuple[1] == 'STORE':
		
		myassem.append(";("+str(mytuple[0])+","+str(mytuple[1])+","+str(mytuple[2])+","+str(mytuple[3])+")") 
		if mytuple[4] == 'REAL':
		    mytuple[2] = str(mytuple[2])
		    if mytuple[2][1] == '$':
		        
		        
		        search(str(mytuple[0]))
		        global myv1,myv2,oper
		       
		        if oper == 'realaddition' :
		            real_add(str(myv1),str(myv2),str(mytuple[0]))
		        elif oper == 'realsubtraction' :
		            real_sub(str(myv1),str(myv2),str(mytuple[0]))
		        output = regex.findall(str(mytuple[2]))
		        if output[0][2] != '' :
		            remove(mytuple[2],'')
		    else:
		        search(mytuple[0])
		        if mytuple[0] in myrealno :
		            my_instruct = mytuple[0]+':\t dd\t'+mytuple[2] + '\n'
		            datasec.append(my_instruct)
		            for i in range(len(myrealno)) :
		                if myrealno[i] == mytuple[0] :
		                    tindex = i
		            myrealno.pop(tindex)
		        output = regex.findall(mytuple[2])
		        if output[0][2] != '' :
		            remove(mytuple[2],'')


		elif mytuple[4] == 'INTEGER':
		    search(mytuple[0])
		    move(mytuple[0],mytuple[2],mytuple[3])
		    output = regex.findall(str(mytuple[2]))
		    if output[0][2] != '' :
		        remove(mytuple[2],'')




	elif mytuple[1] == 'CALLPROCEDURE' :
        
        	if mytuple[0] == 'printf' :
            		printf_flag  = 1

	elif mytuple[1] == 'VALUEACTUALPARAMETER' and mytuple[0] == '#'  :
      
        	if mytuple[2] != '" "' and printf_flag == 1 :
            		if mytuple[3] != '-':
               
                		printarray(mytuple[2],str(mytuple[3]))

            		elif mytuple[3] == '-':
             
                		printmyvar(mytuple[2])
        	printf_flag = 0  
    
	elif mytuple[1] == 'SUBLOAD' :
		if mytuple[4] == 'INTEGER':
		    #print('inside integer')
		    search(mytuple[0])
		    sub_loady(mytuple[2],mytuple[3])
		    generate_my_instruct(mytuple[0])
		    output = regex.findall(str(mytuple[2]))
		    if output[0][2] != '' :
		        #print('output',output[0][2][2])
		        remove(mytuple[2],'')
		    output = regex.findall(str(mytuple[3]))
		    if output[0][2] != '' :
		        if output[0][2][1] == '$' :
		            #print('output',output[0][2][1])
		            remove(mytuple[3],'') 


     

  


 	
	elif mytuple[1] == 'ILT' :
		cond = 'LT'
		compare(mytuple[2],mytuple[3])
		                                        
	elif mytuple[1] == 'IGT' :
		cond = 'GT'
		compare(mytuple[2],mytuple[3])
		                                        
	elif mytuple[1] == 'ILTEQ' :
		cond = 'LTEQ'
		compare(mytuple[2],mytuple[3])
		                                        
	elif mytuple[1] == 'IGTEQ' :
		cond = 'GTEQ'
		compare(mytuple[2],mytuple[3])                
		                        
	elif mytuple[1] == 'IEQ' :
		cond = 'EQ'
		compare(mytuple[2],mytuple[3])
		                                        
	elif mytuple[1] == 'INOTEQ' :
		cond = 'NOTEQ'
		compare(mytuple[2],mytuple[3])
                        
	elif mytuple[1] == 'CJUMPT':
		if cond == 'LT' :
		    my_instruct = 'jl\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'GT' :
		    my_instruct = 'jg\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'LTEQ' :
		    my_instruct = 'jle\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'GTEQ' :
		    my_instruct = 'jge\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'EQ' :
		    my_instruct = 'je\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'NOTEQ' :
		    my_instruct = 'jne\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)	

	elif mytuple[1] == 'CJUMPF':
		if cond == 'LT' :
		    my_instruct = 'jge\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'GT' :
		    my_instruct = 'jle\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'LTEQ' :
		    my_instruct = 'jg\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'GTEQ' :
		    my_instruct = 'jl\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'EQ' :
		    my_instruct = 'je\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		elif cond == 'NOTEQ' :
		    my_instruct = 'jne\t'+mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)	

	elif mytuple[1] == 'IADD' :
		search(mytuple[0])
	
		addition(mytuple[2],mytuple[3])
		
		generate_my_instruct(mytuple[0])
		
		ss_output = regex.findall(mytuple[2])
		if ss_output[0][2] != '' :
		    remove(mytuple[2],'')
		
		ss_output = regex.findall(str(mytuple[3]))
		if ss_output[0][2] != '' :
		    remove(mytuple[3],'')

	elif mytuple[1] == 'VALUE' :
		foundreg = regfind(mytuple[0],'0123')
		remove(mytuple[0],'')
		regfind(mytuple[0],foundreg)
		mylocal.append(mytuple[0])
	

	elif mytuple[1] == 'PROCCALL' :
		    my_instruct ='call\t'+ mytuple[0]
		    myassem.append(my_instruct)
		    #print(my_instruct)
		        
	elif mytuple[1] == 'REFERENCEACTUALPARAMETER' :
		output = regex.findall(str(mytuple[0]))
		if output[0][2] != '' :
		    remove(mytuple[0],'')

	elif mytuple[1] == 'IMINUS' :
		search(mytuple[0])
		subtraction(mytuple[2],mytuple[3])
		gen_final_my_instruct(mytuple[0])
		output = regex.findall(str(mytuple[2]))
		if output[0][2] != '' :
		    remove(mytuple[2],'')
		output = regex.findall(mytuple[3])
		if output[0][2] != '' :
		    remove(mytuple[3],'')
		
	
		'''		       
		for k in range(0,len(mylocal)):
			print "MY LOCAL",mylocal[k]
		      
		for k in range(0,len(myglobal)):
			print "MY GLOBAL",myglobal[k]
		'''

	elif mytuple[1] == 'VALUEACTUALPARAMETER':
        	myassem.append(";("+str(mytuple[0])+","+str(mytuple[1])+","+str(mytuple[2])+","+str(mytuple[3])+")")
       
        	count_myprint = count_myprint + 1
		datasec.append("stmt"+str(count_myprint)+":\t"+"db\t"+str(mytuple[2])+",10,0\n")

	elif mytuple[1] == 'FLAG':
		myassem.append(";("+str(mytuple[0])+","+str(mytuple[1])+","+str(mytuple[2])+","+str(mytuple[3])+")")


	elif mytuple[1] == 'RMINUS' :
		search(mytuple[0])
		global myv1
		global myv2
		global oper
		oper = 'realsubtraction'
		myv1 = mytuple[2]
		myv2 = mytuple[3]
		output = regex.findall(mytuple[2])
		if output[0][2] != '' :
		    remove(mytuple[2],'')
		output = regex.findall(mytuple[3])
		if output[0][2] != '' :
		    remove(mytuple[3],'')

	elif mytuple[1] == 'RADD' :
		search(mytuple[0])
		global myv1
		global myv2
		global oper
		oper = 'realaddition'
		myv1 = mytuple[2]
		myv2 = mytuple[3]
		output = regex.findall(mytuple[2])
		if output[0][2] != '' :
		    remove(mytuple[2],'')
		output = regex.findall(mytuple[3])
		if output[0][2] != '' :
		    remove(mytuple[3],'')






	
	
