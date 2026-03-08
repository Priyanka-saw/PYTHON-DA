# conditional statement - it is used to perform different actions based on different conditions only if the condition is true then the block of code will be executed otherwise it will be skipped

# types of conditioanl statements with examples

# 1. if statement
# if statement - it is used to execute a block of code only if a specified condition is true    
age = 18
if age >= 18:
    print("you are eligible to vote")


# 2.if else statement
# if else statement - it is used to execute a block of code if a specified condition is true, and another block of code if the condition is false
age = 16    
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# 3. if elif statment
# if elif else statement - it is used to execute a block of code if a specified condition is true, and another block of code if the condition is false, and another block of code if the condition is false
age = 65
if age < 18:
    print("you are a child")
elif age < 60:
    print("you are an adult")
else:
    print("you are a senior citizen")

# 4.nested statment 
# nested if statement - it is used to check multiple conditions in a single block of code
age = 25
if age < 18:
    print("you are a child")
else:
    if age < 60:
        print("you are an adult")
    else:
        print("you are a senior citizen")

# 5. ternary operator : short hand if statment - it is used to evaluate a condition and return a value based on the condition
# ternary operator - it is a shorthand for if else statement
age = 20
result = "eligible to vote" if age >= 18 else "not eligible to vote"
print(result)





# practice
marks = 87
if marks >= 90:
    print("you will get a phone")
else:
    print("you will notr get a phone for 1 week ")
print("thank you!") 



marks_1 = 87

if marks_1 >= 90:
    print("you can go to a trip")
elif marks_1 >= 80:
    print("you can go to a movie")
else:
    print("you will get one book")


 