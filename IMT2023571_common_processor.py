import time
global PC
global alpha
alpha=0.01
global exit_flag
exit_flag=False
def dectobin(a):
   s=""
   while(a):
      s+=str(a%2)
      a=a//2
    
   s=s[::-1]
   return (5-len(s))*'0'+s
def bintodec(binary):
    decimal = 0
    power = len(binary) - 1
    
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    
    return decimal
def decimal_to_binary(n):
  n=int(n)
  if (n >= 0):
    b = ""
    while n > 0:
      r = n % 2
      b = str(r) + b
      n //= 2
    a = len(b)
    if (a == 31):
      return ('0' + b)
    elif (a < 31):
      return ((32 - a) * '0' + b)
  else:
    n1 = -n
    i = 1
    while (n1 // (2**(i)) != 0):
      i += 1
    #print(i)
    i += 1  # value=5
    a = 2**(i - 1) - n1
    b = decimal_to_binary(a)
    b = b[-(i - 1):]
    b = ((32 - len(b)) * '1') + b
    return b
 
def binary_to_decimal(b_string):
  ret =0
  b_string=b_string[::-1]
  count=0
  for i in range(len(b_string)):
    if(i<len(b_string)-1):
      ret+=(2**count)*int(b_string[i])
    else:
      ret-=(2**count)*int(b_string[i])
    count+=1
  if(ret>=0):
    return str(ret)
  else:
    return '-'+str(-ret)
  

global regfile
regfile={}
for i in range(32):
  key=dectobin(i)
  regfile[key]="0"*32


def splitter(s):
    l=[]
    s1=s[:8]
    l.append(s1)
    s2=s[8:16]
    l.append(s2)
    s3=s[16:24]
    l.append(s3)
    s4=s[24:]
    l.append(s4)
    return l


global IF


IF={}

#file1 = open("IMT2023571_fibonacci_instruction_memory.txt", "r")
#file1 = open("IMT2023571_power_instruction_memory.txt", "r")
file1 = open("IMT2023571_factorial_instruction_memory.txt", "r")


def instruction_memory_generator():
  global IF
  i=12284
  for line in file1:
    ad1=decimal_to_binary(i)
    ad2=decimal_to_binary(i+1)
    ad3=decimal_to_binary(i+2)
    ad4=decimal_to_binary(i+3)
    l=splitter(line[:-1])
    IF[ad1]=l[0]
    IF[ad2]=l[1]
    IF[ad3]=l[2]
    IF[ad4]=l[3]
    i=i+4


#datafile=open("IMT2023571_fibonacci_data_memory.txt","r")
#datafile=open("IMT2023571_power_data_memory.txt","r")
datafile=open("IMT2023571_factorial_data_memory.txt","r")


global datamem
datamem={}
def data_generator():
    i=0
    for line in datafile:
        ad1=decimal_to_binary(i)
        ad2=decimal_to_binary(i+1)
        ad3=decimal_to_binary(i+2)
        ad4=decimal_to_binary(i+3)
        datamem[ad1]=line[:8]
        datamem[ad2]=line[8:16]
        datamem[ad3]=line[16:24]
        datamem[ad4]=line[24:-1]
        i+=4

PC=decimal_to_binary(12288)
global regdst
global jump
global branch
global memread
global aluop
global memwrite
global alusrc
global regwrite
global memtoreg
global op_generator
#global funct
op_generator = {}  #op_generator
#funct = {}
op_generator['001001']="li"
op_generator["100011"] = "lw"
op_generator["101011"] = "sw"
op_generator["000101"] = "bnq"
op_generator["000000"] = "sub"
#funct["100010"] = "sub"
op_generator["000000"] = "add"
#funct["100000"] = "add"
op_generator["001000"] = "addi"
op_generator["000100"] = "beq"
op_generator["000010"] = "j"
op_generator["000000"] = "move"
#funct["100001"] = "move"
op_generator["011100"]="mul"
op_generator['000000']="setless"
# funct["100011"]="subu"
# funct["000010"]="srl"
# funct["010000"]="mfhi"

#datafile=open("bindata.txt","r")







def control(opcode):
    global regdst
    global jump
    global branch
    global memread
    global aluop
    global memwrite
    global alusrc
    global regwrite
    global memtoreg

    if(opcode=="0"*6):
        regdst =1
        jump =0
        branch=0
        memread=0
        aluop=10
        memwrite=0
        alusrc=0
        regwrite=1
        memtoreg=0
    val=op_generator[opcode]
       
    if(val=="lw"):
        regdst =0
        jump =0
        branch=0
        memread=1
        aluop=0
        memwrite=0
        alusrc=1
        regwrite=1
        memtoreg=1
    if(val=="sw"):
        regdst =0
        jump =0
        branch=0
        memread=0
        aluop=0
        memwrite=1
        alusrc=1
        regwrite=0
        memtoreg=0
    if(val=="beq"):
        regdst =0
        jump =0
        branch=1
        memread=0
        aluop=1
        memwrite=0
        alusrc=0
        regwrite=0
        memtoreg=0
    if(val=="bnq"):
        regdst =0
        jump =0
        branch=1
        memread=0
        aluop=1
        memwrite=0
        alusrc=0
        regwrite=0
        memtoreg=0
    if(val=="j"):
        regdst =0
        jump =1
        branch=0
        memread=0
        aluop=0
        memwrite=0
        alusrc=1
        regwrite=0
        memtoreg=0
    if(val=="addi"):
        regdst =0
        jump =0
        branch=0
        memread=0
        aluop=0
        memwrite=0
        alusrc=1
        regwrite=1
        memtoreg=0
    if(val=="mul"):
        regdst =1
        jump =0
        branch=0
        memread=0
        aluop=11
        memwrite=0
        alusrc=0
        regwrite=1
        memtoreg=0

def add_(x,y):
   val1=int(binary_to_decimal(x))
   val2=int(binary_to_decimal(y))
   val=val1+val2
   return decimal_to_binary(val)

def sub_(x,y):
   val1=int(binary_to_decimal(x))
   val2=int(binary_to_decimal(y))
   val=val1-val2
   return decimal_to_binary(val)

def mul(x,y):
   val1=int(binary_to_decimal(x))
   val2=int(binary_to_decimal(y))
   return decimal_to_binary(val1*val2)
def setless(x,y):
   
   val1=int(binary_to_decimal(x))
   val2=int(binary_to_decimal(y))
   if(val1<val2):
      return "0"*31 +"1";
   else:
      return '0'*32







def writeback(data,a3):
    global alpha
    time.sleep(alpha)
    print("write back starts")
    global PC
    global regdst
    global jump
    global branch
    global memread
    global memtoreg
    global aluop
    global memwrite
    global alusrc
    global regwrite
    global memtoreg
    global regfile
    if(regwrite==1):
        print("writing back to memory")
        regfile[a3]=data
    else:
        print("no writing back required")
        pass
    print("write back ends")
    print()


def memory(aluresult,rd2,a3):
    global alpha
    time.sleep(alpha)
    print("Mem Access Starts")
    global PC
    global regdst
    global jump
    global branch
    global memread
    global memtoreg
    global aluop
    global memwrite
    global alusrc
    global regwrite
    global memtoreg
    global regfile
    data='0'*32
    

    if(memtoreg==0 and memwrite==0 and memread==0): #r format
        data=aluresult
        print("due to r type no mem access done")

     
    elif(memtoreg==0 and memwrite==1 and memread==0): #store
        
        datamem[aluresult]=rd2[:8]
        datamem[decimal_to_binary(int(binary_to_decimal(aluresult))+1)]=rd2[8:16]
        datamem[decimal_to_binary(int(binary_to_decimal(aluresult))+2)]=rd2[16:24]
        datamem[decimal_to_binary(int(binary_to_decimal(aluresult))+3)]=rd2[24:]
        print("store-> writing in the memory")
        print("Mem Access Ends")
        print()
        return
    elif(memtoreg==1 and memread==1 and memwrite==0):
       data=datamem[aluresult]+datamem[decimal_to_binary(int(binary_to_decimal(aluresult))+1)]+datamem[decimal_to_binary(int(binary_to_decimal(aluresult))+2)]+datamem[decimal_to_binary(int(binary_to_decimal(aluresult))+3)]
       print("load -> reading memory")
       
    print("Mem Access Ends")
    print()
    writeback(data,a3)



def execute(rd1,rd2,sign,fun,opcode,a3):
    global alpha
    time.sleep(alpha)
    print("execute started")
    global PC
    global regdst
    global jump
    global branch
    global memread
    global memtoreg
    global aluop
    global memwrite
    global alusrc
    global regwrite
    global memtoreg
    global regfile
       

    if(alusrc==0):
        alu2input=rd2
    else:
        alu2input=sign

    flag=0
    if(aluop==0):
        print("add called")       #load and store
        aluresult=add_(rd1,alu2input)
    elif(aluop==1): 
        print("sub called")      #beq and bne
        aluresult=sub_(rd1,alu2input)
        if(op_generator[opcode]=="beq"):
            if(int(binary_to_decimal(aluresult))==0):
                flag=1
            else:
                flag=0
        else:
            
            
            if(int(binary_to_decimal(aluresult))!=0):
                
                flag=1
            else:
                
                flag=0
    elif(aluop==10):
        if(fun=="100000"):
            print(type(rd1))
            print("add called")  
            aluresult=add_(rd1,alu2input)
        elif(fun=="100010"):
            print("sub called")  
            aluresult=sub_(rd1,alu2input)
        elif(fun=="101010"): #setonless
            print("set less called")  
            aluresult=setless(rd1,alu2input)
    elif(aluop==11):
        print("mul called")  
        aluresult=mul(rd1,alu2input)
    
    print("calculations done by alu-> ",binary_to_decimal(aluresult))
    if(flag==1 and branch==1):
        
        immediate=sign
        PC=decimal_to_binary(int(binary_to_decimal(PC)) + 4 + int(binary_to_decimal(immediate))*4)
        print("branch statements getting executed and following is the updated value of pc")
        print(binary_to_decimal(PC))
        print("ALU ends")
        print()
        return
    elif(branch==1 and flag==0):
       print("branch statements getting executed but the condition was not satisfied so normal pc incrementation")
       
       
       PC=decimal_to_binary(int(binary_to_decimal(PC))+4)
       print(binary_to_decimal(PC))
       print("ALU ends")
       print()
       return
    else:
        print("pc getting updated by 4")

        PC=decimal_to_binary(int(binary_to_decimal(PC))+4)
        print(binary_to_decimal(PC))
    print("ALU ends")
    print()
    if(type(aluresult)!=None):
        memory(aluresult,rd2,a3)
    

    
    





def decode(instruction):
    global alpha
    time.sleep(alpha)
    print("Decode Begins")
    global PC
    global regdst
    global jump
    global branch
    global memread
    global memtoreg
    global aluop
    global memwrite
    global alusrc
    global regwrite
    global memtoreg
    global regfile
    opcode=instruction[:6]
    print("Instruction's Opcode ",opcode)
    control(opcode)
    print("Control Signals Generated")
    print("regdst-",regdst)
    print("jump-",jump)
    print("branch-",branch)
    print("memread-",memread)
    print("memtoreg-",memtoreg)
    print("aluop-",aluop)
    print("memwrite-",memwrite)
    print("alusrc-",alusrc)
    print("regwrite-",regwrite)
    print("memtoreg-",memtoreg)
    if(jump==1):
        immediate=instruction[6:]
        PC="0000"+immediate+"00"
        return

    else:
        a1=instruction[6:11]
        a2=instruction[11:16]
        if(regdst==0):
            a3=instruction[11:16]
        else:
            a3=instruction[16:21]
        
        
        rd1=regfile[a1]
        rd2=regfile[a2]
        print("read data 1->" ,binary_to_decimal(rd1))
        print("read data 2->" ,binary_to_decimal(rd2))
        sign=instruction[16:]
        if(sign[0]=="1"):
            sign="1"*16+sign
        else:
            sign="0"*16+sign
        print("sign-> ",sign)
        fun=instruction[26:]
        print("function field-> ",fun)
        print("Decode finishes")
        print()
        execute(rd1,rd2,sign,fun,opcode,a3)
  
def fetch():
    global alpha
    time.sleep(alpha)
    print("Fetch Begins")
    global regfile
    global PC
    instruction=IF[PC]+IF[decimal_to_binary(int(binary_to_decimal(PC))+1)]+IF[decimal_to_binary(int(binary_to_decimal(PC))+2)]+IF[decimal_to_binary(int(binary_to_decimal(PC))+3)]
    print("Instruction Fetched  ",instruction)
    print("Fetch Ends")
    print()
    decode(instruction)


instruction_memory_generator()
data_generator()

#while(int(binary_to_decimal(PC))!=12328 and int(binary_to_decimal(PC))!=12344 and int(binary_to_decimal(PC))!=12380): #fibonacci
while(int(binary_to_decimal(PC))!=12336 and int(binary_to_decimal(PC))!=12348): #factorial
#while(int(binary_to_decimal(PC))!=12316 and int(binary_to_decimal(PC))!=12340):  #power
   fetch()
print()
print()
#print("final val",binary_to_decimal(regfile['01000'])) #fibonacci
print("final val",binary_to_decimal(regfile['01001']))#factorial
#print("final val",binary_to_decimal(regfile['10000']))#power





    
    
    
    

    



