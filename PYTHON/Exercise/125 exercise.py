# 29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. \

# list1=['a','b','c']
# list2=['a','r','d']
# for i in list1:
#     if i not in list2:
#         print(i)

# 31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers

# num1= int(input())
# num2= int(input())
# i=1
# if num1>num2:
#     large=num1
# else:
#     large=num2
# for i in range(1,large):
#     if num1%i==0 and num2%i==0:
#         gcd=i

# print(gcd)

            
# 32. Write a Python program to get the least common multiple (LCM) of two positive integers. 
# 5 6 =30
# def compute_lcm(x, y):

#    # choose the greater number
#    if x > y:
#        greater = x
#    else:
#        greater = y

#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1

#    return lcm

# num1 = 54
# num2 = 24

# print("The L.C.M. is", compute_lcm(num1, num2))




#36 Write a Python program to add two objects if both objects are an integer type.
# def add_numbers(a, b):
#    if not (isinstance(a, int) and isinstance(b, int)):
#        return "Inputs must be integers!"
#    return a + b
# print(add_numbers(10, 20))
# print(add_numbers(10, 20.23))
# print(add_numbers('5', 6))
# print(add_numbers('5', '6'))