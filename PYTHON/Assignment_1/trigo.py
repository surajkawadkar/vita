#python does not support switch case
import math
print('''S – sin (x)	    		C – cos (x)
T – tan (x)		         	X – quit''')
choice=input("enter alphabet correspond to operation: ")
if choice=='S':
    x=float(input("enter the number: "))
    print(math.sin(x))
elif choice=='C':
    x=float(input("enter the number: "))
    print(math.cos(x))
elif choice=='T':
    x=float(input("enter the number: "))
    print(math.tan(x))
elif choice=='X':
    exit
else:
    print("Invalid choice.... kindly enter correct Alphabet")
