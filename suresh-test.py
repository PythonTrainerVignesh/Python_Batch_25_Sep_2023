#1
graduation=input("Are you graduated :")
age=int(input("What is your age :"))
if graduation== "yes" and 22<= age <=30:
    print("your eligible")
else:
    print("your not eligible")

#2
laptop=input("Do you have laptop :")
broadband=input("D0 you have broadband :")
if laptop=="yes" and broadband=="yes":
    print("Attend the online class")
else:
    print("Attend the offline class")

#3
water=input("If you have water :")
if water=="yes":
    print("Drink it")
else:
    print("Go to shop and get it :)")

#4
rain=input("Is it raining there :")
climete=input("How does it rain there lightly or heavily :")
if rain=="yes" and climete=="lightly":
    print("Then go for shoping :")
else:
    print("Then sit at home ")

#5
sunny=input("Is it sunny today :")
temperature=int(input("What's today temperature :"))
if sunny=="no" and temperature <= 30:
    print("Then go to park")
else:
    print("Stay at home")

#6
carrom=input("Do know how to play carrom ? :")
chess=input("Do know how to play chess ? :")
if carrom=="yes" or chess=="yes":
    print("You can participete the tournament")
else:
    print("sorry you can't participate in tournament, Pleas go and study")

#7
java=input("Do you know java :")
python=input("Do you know python :")
if java== "yes" or python== "yes":
    print("You are eligible to apply for the job")
else:
    print("You are not eligible to apply for the job")
#8
certificate=input("Do you have certificate :")
if certificate=="yes":
    print("welcome")
else:
    print("error")

#9
age=int(input("What is your age :"))
license=input("Do you have license :")
LLR=input("Do you have LLR :")
if 17<= age >=18 and license=="yes" or LLR=="yes" :
    print("You are eligible")
else:
    print("You not are eligible")
#10
mobile=int(input("What is your mobile charge percentage :"))
if mobile>20:
    print("Watch a movie")
else:
    print("Charge the mobile")