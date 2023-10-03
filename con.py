#!/usr/local/bin/python3.10

# imports
import sys


# in this code we will convert values like binary/octal/hexadecimal/deciaml/text to each other




# check if arguments are right
if ( len(sys.argv) < 4 
    or sys.argv[1] == "?" 
    or not sys.argv[1] in "DBOHT" 
    or not sys.argv[2] in "DBOHT" ):

    
    print("con [D,B,O,H,T] [D,B,O,H,T] value \n\n"
          + "convert value from base1 to base2 \n"
          + "D Deciaml \n"
          + "B Binary \n"
          + "O Octal \n"
          + "H Hexadeciaml \n"
          + "T Text")

    exit()



# values
val = sys.argv[3:]
B1 = sys.argv[1]
B2 = sys.argv[2]


# here just split if input is without spaces hex
if B1 == "H" and len(val) == 1 :
    for i in range(0 , len(val[0]) , 2):
        val.append( val[0][i] + val[0][i+1] )
    
    del val[0]

if B1 == 'T' :
    val = list(val[0])



# convert
for N in val:

    if B1 == "B":
        N = int(N,2)
    elif B1 == "O":
        N = int(N,8)
    elif B1 == "H":
        N = int(N,16)
    elif B1 == "T":
        N = ord(N)

    N = int(N)
    R = N

    if B2 == "B":
        R = bin(N)
        R = R[2:]
    elif B2 == "O":
        R = oct(N)
        R = R[2:]
    elif B2 == "H":
        R = hex(N)
        R = R[2:]
    elif B2 == "T":
        R = chr(N)
    

    print(R,end="")

print()