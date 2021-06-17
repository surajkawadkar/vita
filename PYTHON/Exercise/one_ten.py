# 2. Write a Python program to get the Python version you are using. 
# import sys
# print(sys.version)


# 3. Write a Python program to display the current date and time.
# import datetime
# print(datetime.datetime.now())


# 4. Write a Python program which accepts the radius of a circle from the user and compute the area. 
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504


# r= int(input())
# print(2*3.14*r*r)


# 5. Write a Python program which accepts the user's first and last name and print 
# them in reverse order with a space between them. 
# name=input()
# surname=input()
# newstr=name+' '+surname
# result=''
# for i in newstr:
#     result=i+result
# print(result)

# 6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')
# --
# list1=[]
# while True:
#     data= input('enter the number')
#     if data=='':
#         break
#     list1.append(data)
# print(list1)
# print(tuple(list1))

# 7. Write a Python program to accept a filename from the user and print the extension of that. 
# Sample filename : abc.java
# Output : java

# filename=input()
# for i in range(len(filename)):
#     if filename[i]=='.':
#         print(filename[i+1:])


# 8. Write a Python program to display the first and last colors from the following list. 
# color_list = ["Red","Green","White" ,"Black"]

# color_list = ["Red","Green","White" ,"Black"]
# print(color_list[0],'and',color_list[-1])

# 9. Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014
op=''
exam_st_date = (11, 12, 2014)
for i in exam_st_date:
    op=op+'/'+str(i)
print(op[1:])