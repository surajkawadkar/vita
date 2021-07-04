# Given a number count the total number of digits in a number
# For example: The number is 75869, so the output should be
# num=75869
# count=0
# while(num>0):
#     num%10
#     count+=1
#     num=num//10
# print(count)




# Reverse the following list using for loop 
# list1 = [10, 20, 30, 40, 50] 
# Expected output: 
# 50 
# 40 
# 30 
# 20 
# 10 

# list1 = [10, 20, 30, 40, 50] 
# for i in range(-1,-len(list1),-1):
#     print(list1[i])






# 2. Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1 Expected Outcome: 
# appendMiddle("Chrisdem", IamNewString) → "ChrIamNewStringisdem" 

# s1='Chrisdem'
# s2='IamNewString'
# l_s1=len(s1)//2
# print(s1[:l_s1]+s2+s1[l_s1:])






# 3 Arrange String characters such that lowercase letters should come first 
# Given input String of combination of the lower and upper case arrange characters in such a way that all lowercase letters should come first. 
# Expected Output: 
# input_String = PyNaTive 
# arranging characters giving precedence to lowercase letters 
# aeiNPTvy 
# arranging characters giving precedence to lowercase letters: 
# yaivePNT 

# s1='PyNaTive'
# s2=''
# list1=list(s1)
# list1.sort()
# for i in list1:
#     if i.islower():
#         s2=i+s2
#     else:
#         s2=s2+i
# print(s2)

# 4. Given a string, return the sum and average of the digits that appear in the string, ignoring all other characters 
# For Example: – 
# sumAndAverage("English = 78 Science = 83 Math = 68 History = 65") = sum 294 Percentage is 73.5 Solution: 


# def sumAndAverage(e,s,m,h):
#     print('sum ',e+s+m+h)
#     print('avg ',(e+s+m+h)/4)
# English = 78; Science = 83; Math = 68; History = 65
# sumAndAverage(English,Science,Math,History)











# 5. Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second. 
# For Example: 
# listOne = [3, 6, 9, 12, 15, 18, 21] 
# listTwo = [4, 8, 12, 16, 20, 24, 28] 
# Expected Output: 
# Element at odd-index positions from list one 
# [6, 12, 18] 
# Element at even-index positions from list two 
# [4, 12, 20, 28] 
# Printing Final third list 
# [6, 12, 18, 4, 12, 20, 28]

# even=[]
# odd=[]
# listOne = [3, 6, 9, 12, 15, 18, 21] 
# listTwo = [4, 8, 12, 16, 20, 24, 28] 
# for i in range(1,len(listOne),2):
#     odd.append(listOne[i])   

# for i in range(0,len(listTwo),2):
#     even.append(listTwo[i])   
# print(odd+even)