start= int(input())
end= int(input())
for num in range(start,end):
    temp_num=num
    power=len(str(num))
    sum=0
    while(num>0):
        last_digit=num%10
        sum+=last_digit**power
        num=num//10
        
        if sum==temp_num:
            print(temp_num,end=',')

