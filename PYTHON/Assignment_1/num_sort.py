num1= int(input("enter first number"))
num2= int(input("enter second number"))
num3= int(input("enter third number"))
condition1=num3>num2>num1
condition2=num3>num1>num2
condition3=num2>num1>num3
condition4=num2>num3>num1
condition5=num1>num3>num2
if condition1:
    print("descending  order is",num3,num2,num1)
elif condition2:
    print("descending order is",num3,num1,num2)
elif condition3:
    print("descending order is",num2,num1,num3)
elif condition4:
    print("descending order is",num2,num3,num1)
elif condition5:
    print("descending order is",num1,num3,num2)

else:
    print("descending order is",num1,num2,num3)