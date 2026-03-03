#Python has a built-in package called re, which can be used to work with Regular Expressions.
#Import the re module:
import re

#1
import re
txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

#2
import re
txt = "That will be 59 dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)

#3
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

#4
import re
txt = "hello planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


#5
import re
txt = "hello planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)


#6
import re
txt = "8 times before 11:45 AM"
#Check if the string has any digits:
x = re.findall("[0-9]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#7
import re
txt = "8 times before 11:45 AM"
#Check if the string has any characters from a to z lower case, and A to Z upper case:
x = re.findall("[a-zA-Z]", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


#8
#The split() function returns a list where the string has been split at each match:
#Split at each white-space character:
#Split the string only at the first occurrence:
import re
txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) 


#9
#The sub() function replaces the matches with the text of your choice:
#Replace every white-space character with the number 9:
#Replace the first 2 occurrences:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
 