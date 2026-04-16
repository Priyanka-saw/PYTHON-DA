# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1, 6):    #rows
#     for j in range(1, i+1):   #columns
#         print(j, end=" ")
#     print()


# *
# **
# ***
# ****
# *****


# for i in range(1, 6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


# 1
# 22
# 333
# 4444
# 55555

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(i, end=" ")
#     print()


# 11111
# 2222
# 333
# 44
# 5

# for i in range(1, 6):
#     for j in range(6, i, -1):
#         print("*", end=" ")
#     print()


# *
# **
# ***
# ****
# ***
# **
# *

for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
for i in range(5, 0, -1):
    for k in range(0, i-1):
        print("*", end=" ")
    print()


