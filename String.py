# string are the combination of characters which are used to store the data in the form of text

# string are the immutable data types which means we cannot change the value of the string once it is created

# functions of string part 1

# len
# indexing
# slicing
# concatenation
# repetition
# escape sequence
#count
# find
# upper
# lower
# title
# strip
# replace
#index
#format

#example

name = "john"
print(name)
print(type(name))
print(len(name))

print(name[0])
print(name[1])
print(name[2])
print(name[3])

print(name[-1])

print(name[0:4])
print(name[0:3])
print(name[1:4])
print(name[0:4:2])

print(name + " doe")
print(name * 3)

print("john's car")
print("john\"s car")
print('john\'s car')
print("john\ns car")
print("john\tcar")

print(name.count("o"))

print(name.find("o"))

print(name.upper())

print(name.lower())

print(name.title())

print(name.strip("j"))

print(name.replace("j", "J"))

print(name.index("o"))

print("my name is {} and i am {} years old".format("john", 25))

print("my name is {0} and i am {1} years old".format("john", 25))
print("my name is {name} and i am {age} years old".format(name="john", age=25))

print(name.capitalize())

#string part 2
#string functions are used to perform various operations on the string such as counting the number of characters, find the index of a characters, converting the string to upper case,
#  lower case, title case, stripping the white spaces, replacing the characters, etc.   

# isalpha - it is used to check whether the string contains only alphabets or not. It returns True if the string contains only alphabets, otherwise it returns False.
# isdigit -  digits or not. It returns True if the string contains only digits, otherwise it returns False.
# isspace -  white spaces or not. It returns True if the string contains only white spaces, otherwise it returns False.
# isalnum -  alphanumeric characters or not. It returns True if the string contains only alphanumeric characters, otherwise it returns False.
# islower - It returns True if the string contains only lowercase characters, otherwise it returns False.
# isupper - only uppercase characters or not. It returns True if the string contains only uppercase characters, otherwise it returns False.
# numeric - It returns True if the string contains only numeric characters, otherwise it returns False.
# isdecimal - It returns True if the string contains only decimal characters, otherwise it returns False.
# istitle - It returns True if the string contains only title case characters, otherwise it returns False.

print(name.isalpha())
print(name.isdigit())
print(name.isspace())
print(name.isalnum())
print(name.islower())
print(name.isupper())
print(name.isnumeric())
print(name.isdecimal())
print(name.istitle())


# string part 3
# endswith - it is used to check whether the string ends with a specific character or not. It returns True if the string ends with the specified character, otherwise it returns False.
# startswith - It returns True if the string starts with the specified character, otherwise it returns False.
# split - it is used to split the string into a list of substrings based on a
#  specific delimiter. It returns a list of substrings.
# strip - It returns a new string with the leading and trailing white spaces removed.
# join - it is used to join the list of substrings into a single string based on a specific delimiter. It returns a single string.
# ljust - It returns a new string with the specified width and the original string is left justified.


# example
print(name.endswith("n"))
print(name.endswith("o"))
print(name.startswith("j"))
print(name.split("o"))
print(name.strip("j"))
print("-".join(name.split("o")))
print(name.ljust(10, "*"))

 




