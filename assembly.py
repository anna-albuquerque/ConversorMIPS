entrada='entradaMIPS.txt'
stresult="Os códigos hexadecimais são: \n"
c=0
binstr=""
from nltk import tokenize
from nltk.tokenize import RegexpTokenizer
with open(entrada) as assemblyCode:
	text= assemblyCode.readlines()
	for line in text:
		tokenizer = RegexpTokenizer(r'\-*\w+')
		token=tokenizer.tokenize(line)
		if(token[0]=="addi"):
			binstr="001000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			if(int(token[3])>=0):
				binstr+='{0:016b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			else:
				binstr+='{0:016b}'.format(int(token[3]) & 0b1111111111111111)
		elif(token[0]=="add"):
			binstr="000000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+="00000100000"
		elif(token[0]=="and"):
			binstr="000000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+="00000100100"
		elif(token[0]=="or"):
			binstr="000000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+="00000100101"
		elif(token[0]=="xor"):
			binstr="000000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+="00000100110"
		elif(token[0]=="sub"):
			binstr="000000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+="00000100010"
		elif(token[0]=="slt"):
			binstr="000000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+="00000101010"
		elif(token[0]=="nor"):
			binstr="000000" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+="00000100111"
		elif(token[0]=="sll"):
			binstr="000000" #opcode
			binstr="00000" #ask for the s parameter
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+="000000"
		elif(token[0]=="slr"):
			binstr="000000" #opcode
			binstr="00000" #ask for the s parameter
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+="000010"
		elif(token[0]=="sw"):
			binstr="101011" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+='{0:016b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))#ASK IF iiii is equal to offset
		elif(token[0]=="lw"):
			binstr="100011" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+='{0:016b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))#ASK IF iiii is equal to offset
		elif(token[0]=="beq"):
			binstr="000100" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:016b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))#ASK IF iiii is equal to offset
		elif(token[0]=="syscall"):#syscall
			binstr="00000000000000000000000000001100"
		elif(token[0]=="bne"):
			binstr="000101" #opcode
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			binstr+='{0:05b}'.format(int(''.join(list(filter(str.isdigit, token[2])))))
			binstr+='{0:016b}'.format(int(''.join(list(filter(str.isdigit, token[3])))))#ASK IF iiii is equal to offset	
		elif(token[0]=="j"):
			binstr="000010" #opcode
			if(int(token[1])>=0):#could be negative
				binstr+='{0:026b}'.format(int(''.join(list(filter(str.isdigit, token[1])))))
			else:
				binstr+='{0:026b}'.format(int(token[1]) & 0b11111111111111111111111111)
		else:
			binstr="00000000000000000000000000000000"#wrong command
		stresult+=" " +str('0x%08x' % int(binstr, 2)).upper()[2:]+"\n"
		c+=1

assemblyCode.close()
n=1
for x in range(n):
	stresult +=" "
print(stresult)	