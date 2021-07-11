import re
text= 'my name is suraj and my friend name is ram. i have a dell laptop,my laptop has 8gb ram'
regx='my'
print(re.findall(regx,text))
# find all 'my' in the given text


regx='^my'
# print string where start with 'my'
print(re.findall(regx,text))

regx='ram$'
# print string where ends with 'ram'
print(re.findall(regx,text))

regx='ram'
# print string 'ram' letter
print("all ram")
print(re.findall(regx,text))


regx='my'
# print string 'ram' letter
print("re.search return first occurance of regex match with indexes")
print(re.search(regx,text))


txt = "hello world"

#Search for a sequence that starts with "he",
#  followed by two (any) characters, and an "o":

# '.' dot is any character except newline
x = re.findall("he..o", txt)
print(x)
# ///////////////////////////////////////////
# * character

txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "ai" followed by 0 or more "x" characters:

x = re.findall("aix*", txt)

print(x)


# /////////////////////////
txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains "a" followed by exactly two "l" characters:

x = re.findall("al{2}", txt)

print(x)

################################
# or condition '|' character
txt = "The rain in Spain falls mainly in the plain!"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", txt)

print(x)


# ///////////////////////
txt = "The rain in Spain"

#Check if the string starts with "The":
print('|A character')
x = re.findall("\AThe", txt)

print(x)


# ///////////////////////////
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

print("character B")
x = re.findall(r"\Bain", txt)

print(x)

# //////////////////////////////////

txt = "The8 ra8in in Sp3ain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

# ////////////////////////////

txt = "The rain in Spain78946"

#Return a match at every no-digit character:
print('print only non digit ')
x = re.findall("\D", txt)

print(x)
# /////////////////////////////////
txt = "The rain in Spain"

#Return a match at every white-space character:
print('print whitespaces')
x = re.findall("\s", txt)

print(x)


# //////////////////////////////
txt = "The rain in Spain"

#Return a match at every NON white-space character:
print("does not contain white spaces")
x = re.findall("\S", txt)

print(x)


# ////////////////////////
txt = "The rain in Spain! #$%^&*"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)
# ///////////////////////////////////////
