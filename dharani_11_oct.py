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
# if plant_name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif plant_name == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print(f"Spathiphyllum! Not {plant_name}!")

income = float(input("Enter your income in thalers: "))

if income <= 85528:
    PIT = max((0.18 * income - 556.02), 0.0)  # let 1 thalers = 100 cents
    print(f"The calculated personal income tax(PIT) is: {round(PIT,1)} thalers")
else:
    overdue = income - 85528
    tax = max((14839.02 + 0.32 * overdue), 0.0)
    print(f"The calculated personal income tax(PIT) is: {round(tax,1)} thalers")
