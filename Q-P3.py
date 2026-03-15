#1. WAP to find a sum of all the even number upto 50

# sum = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         print(i)
#         sum += i
# print("the sum of the even no upto 50 is", sum)


#2. WAP to first 20 number and their square

# print("Square of the number is : ")
# for i in range(1, 21):
#     print(i, i**2)


#3. WAP to find sum of the first 10 odd number using while number 

# sum = 0
# i = 1
# while i <= 20:
#     if i % 2 != 0:
#         print(i)
#         sum += i
#     i += 1
# print("the sum of the first 10 odd number is", sum)

#3.WAP  to check if a no is divisible by 8 and 12 upto 100 no

# for i in range(1, 101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i, "is divisible by 8 and 12")


#4. WAP to create a biling system at supermarket

print("Ente tthe price of the item")
price = float(input())
print("Enter the quantity of the item")
quantity = int(input())
total = price * quantity
print("the total bill is", total)

