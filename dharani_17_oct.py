# n = 11
# while n > 1:
#     n = n - 1
#     print(n)
#
# count = 0
# while True:
#     count = count + 1
#     username = input("Enter your username: ")
# Next one:

# Today is for loop:

# word = "I'm learning python"    # iterable
#
# for i in word:
#     print(i)
#
# next one: here range(0, 100 ,5):
# count = 1
# for i in range(2, 21, 2):
#     count = count +1
#     print(f"2 * {count} = {i}")
#
# for i in range(1, 21):
#     print(f"2 X {i} = {i * 2}")
#
# # next one
#
# word = "I'm learning python"
# count = 0
# for i in word:
#     if i == 'n':
#         count = count + 1
# print(count)
#
# for j in word:
#     print(j, end='')
#     if j == 'g':
#         break

# next

# word = "United States of America"              # "Mississippi"
#
# count = 0
# Count = 0
# for i in word:
#     if i == "i":
#         count = count + 1
#     elif i == "s":
#         Count = Count + 1
#     else:
#         continue
# print(f"The no. of i's in {word} is {count}.")
# print(f"The no. of s's in {word} is {Count}.")

# next one

# word = "Hi-There"
#
# for i in word:
#     print(i + i, end='')
#     # print(i * 2, end='')

# cs = 0
# fruits = ['apple', 'banana', 'cherry']
# for k in fruits:
#     cs = cs + 1
#     print(f"{cs}. {k}")
#
# num = [1, 2, 3, 4, 5, 6]
# total = 0
# for no in num:
#     total = total + no
# print("Sum:", total)
#
# names = ["Alice", "Bob", "Charles"]
# for j in names:
#     print(f"Hello, {j}!")
#
# Friuts = ['apple', 'banana', 'cherry']
# vowel_count = 0
# for word in Friuts:
#     for l in word:
#         if l in "aeiou":
#             vowel_count = vowel_count + 1
# print(f"Total vowels in {Friuts}: {vowel_count}")
#
# # next one:
#
# no_tuple = (1, 2, 3, 4, 5, 6)  # Immutable :- not changeable
# no_list = [1, 2, 3, 4, 5, 6]  # Mutable
# no_dict = {"fruit1": "Apple",
#            "fruit2": "Mango",
#            "fruit": "Banana",
#            "email": "dharani@ita.in"}  # Key-Value pair

# ______________________________________DATE: 18/10/23:-

# number = int(input("Enter a number: "))
# non_prime = False
#
# for i in range(2, number):
#     if number % i == 0:
#         non_prime = True
#         break
# if non_prime:
#     print(f"{number} is not a prime number.")
# else:
#     print(f"{number} is a prime number.")
# _______________ FInd the no of prime numbers in given numbers?
#
# numb = int(input("Enter a non negative and non zero integer: "))
#
# prime_numbers = []
#
# for num in range(2, numb + 1):
#     is_prime = True
#     for i in range(2, num):  # range(2, int(num ** 0.5) + 1)
#         if (num % i) == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime_numbers.append(num)
#
# print(f"Prime numbers below {numb} are: {prime_numbers}")

# ________________-__FUNCTIONS:-

# uname_list = []
#
#
# def register(uname, passwd, confirm_passwd):
#     if uname.capitalize() not in uname_list:
#         if passwd == confirm_passwd:
#             print(f"Welcome {uname}.")
#             uname_list.append(uname.capitalize())
#         else:
#             print("Password mismatch. Please try again")
#     else:
#         print(f"This {uname} already exist try another username.")
#
#
# register("Dharani", "pass@123", "pass@123")
# register("Python", "pass123", "pass123")
# register("Guest", "pass123", "pass123")
# register("Ganesh", "pass@123", "pass@123")
# register("Dharani", "pass@123", "pass123")
# print(uname_list)

# ______For the strings places to get slicing [start:end:step]__________________________________
# positions can be reversing using "-ve int".
