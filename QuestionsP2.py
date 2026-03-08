# Question 1: Write a program to check if a no is positive

# num = 5
# if num > 0:
#     print("the no is positive", num)
# else:
#     print("the no is negative", num)


# # #2: WAP to check whether the number is odd or even

# num1 = 10
# if num1 % 2 == 0:
#     print("the no is even", num1)
# else:
#     print("the no is odd", num1)


# # #3: WAP to create a calculator 

# num2 = 10
# num3 = 5
# print("enter OPerattor")
# op = input()
# if op == '+':
#     print(num2 + num3);
# elif op == '-':
#     print(num2-num3);
# elif op == '*':
#     print(num2*num3);
# elif op =='/':
#     print(num2/num3);
# else:
#     print("invalid operartor")

# #4: WAP to check whether the passed letter is a vovel or not 
# print("enter a letter")
# letter = input()
# if letter in 'aeiouAEIOU':
#     print("the letter is a vovel", letter)
# else:
#     print("the letter is not a vovel", letter)


# #5: WAP to check if a no is a single digit no, 2-digit no and so on upto 5-digit no
# print("enter a no")
# num4 = int(input())
# if num4 < 10:
#     print("the no is a single digit no", num4)
# elif num4 < 100:
#     print("the no is a 2-digit no", num4)
# elif num4 < 1000:
#     print("the no is a 3-digit no", num4)
# elif num4 < 10000:
#     print("the no is a 4-digit no", num4)
# elif num4 < 100000:
#     print("the no is a 5-digit no", num4)
# else:
#     print("the no is more than 5-digit no", num4)




#6 area calculator for circle, rectangle and square

print("..........AREA CALCULATOR...........")

print("enter the shape")
shape = input()
if shape == 'circle':
    print("enter the radius")
    r = float(input())
    area = 3.14 * r * r
    print("the area of circle is", area)
elif shape == 'rectangle':
    print("enter the length")
    l = float(input())
    print("enter the breadth")
    b = float(input())
    area = l * b
    print("the area of rectangle is", area)
elif shape == 'square':
    print("enter the side")
    s = float(input())
    area = s * s
    print("the area of square is", area)
else:
    print("invalid shape")

