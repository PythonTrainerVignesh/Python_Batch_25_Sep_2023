miles = float(input("Enter miles:"))
kilometer = float(input("Enter kilometer:"))
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometer / 7.38
print(round(kilometers_to_miles))
print(f"{miles} miles is {round(miles_to_kilometers, 2)} kilometers")
print(f"{kilometer} kilometers is {round(kilometer,2)} miles", end='\n\n')

x = float(input("Enter number:"))
print(x)
print((3*(x*x*x)-2*(x*x)+(3*x)-1))
#
x = float(input("Enter number:"))
y1 = (x+(1/x))
y2 = (x+(1/y1))
y3 = (x+(1/y2))
print(1/y3)

given_hour =float(input("Enter hour:"))
given_minutes =float(input("Enter minutes:"))
duration = float(input("Enter duration:"))
end_hour = (given_hour + (given_minutes + duration) // 60) % 24
end_minutes = (given_minutes + duration) % 60
print(f"end_time:-{end_hour}:{end_minutes}", end = '\n\n')

n = float(input("Enter number:"))
print(n >= 100)

celsius = float(input("enter value:"))
fahrenheit = float(input("enter value:"))
celsius_to_fahrenheit = (celsius * 9/5) + 32
fahrenheit_to_celsius = (fahrenheit - 32)*5/9
print(f"{celsius} celsius is {round(celsius_to_fahrenheit,2)} fahrenheit")
print(f"{fahrenheit} fahrenheit is {round(fahrenheit_to_celsius,2)} celsius", end='\n\n')

x = float(input("enter number:"))
y = float(input("enter value:"))
print(f"{x}:{y}+{round(x+y)}")

name = str(input("enter your name:"))
salary = int(input("salary package:"))
print(f"{name},'your package is around:{salary}.", end = '\n\n')

name = str(input("enter your name:"))
print("hello," + name)




