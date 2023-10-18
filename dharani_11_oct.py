# if - elif -  else:
#  Methods class:

# n = input("Enter a number: ")
#
# if not n.isdigit():
#     print("Invalid input. Please try again.")
# elif (int(n) % 2) == 0:
#     print(f"This number {n} is an even number.")
# elif (int(n) % 2) != 0:
#     print(f"Given number {n} is odd number.")
# else:
#     pass

# next one
#
# n1 = int(input("Enter a number n1 = "))
# n2 = int(input("Enter a number n2 = "))
#
# if n1 > n2:
#     print(f"Largest number is {n1}")
# # elif n1 < n2:
# #     print(f"Largest number is {n2}")
# elif n1 == n2:
#     print("Give different numbers.")
# else:
#     print(f"Largest number is {n2}")
#
# n1 = int(input("Enter n1 = "))
# n2 = int(input("Enter n2 = "))
# n3 = int(input("Enter n3 = "))
#
# if n1 > n2 and n1 > n3:
#     print(f"The largest number is {n1}")
# elif n2 > n1 and n2 > n3:
#     print(f"The largest number is {n2}")
# elif n1 == n2 or n2 == n3 or n1 == n3:
#     print("Please try different numbers for each.")
# else:
#     print(f"The largest number is {n3}")
#
# plant_name = input("Enter the name of the plant: ")
#
# # next one
#
# if plant_name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif plant_name == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print(f"Spathiphyllum! Not {plant_name}!")

# Income calculation:
#
# income = float(input("Enter your income in thalers: "))
#
# if income <= 85528:
#     PIT = (0.18 * income - 556.02)  # let 1 thalers = 100 cents
#
#     if PIT <= 0:
#         PI = 0.0
#         print(f"The calculated personal income tax(PIT) is: {round(PI, 1)} thalers")
#     else:
#         print(f"The calculated personal income tax(PIT) is: {round(PIT, 1)} thalers")
# else:
#     overdue = income - 85528
#     tax = 14839.02 + 0.32 * overdue
#     print(f"The calculated personal income tax(PIT) is: {round(tax,1)} thalers")


# # DATE: 12/10/23:
# # Today's class is about the loops:
# # There are two loops. they are 1.While loop & 2.For loop.
# # syntax:: while True: __________ break.

# WHILE LOOP:
# x = 0
# y = 0
# while True:
#     x = x + 2
#     y = y + 1
#     if x > 20:
#         break
#     else:
#         print(f"2 * {y} ={x}")
#
# result = 0
# while True:
#     result = result + 1
#     if result > 20:
#         break
#     else:
#         print(f"2 * {result} = {result * 5}")
#
# # next
# num = 0
# while True:
#     num = num + 2
#     if num > 100:
#         break
#     else:
#         print(f"{num}", end=", ")

# next one
# while True:
#     username = input("Enter your username: ")
#     if username == 'admin':
#         password = input("Enter your password: ")
#         if password == "admin":
#             print("Login successfully.")
#             break
#         else:
#             print("Incorrect password. Please try again.")
#     else:
#         print("Incorrect username. Please try again.")
#
# # next one:
# num = 11
# while True:
#     num = num - 1
#     if num <= 0:
#         break
#     else:
#         print(f"{num}", end=", ")

# next one

# start = int(input("Enter a number to start: "))
# stop = int(input("Enter a number to stop: "))
# while True:
#     #    print(start, end=', ')
#     start = start - 1
#     if start <= stop:
#         break
#     else:
#         print(start, end=', ')

#  DATE :- 13/10/23.
# While-else loop.

# num = int(input("Enter the number: "))
#
# while num < 10:
#     num = num + 2
#     print(num)
# else:
#     print("Program Exiting....")

# count = 0
# while True:
#     count = count + 1
#     user_name = input("Enter user_name: ")
#     pass_count = 0
#     if user_name == 'admin':
#         count = 0
#         while pass_count < 3:
#             pass_count = pass_count + 1
#             password = input("Enter password: ")
#             if password == 'admin':
#                 print("Login Successful.")
#     if count > 4:
#         print("Too many attempts. Please try again sometime later.")
#         break

# next one
# count = 0
# c0 = int(input("Enter a number which is non-negative and non-zero integers: "))
# while c0 != 1:
#     count = count + 1
#     if c0 % 2 == 0:
#         c0 = c0 // 2
#         print(c0)
#     else:
#         c0 = 3 * c0 + 1
#         print(c0)
#         continue
# print(f"steps = {count}")

# n = 0
# while n < 5:
#     n = n + 1
#     print("Hello World.")

# n = 0
# while True:
#     n = n + 1
#     if n <= 3:
#         print("Hello World.")
#     else:
#         break

# next one
# num = int(input('Enter 5 numbers: '))

count = 0
average = 0
while count < 5:
    count = count + 1
    no = int(input(f'{count}. Enter no: '))
    average = average + 5
print(average // 5)
