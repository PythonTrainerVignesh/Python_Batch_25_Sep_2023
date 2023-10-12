age = int(input("enter your age:"))
if age >= 18:
    print('you are eligible.')
else:
    print("you are not eligible.", end = '\n\n')

answer = (input('are u a student?:'))
if answer =="yes":
    print('you are eligible.')

else:
    print("you are not eligible.")

balance = int(input("enter balance:"))
print("balance")
if balance >= 1000:
    print("order a pizza")
else:
    print("watch tv")

study = int(input("total_hours:"))
if study >= 2:
    print("pass")
else:
    print("fail")

raining = (input("is it raining?:"))
if raining == 'yes':
    print("online class.")
else:
    print("offline class")

age = int(input("enter your age?:"))
licence = input("do u have licence?:")
if age >= 18 and licence == "yes":
    print("you are eligible.")
else:
    print("you are not eligible.")

graduation = (input('do u have a graduation:'))
age = int(input('your age:'))
if graduation == "yes" and 22 <= age <= 30:
    print('you are eligible')
else:
    print('you are not eligible')

laptop = input('do u have a laptop?:')
broadband = input('do u have a broadband?:')
if laptop == 'yes' and broadband == 'yes':
    print('attend online class.')
else:
    print('attend offline class.')

carom = input('do u know to play carom?:')
chess = input('do u know to play  chess?:')
if carom == "yes" or chess == "yes":
    print('participate in the tournament!')
else:
    print('otherwise go and study.')

java = (input('do u know java?:'))
python = (input('do u know python?:'))
if java == "yes" or python == "yes":
    print('you are eligible for job.')
else:
    print('you are not eligible for job.', end='\n\n')

certification = (input("do u have a certificate?:"))
if certification == "yes":
    print('you are invited:')
else:
    print('you are not invited:')

age = int(input("enter your age?:"))
license = input("do u have a license?:")
llr = input("do u have a llr?:")
if age >= 18 and license == "yes" or llr == "yes":
    print("you are eligible.")
else:
    print("you are not eligible.")

mobile_charge = input("your mobile charge:")
if mobile_charge > "20":
    print("watch a movie.")
else:
    print("charge the mobile.")

sunny = input("is it sunny?:")
temperature = float(input("enter the temperature in celsius?:"))
if sunny == "yes" and temperature < 30:
    print('go to park:')
else:
    print('stay at home:')

raining = input("is it raining?:")
intensity = input("raining lightly or heavily?:")
if raining == "yes" and intensity == "lightly":
    print("go for shopping.")
else:
    print("sit at home.")
#
charger = input("do u have a charger(yes or no?:")
charged = int(input("how much is it charged?:"))
if charger =='yes' and charged < 20:
    print("charge it!")
else:
    print("shutdown.")