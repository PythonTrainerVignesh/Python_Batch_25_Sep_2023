# source code
# print is a function
# IDE Integrated development environment
# python with integrated folder in pycharm
# PEP python enhancement proposal
# PEP is using for style code
# python modules
# 1.during installation
# 2.own repo
# 3.3rd party like GitHub.com

# positional argument using (,) in between character
print('hello', 'simon')
# escape character(\)


# keyword argument
print("hello", "world", sep=" ")
print("hello", "world", end=" ")
print("hello", "world", sep=" ", end=" ")
print("ending")
# python data types or python literals
# 1.sting ()ch
# 1.1 print('')
# 1.2 print("""")

# 2. integer
# print (45)

print(100 * 4)  # whole number
print(10 + 10)
print("python\tclass")
# 3. floating point integer
print(10.23)

# 4. boolean is a camel case
# print(True)
# print(False)
# print(4>5)

# python operators(7) or comparison operator(6)


# print(8+8)addition
# print(8-8)subtraction
# print(8*8)multiplication
# print(8%8)modules
# print(8/8)division(the answer will always be in float)
# print(8**8)power/exponetial
# print(8//8) floor division

# comparison operator
# print(<) lesser than
# print(>)greater than
# print(<=)lesser than or equal to
# print(>=)greater than or equal to
# print(!=)not equal to
# print(==)similer

# bodmas rule
print(2 + 3 - 2 * 4 / 4 - (33 / 5 * 4))
print(9 % 7 % 2)
print(2 * 4 % 5)



Jhon = 3
Mary = 5
adam = 6
total_apples = Jhon+Mary+adam
print("Total number of apples:",total_apples)

miles = 50
kilometers = 20
miles_to_kilometer = miles * 1.61
kilometer_to_miles = kilometers / 1.61

print (50,"miles is", miles_to_kilometer ,"kilometers")



miles = 6.45
kilometers = 10.67
done = 1.61
miles_to_kilometer = miles * done
kilometer_to_miles = kilometers / done
print(6.45,"miles is",round(miles_to_kilometer ,3),"kilometers")




x =((3*(-1.)**3 )- (2*(-1.)**2) + (3*(-1.)- 1))
print("y =",x)

x = (1/(10+1/(10+1/(10+1/10))))
print("y =",x)


n=55
print(n>=100)
n = 101
print(n>=100)

y = ((3*(1.)**3)-(2*(1.)**2)+(3*(1.)-1))
print("y =",y)
x=10
x =6
print("y =",x)

n=10
print(n<=100)




cel = 48.9
fah = 110.5
celsius =(48.9*9/5)+32
print(celsius )
fahrenheit = (110-32)*5/9
print (round(fahrenheit,2))

x = 1.
n = ((3*(x)**3)-(2*(x)**2)+(3*(x))-1)
print("y =",n)

#x = input("x value is:")
a = ((3*(float(x))**3)-(2*(float(x))**2)+(3*(float(x)))-1)
print(a)


hour = int(input("start time: "))
min = int(input("start min:"))
dur = int(input("event duration:"))
endhour = (hour*60+min+dur)//60%24
endmin = ((min + dur)%60)
print("event end time is ",endhour,":",endmin)


age= int(input("enter your age :"))
if age <=18:
    print(f"{age}your not eligible to vote" )
else:
    print(f"{age}your eligible to vote")



age = input('Enter your age: ')

if age.isdigit():
    if int(age) >= 18:
        License = input('Do you have a license (yes/no): ')
        if License == 'yes':
            print('You are eligible to drive.')
        elif License == 'no':
            LLR = input('Do you have LLR (yes/no): ')
            if LLR == 'yes':
                print('You are eligible to drive with a pillion rider.')
            elif LLR == 'no':
                print('You are not eligible to drive. Go & apply for a LLR first.')
            else:
                print('Invalid input.')
        else:
            print('Invalid input.')
    else:
        print('You are not eligible.')
else:
    print('Invalid input.')


# Find average of 5 nos
count = 0
average = 0
while count < 5:
    count = count + 1
    no = int(input(f'{count}: Enter no: '))
    average = average + no
print(average // 5)

count = 0
while True:
    count = count + 1
    name = input('Enter username: ')
    if name == 'admin':
        count = 0
        passwd_count = 0
        while passwd_count < 3:
            passwd_count = passwd_count + 1
            passwd = input('Enter password: ')
            if passwd == 'admin':
                print('login successful.')
                break
            else:
                print('Incorrect password.')
    if count == 3:
        print('Too many attempts. Try again after sometime.')
        break


word = "I'm learning python"  #iterable

for no in range(1, 13):
    print(f"2 x {no} = {2*no}")

word = "United States of America"  # iterable

count_s = 0
count_i = 0
for i in word:
    if i.lower() == 's':
        count_s = count_s + 1
    elif i.lower() == 'i':
        count_i = count_i + 1
    else:
        continue
print(f"The no of s in {word} is {count_s}.", f"The no of i in {word} is {count_i}.", sep='\n')


no_tuple = (1, 2, 3, 4, 5, 6)  # Immutable
no_list = [1, 2, 3, 4, 5, 6, 'dgddf', [0, 5, 8, 90], {"": ""}]  # Mutable
no_dict = {"fruit1": "Apple",
           "fruit2": "Mango",
           "fruit3": "Banana",
           "email": "vignesh@fita.in",
           "phone_no": "8056195179",
           }  # Key-Value pairs

print(no_tuple[5])
# no_tuple[5] = 10

print(no_list)
no_list.reverse()
print(no_list)

no_dict['name'] = 'vignesh'
print(no_dict)
# print(no_dict)
print()

uname_list = []


def register(uname, passwd, confirm_passwd):
    if uname.capitalize() not in uname_list:
        if passwd == confirm_passwd:
            print(f"Welcome {uname}.")
            uname_list.append(uname.capitalize())
        else:
            print(f"Password mismatch.")
    else:
        print(f"{uname} already exist.")


register("Ganesh", "pass123", "pass123")
register("Python", "pass123", "pass123")
register("Guest", "pass123", "pass123")
print(uname_list)
