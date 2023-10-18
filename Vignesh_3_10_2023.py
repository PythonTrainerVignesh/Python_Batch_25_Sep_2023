# Source Code
# Print is a function
print(5)

# Python modules
# 1. During installation
# 2. Own repo
# 3. 3rd Party like GitHub.com

# Python Data Types or Python Literals
# 1. String (Ch)
print('Hello World')
print("Hello World")
print('Hello "" World')
print("Hello '' World")
print("Python's Class")
print("Python\nClass")
print("Python\tClass")

# Positional Arguments
print(5, 6, 8, 'Hello', 55.5, (5 + 8), True, False, (5 - 5))
# Escape Character (\)
# Research why \n and \t is not escaping
print('I\'m', 'learning', 'Python')

# Keyword Arguments
print('Hello', 'World', end='\n')
print('Hello', 'World', sep='\n')
print('Hello', 'World', sep=' $$$ ', end='')
print('Ending')

# 2. Integer
print(50)
# Integer/Float/Boolean inside '' or "", it is a string.
print("50")
print(1000 * 5)  # Whole number

# 3. Floating Point Integer
print(5.5)
print(.5)
print(9.)
print(9. * 5)
print(999999, .95 * 5)

# 4. Boolean (True/False) # Camel Case
print(True)
print(False)
print(5 < 9 > 8)
print(9 * 9.9 == 9.9 * 9)

# Python Operators (7) vs Comparison Operators (6)
print(8 + 8)  # Addition
print(8 - 8)  # Subtraction
print(8 / 8)  # Division (The answer will always be in Float)
print(8 * 8)  # Multiplication
print(8 % 3)  # Modulus - Remainder
print(8 ** 3)  # Power/Exponential
print(10 // 8)  # Floor Division

# Comparison Operators (6)
print(8 > 8)  # greater than
print(8 < 8)  # less than
print(8 <= 8)  # Less than or equal to
print(8 >= 8)  # Greater than or equal to
print(8 != 8)  # Not Equal to

print(8 == 8)  # Similar

# BOD-MAS Rule
print(2+5-5*2/8-(85/3*5))
print(85/3*5)
print(9 % 6 % 2)
print(2 * 3 % 5)
print((7 % -4), (2 % 9), (2 ** 3 ** 2))
a = list(range(-4, 9))
print(a)

print("Admin" == "admin")
print(123 == "123")
print(5 != 7)
age = 30
print(age > 30 or age == 30)
print(age >= 30)
print(True > False)

# Variables
# Variable name should never start in int
x = 5
y = 3

a, b, c = 1, 2, 6

print(x + y)
print('x' + 'y')
print('x', 'y')
print(x, y)

# Not to use the below-mentioned keywords as a variable
names = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
         'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
         'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

miles = 7.38
kilometers = 12.25
conversion_value = 1.61

miles_to_kilometers = round(miles * conversion_value, 2)
kilometers_to_miles = round(kilometers / conversion_value, 2)

print(f"{miles} miles is {miles_to_kilometers} kilometers")
print(f"{kilometers} kilometers is {kilometers_to_miles} miles")

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
