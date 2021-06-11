
# Some of the formulas used in today's Lab Session :
# Simple Interest= (Rate of Interest* Principal Amount*Time)/100
# Total Amount = Principal Amount+ Simple Interest
# 1 Feet = 12 inches
# 1 Inch= 2.5 cm
# 1 Hour= 60 Minutes
# 1 Minute = 60 Seconds
# therefore 1 Hour= 60* 60 Seconds


# inr =float(input())
# dollars = inr/73.05
# print(dollars)

# # total returm of  FD
# amt=float(input("amt"))
# interest=int(input("year"))
# ror=float(input("ror"))
# print("return is",(amt*interest*ror)+amt)


# total sec 
# hour=int(input("hours"))
# min=int(input("min"))
# sec=int(input("sec"))
# print("total sec =",(hour*60*60)+(min*60)+sec)

# seconds to hour min and sec
# sec=int(input("sec"))
# hour=sec//3600
# min=(sec%3600)//60
# seconds=sec-(sec//3600)-(sec+(sec//3600))
# print("total sec =",hour,min,seconds)


# cm to foo and inch
# height=float(input("enter in cm"))
# print("foot =",height//(2.5*12))
# print("inch",(height%12)//2.5)


# height=float(input("enter in cm"))
# feet=height//(2.54*12)
# print("foot =",feet)
# inch=(height%12)%2.5
# print("inch",inch)

# convet height into cm
# print("Height in cm is:",float(input("Enter height:"))*12*2.5)

# Bitwise Operator
x=10
print(oct(10))
print(bin(10))
print(hex(10))


# <<left shift and >> right shift


print(x<< 3) # 80-->multiply x by 3 times by 2 -->10*2=20-->20*2=40-->40*2=80
print(x>>2)

# tild ~ -->reverse the sign and subtract -1 ==eg~3:-3-1=-4
num=-132
print(num)

# tutorial
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print ("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 
print( "Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001
print ("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011
print ("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000
print ("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111
print ("Line 6 - Value of c is ", c)





