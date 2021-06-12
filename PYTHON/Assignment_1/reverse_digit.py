rev_d=0
num= int(input())
while(num>0):
    last_d=num%10
    rev_d=rev_d*10+last_d
    num=num//10
print(rev_d)