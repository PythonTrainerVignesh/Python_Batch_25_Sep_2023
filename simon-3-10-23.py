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
