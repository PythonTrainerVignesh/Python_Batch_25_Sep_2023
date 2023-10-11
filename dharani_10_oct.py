# # Today class is about conditional statements or arguments:
#
# age = int(input("Enter your age for verification: "))
#
# if age >= 18:
#     print(f"Your are eligible for voting.")
# else:
#     print(f"Your are not eligible for voting.")
#
# # Next one
#
# number1, number2 = int(input('Enter an number1')), int(input('Enter an number2'))
#
# if number1 > number2:
#
# # Next one:
#
# student = input('Are you a student (Yes/No): ')
# if student == 'Yes':
#     print(f'You are eligible for 50% discount.')
# elif student == 'No':
#     print("You are not eligible.")
# else:
#     print("Enter only Yes/No option.")
#
# # Another one
#
# balance = int(input("How much balance available? : Rs."))
# if balance > 1000:
#     print("you can order a pizza for yourself.")
# else:
#     print("You can only watch the TV.")
#
# # Next one
#
# Hours = int(input("How many hours are you studying for exam? : "))
#
# if Hours >= 2:
#     print("You are able pass the exam.")
# else:
#     print("you can't pass the exam.")
#
# # Next one
#
# rain = input("Is it raining or not outside? (only give yes/no) : ")
# if rain == 'yes':
#     print("Then there is only Online class for today.")
# elif rain == 'no':
#     print("So today is Offline class.")
# else:
#     print("Give proper answer.")
#
# # next one
#
# age = int(input("what is your age? : "))
# License = input("Do you have license? : ")
#
# if age >= 18 and License == "yes":
#     print("Then you can drive a vehicle.")
# else:
#     print("Then you can't drive any vehicle.")
#
# # Next one
#
# age = int(input('Enter your age: '))
# Graduation = input("Whether you're having any graduation certificate: ")
#
# if 22 <= age <= 30 and Graduation == "yes":
#     print("Then you are eligible.")
# else:
#     print("You are not eligible.")

# Next one

# laptop = input("Do you have a Laptop? (yes/no): ")
# broadband = input("Do you have a Broadband connection? (yes/no): ")
#
# if laptop == 'yes' and broadband == 'yes':
#     print("You can attend the online class.")
# else:
#     print("Attend offline class only.")

# water = input("Do you having water? (yes/no): ")
# if water == 'yes':
#     print("Drink water.")
# else:
#     print("Go and get some water from the shop.")

# raining = input("Is it raining? (yes/no): ")
#
# if raining == 'yes':
#     print("Watch TV at home.")
# else:
#     print('Go out and play.')

# is_raining = input('Is it raining? (yes/no): ')
# intensity = input("Raining lightly or heavily? (lightly/heavily): ")
#
# if is_raining == 'yes' and intensity == 'lightly':
#     print('Go for shopping.')
# else:
#     print('Sit at home.')

# sunny = input('Is it sunny? (yes/no): ')
# temp = float(input("Enter the temperature in celsius: "))
#
# if sunny == 'yes' and temp < 30:
#     print('Go to park.')
# else:
#     print("stay at home.")

# carrom = input("DO you know how to play Carrom? (yes/no): ")
# chess = input("Do you know how to play chess? (yes/no): ")
#
# if carrom == 'yes' or chess == 'yes':
#     print("Participate in the tournament.")
# else:
#     print("Go and study.")

# java = input("Do you know Java? (yes/no): ")
# python = input('Do you know Python? (yes/no): ')
#
# if java == "yes" or python == 'yes':
#     print("You are eligible to apply for the job.")
# else:
#     print("Not eligible. Please work on your tech skills.")

# certification = input('Do you have a certification? (yes/no): ')
#
# if certification == 'yes':
#     print("you are invited.")
# else:
#     print("You are not invited.")

# age = int(input("Enter your age: "))
# License = input("Do you have a driving license or LLR? (yes/no): ")
#
# if age >= 18 and License == 'yes':
#     print("You are eligible to drive.")
# else:
#     print("you are not eligible.")

charge = float(input("Enter your mobile charge percentage: "))

if charge > 20:
    print("You can watch a movie on your mobile.")
else:
    print("Charge your mobile first.")
