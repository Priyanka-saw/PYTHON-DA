# Operators are special symbols or keywords used to perform operations on variables and values.
# types of operators are 
# 1. arithmetics 
# 2.comparison (relational)
# 3. logical
# 4.assignment
# Identity 
# Membership - Check if a value exists in a sequence 
# types - in, not in
# 5.bitwise  - AND, OR, XOR, RIGHT SHIFT, LEFT SHIFT 


# example
a = 5   # 101 in binary
b = 3   # 011 in binary
print(a & b)  # 1


# Identity

# Identity operators check whether two variables refer to the same object in memory (not just equal values).

# Operators:
# types

# is → True if both variables point to the same object

# is not → True if both variables point to different objects

# Example 1: Same Object
a = [1, 2, 3]
b = a

print(a is b)      # True
print(a is not b)  # False

#  b refers to the same list object as a, so a is b is True.

# Example 2: Different Objects (Same Value)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
print(a == b)  # True

x = 10
y = 10

print(x is y)  #True