miles = float(input())
kilometer = input()
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometer / 7.38
print(round(kilometers_to_miles))
print(f"{miles} miles is {round(miles_to_kilometers, 2)} kilometers")
print(f"{kilometer} kilometers is {round(kilometer,2)} miles", end='\n\n')

x = input()
print((3*(x*x*x)-2*(x*x)+(3*x)-1))

x = input()
y1 = (x+(1/x))
y2 = (x+(1/y1))
y3 = (x+(1/y2))
print(1/y3,end='\n\n')

given_hour = input()
given_minutes = input()
duration = input()
end_hour = (given_hour + (given_minutes + duration) // 60) % 24
end_minutes = (given_minutes + duration) % 60
print(f"end_time:-{end_hour}:{end_minutes}", end = '\n\n')

n = input()
print(n >= 100)





