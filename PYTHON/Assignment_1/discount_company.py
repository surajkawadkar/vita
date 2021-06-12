print('''   Product \t	Code \n
Music system	\t 1
Television set	\t 2
Refrigerator	\t 3
''')
choice=int(input("enter respective code whch you wish to buy "))
if choice==1:
    order=float(input("amount to be paid for Music system"))
    if order>15000:
        discount=(order*12)/100
        print("Discount is ",discount)
    elif order>8000:
        discount=(order*8)/100
        print("Discount is ",discount)
    else:
        discount=(order*2)/100
        print("Discount is ",discount)



elif choice==2:
    order=float(input("amount to be paid for TV"))
    if order>70000:
        discount=(order*11)/100
        print("Discount is ",discount)
    else:
        discount=(order*6)/100
        print("Discount is ",discount)
    
elif choice==3:
    order=float(input("amount to be paid for Refrigerator"))
    if order>50000:
        discount=(order*10)/100
        print("Discount is ",discount)

    else:
        discount=(order*5)/100
        print("Discount is ",discount)

else:
    print("Invalid")