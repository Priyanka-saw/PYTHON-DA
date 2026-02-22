#1. wap display person name age and address in different lines

name = "Priyanka"
age = 20
address = "jsr"

# print("name:", name)

# print("age : ", age)

# print("address : ", address)

#print("using one statement")
#print("name :", name, "\nage : ", age, "\naddress : ", address)


#2.swap two variables

num1 = 12
num2 = 23
# print("before swapping : ", num1, num2)

#using third variable
temp = num1
num1 = num2
num2 = temp
# print("after swapping : ", num1, num2)


#without using third variable
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
# print("after swapping : ", num1, num2)


#using right left and left right algoqrithm
num1, num2 = num2, num1
# print("after swapping : ", num1, num2)


#zor operstor
num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2
# print("after swaping : ", num1, num2)


# wap float into integer
num = 3.14
# print("float value : ", num)   

num = int(num)
# print("integer value : ", num)


# take id details from students 
name = input("enter your name : ")
age = int(input("enter your age : "))
grade = input("enter your grade : ")
address = input("enter your address : ")

# print("Students details : ")
# print("Name : ", name)
# print("Age :" , age)
# print("Grade : ", grade)
# print("Address : ", address)


#take an user input as integer then convert to float
num = int(input("enter a number : "))
print("integer value : ", num)

num = float(num)
print(type(num))
print("float value : ", num)


