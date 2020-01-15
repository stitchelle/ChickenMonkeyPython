# Write a program that prints the numbers from 1 to 100. You can use Python's range() to quickly make a list of numbers.

#    -For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
#    - For the multiples of seven (7, 14, 21, etc.) print "Monkey".
#    - For numbers which are multiples of both five and seven print "ChickenMonkey".

# 1ST TRY

# for chickenmonkey in range(1,101):
#     # if chickenmonkey % 5 == 0 and chickenmonkey % 7 == 0:
#     #     print("chickenmonkey")
#     if chickenmonkey % 5 == 0:
#         print("chicken")
#     elif chickenmonkey % 7 == 0:
#         print("monkey")
#     print(chickenmonkey)

# 2ND TRY

for n in range(1, 101):
    s = ""
    if n % 5 == 0:
        s += "Chicken"
    if n % 7 == 0:
        s += "Monkey"
    print (s or n)




