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
name=input()
surname=input()
newstr=name+' '+surname
result=''
for i in newstr:
    result=i+result
print(result)