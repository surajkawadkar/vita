num= int(input())
sum=0
while(num>0):
    power=len(str(num))
    temp_num=num
    last_digit=num%10
    sum=last_digit**power
    num=num//10
if temp_num==sum:
    print("armstrong number")
else:
    print("Not an armstrogn number")