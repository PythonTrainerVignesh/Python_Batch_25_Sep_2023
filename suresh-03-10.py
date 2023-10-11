# Source Code
# Print is a function
print(5)

# Python modules
# 1. During installation
# 2. Own repository
# 3. 3rd Party like GitHub.com

# Python Data Types or Python Literals
# 1. String (when a word and number inside the  "" and '' it consider as a string)
print('Hello World')
print("Hello World")
# print("3 5 5") <-- it also consider as string


# Positional Arguments

# "string" pakkathula comma ( , ) iruntha consider as a "positional argument"
# print("ronaldo","is","GOAT",0,7)

# Escape Character (\) "slash pakkathila word or number it won't escape"
# (\n) it takes to next line
# (\t) 3 space vidum (don't    expect   anything)

print('I\'m', 'learning', 'Python')

# Keyword Arguments
# sep=""  (sep will work only in comma (,) place )
# end=""  (
print('Hello', 'World', end='\n')
print('Hello', 'World', sep='\n')
print('Hello', 'World', sep=' $$$ ', end='')
print('Ending')

# 2. Integer means "number"
# int
# int la words multiplication pannalam, but words multiplication thavira vera maths panna mudiyathu
print(50 + 5)
print("ronaldo" * 5)

# 3. Floating Point Integer
print(5.5)
print(.5)
print(9.)
print(9. * 5)

# 4. Boolean (True/False) # Camel Case
print(True)
print(False)

# Python Operators (7) vs Comparison Operators (6)
print(8 + 8)    # Addition
print(8 - 8)    # Subtraction
print(8 / 8)    # Division (The answer will always be in Float)
print(8 * 8)    # Multiplication
print(8 % 3)    # Modulus - Remainder
print(8 ** 3)   # Power/Exponential
print(10 // 8)  # Floor Division

# Comparison Operators (6)
print(8 > 8)  # greater than
print(8 < 8)  # less than
print(8 <= 8)  # Less than or equial to
print(8 >= 8)  # Greater than or equal to
print(8 != 8)  # Not Equal to
print(8 == 8)  # Similar

# BOD-MAS Rule
print(2+5-5*2/8-(85/3*5))
print(85/3*5)
print(9 % 6 % 2) #right to left
print(2 * 3 % 5) #left to right
print((7 % -4), (2 % 9), (2 ** 3 ** 2))
a = list(range(-4, 9))

john = 3
mary = 5
adam = 6
total_apples= john+mary+adam
print("total numbers of apple:",total_apples)

miles = 7.38
kilometers = 12.25
conversion_value = 1.61

miles_to_kilometers = round(miles * conversion_value, 2)
kilometers_to_miles = round(kilometers / conversion_value, 2)

print(f"{miles} miles is {miles_to_kilometers} kilometers")
print(f"{kilometers} kilometers is {kilometers_to_miles} miles")

x=(3*(0.)**3)-(2*(0.)**2)+(3*(0.)-1)
print("y=",x)

x=1/(100+1/(100+1/(100+1/100)))
print("y=",x)

n=55
print(55>=100)
print(99>=100)
print(160>=100)
print(3>2)

x=-1
y=(3*(x)**3)-(2*(x)**2)+(3*(x)-1)
print("y =",y)

x=1
y=1/(x+1/(x+1/(x+1/x)))
print("y =",y)

h=12
m=17
r=59
a=m+r
b=76
print(76%60)


dc=49.7
print(round(dc*(9/5)+32,2))


start_hour=23
start_minutes=58
duration=642
minutresult=(start_minutes+duration)%60
hoursresult=((((start_hour*60)+start_minutes+duration)//60)%24)
print(f"the event will end on {hoursresult}:{minutresult}")

start_hour=int(input("event start hour : "))
start_minutes=int(input("event start minute : "))
duration=int(input("given duration : "))
minutresult=((start_minutes+duration)%60)
hoursresult=(((start_hour+duration)//60+start_hour)%24)
print(f"the event will end on {hoursresult}:{minutresult}")
