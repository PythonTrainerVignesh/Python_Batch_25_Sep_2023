# number = (input("choose a number:"))
# if not number.isdigit():
#     print("invalid number.")
# elif int(number) % 2 == 0:
#     print("number is even:")
# elif int(number)% 2 != 0:
#     print("number is odd")
# else:
#     print("invalid number.")
#
age = input('enter your age: ')

if age.isdigit():
    if int(age) >= 18:
        licence = input('Do u have a licence (yes/no): ')
        if licence == 'yes':
            print("you are eligible.")
        elif licence == 'no':
            llr = input("Do u have a llr(yes/no)?:")
            if llr == 'yes':
                print("you are eligible to drive with pillion rider.")
            elif llr == 'no':
                  print("you are not eligible to drive. Go and apply for a llr first.")
            else:
                print("Invalid input.")
        else:
             print("Invalid input")
    else:
          print("you are not eligible.")
else:
    print("Invalid input.")



number1 = int(input("enter a number n1=():"))
number2 = int(input("enter a nuber n2=():"))
number3 = int(input("enter a number n3=():"))
if number1 > number2 and number1 > number3:
    print(f"larger number is {number1}")
elif number2 > number1 and number2 > number3:
    print(f"largest number is {number2}")
elif number1 == number2 or number2 == number3 or number1 == number3:
    print("try different number.")
else:
    print(f"the largest number is {number3}", end = '\n\n')

name = input("enter a plant name?:")
if name == 'Spathiphyllum':
    print("yes - Spathiphyllum is the best plant ever:")
elif name == 'spathiphyllum':
    print("No,I want a big spathiphyllum:")
else:
    print("spathiphyllum! Not[name]!")

income = float(input("enter you income:"))
if income <= 85528:
    tax = income * (18/100)- 556.02
else:
      income-85528
