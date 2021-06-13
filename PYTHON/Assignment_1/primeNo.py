num1= int(input("first no"))
num2= int(input("second no"))
i=2
flag=0
for i in range(num1,num2+1):
    for j in range(2,i):
        flag=0
        if i%j==0:
            break

        else:
            flag=1
            #print(i,end=',')
    if flag==1:
        print(i,end=',')