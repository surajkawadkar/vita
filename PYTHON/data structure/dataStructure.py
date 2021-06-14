

# reverse withpout using function
# list1=[11,22,33,44,55]

# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])


# a = [5, 2, 3, 1, 4]
# b=[55,88]
# a=a+b


# print(a)
# print(b)
# # print(ans)



# print number till user enter blank  and then show those which are above average 
#import numpy as np
# list1=[]
# while(True):
#     num=input()
#     if num=='':
#         break
#     else:
#         list1.append(float(num))
# print(list1)

# average=sum(list1)/len(list1) #average=np.mean(list1) 
# print(average)
# for i in list1:
#     if i>average:
#         print(i)

# add infinite elemebt in list and show ooccurances of that elenemebt in list
# list1=[]
# while(1):
#     num=input()
#     if num=='':
#         break
#     else:
#         list1.append(int(num))

# unique=set(list1)
# # newList=list(unique)
# for i in unique:
#     if i in list1:
#         print(i,"i",list1.count(i))
dictionary={0:'zero',
1:'one',
2:'two',
3:'three',
4:'four',
5:'five',
6:'six',
7:'seven',
8:'eight',
9:'nine'}
num= input()
for i in num:
    print(dictionary[int(i)])
