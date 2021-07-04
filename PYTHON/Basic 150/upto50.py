# s=input()
# print(s[::-1])

###################################

# we can print a string in modified way in one line using 4 ways including loop
#######################################

#####
# " * " symbol
s='suraj'
num=[1,2,3,4]  #
print(*s,sep=',')
# print(*num,sep=',')   doesnt work for int join only join string

print("by using join function")
print(','.join(s))
# print(','.join(num))  join only join the string

print("using map function")
print(','.join(map(str,s)))
print(','.join(map(str,num)))


str1=input().split()