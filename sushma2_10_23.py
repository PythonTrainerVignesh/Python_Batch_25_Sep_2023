john = 4
mary = 5
adam = 6
total_apples = john+mary+adam
print("total number of apples", total_apples)
print(f"total number of apples", {total_apples})

miles = 7.38
kilometer = 12.25
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometer / 7.38
print(round(kilometers_to_miles))
print(f"{miles} miles is {round(miles_to_kilometers, 2)} kilometers")
print(f"{kilometer} kilometers is {round(kilometer,2)} miles")

x = -1.0
print((3*(x*x*x)-2*(x*x)+(3*x)-1))

x = -5
y1 = (x+(1/x))
y2 = (x+(1/y1))
y3 = (x+(1/y2))
print(1/y3)

given_hour = 12
given_minutes = 17
duration = 59
end_hour = (given_hour + (given_minutes + duration) // 60) % 24
end_minutes = (given_minutes + duration) % 60
print(f"end_time:-{end_hour}:{end_minutes}", end = '\n\n')

n = + 123
print(n >= 100)
#1mile = 1.61km











