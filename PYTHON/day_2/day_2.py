# minmum number
# num1=int(input())
# num2=int(input())
# num3=int(input())
# if(num1<num2 and num2<num3):
#     print(num1)

# elif (num2<num3 and num2<num1):
#     print(num2)
# else:
#     print(num3)

# grades of a student
# perc=float(input())
# if perc>60:
#     print("first class")
# elif perc>=50:
#     print("second class")
# elif perc>=40:
#     print("pass")
# else:
#     print("fail")

# for i in range(1,10,1):
#     if i==3:
#         break
#     print(i)

# dicisible by 5 and 3
# for i in range(1,101,3):
#     if(i%5==0):
#         print(i)

# accept input from user till user does not enter nothing and hit enter and find sum and avg
# sum=0
# while(1):
#     x=input()
#     if x='':
#         break

    
#     sum+=float(x)
# print(sum)
# print(sum/num)

# Factorial
# fact=1
# num=int(input())
# for i in range(1,num+1):
#     fact*=i
# print(fact)

num= int(input())
sum=0
while(num>0):
    rem=num%10
    sum+=rem
    num=num//10
print(sum)

