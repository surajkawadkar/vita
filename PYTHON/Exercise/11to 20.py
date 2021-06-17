# 11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).
# Sample function : abs()
# Expected Result :
# abs(number) -> number
# Return the absolute value of the argument.


# num= int(input())
# print(abs(num))

# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

# import calendar
# print(calendar.month(theyear=2021,themonth=7))



# 13. Write a Python program to print the following 'here document'. 
# Sample string :
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example



# print('''a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
# ''')

# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# import datetime
# f_date = datetime.date(2014, 7, 2)
# l_date = datetime.date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)

# 20. Write a Python program to get a string which is n (non-negative integer) copies of a given string. 
# def larger_string(str, n):
#    result = ""
#    for i in range(n):
#       result = result + str
#    return result

# print(larger_string('abc', 2))
# print(larger_string('.py', 3))