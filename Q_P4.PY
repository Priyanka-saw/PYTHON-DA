#1. Write a program to get fibonacci series up to 10 numbers

# fibonacci number is 0 1 1 2 3 5 8 13..
a = 0
b = 1

n = int(input("Enter a number: "))
if n == 1:
    print(1)
else:    
    print(a)
    print(b)
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


#2. Write a program to check if a number is prime or not
# divisible by 1 or itself 1, 3, 11, 13, 17, 

num = int(input("enter a number: "))

if num <= 1:
    print("not prime")
else:
    for i in range (2, num):
        if num % i == 0:
            print("number is not prime ")
            break
    else:
        print("number is prime")


#3. Write a program to find a palindrome of integers
#4. Write a program to create an area calculator.
