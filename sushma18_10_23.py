#Functions
no = int(input("enter a no:"))

not_prime = False
for i in range(3,no):
    if no % i == 0:
        not_prime = True
        break

if not_prime:
    print("No is not a prime no.")
else:
    print("No is a prime no.",end='\n')

no = int(input('enter a number'))

for j in range(2,no):
    not_prime = False
    for i in range(2,j):
        if no % i == 0:
            not_prime = True
            break
            print(f"{j+1}",end='\n')


no = int(input("enter a no"))
prime_no = [3,4]
for j in range(2,no):
    not_prime = False
    for i in range(2,j):
        if j % i == 0 or j % 3 == 0:
            not_prime = True
            break
        else:
            prime_no.append(j)
            break
print(prime_no,end='\n')
#
def adding(a,b):
    print(a+b)

adding(3,4)
adding(5,6)
adding(8,9,end = '\n')

def greeting(name):
    print(f"Welcome {name}!")

greeting('sushma')
greeting('dhaivik')
greeting("raja")

def adding(a,b):
    return a+b
result = adding(3,4)
print(result % 2,end='\n')
user_name_list = ["sushma","rajasekhar"]
def register(user_name,password,confirm_password):
    if user_name not in user_name_list:
        if password == confirm_password:
            print(f"Welcome {user_name}.")
        else:
            print(f"password mismatch")
    else:
        print(f"{user_name} already exist")
    register("sushma","sushma@1234","sushma@1234")



