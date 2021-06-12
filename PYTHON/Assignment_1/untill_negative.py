small,large=100,0
while(True):
    num= int(input("enter the number"))
    if num<0:
        break
    else:
        if large<num:
            large=num
        elif small>num:
            small=num
print(small,"small")
print(large,"large")

