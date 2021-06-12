print('''1- Additon
2--Subtraction
3--multip;ication
4--exit''')
choice=int(input("enter the number corresponds to operation: "))
if choice==1:
    a,b=map(float,(input("enter the numbers: ")).split())
    print(a+b)
elif choice==2:
    a,b=map(float,(input("enter the numbers: ")).split())
    print(a-b)
elif choice==3:

    a,b=map(float,(input("enter the numbers: ")).split())
    print(a*b)
elif choice==4:
    exit
else:
    print("Invalid choice.... kindly enter correct number")