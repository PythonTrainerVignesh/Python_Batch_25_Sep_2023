John = 3
Mary = 5
Adam = 6
total_apples = John + Mary + Adam

print("Total number of apples:", total_apples)
print(f"Total number of apples: {total_apples}", end="\n\n")

# Round function
Kilometers = 12.25
Miles = 7.38

miles_to_kilometer = Miles * 1.61
kilometer_to_miles = Kilometers / 1.61

print(f"{Miles} miles is {round(miles_to_kilometer,2)} kilometers")
print(f"{Kilometers} kilometer is {round(kilometer_to_miles,2)} miles", end="\n\n")


x = 0

y = (3.0 * x**3) - (2.0 * x**2) + (3.0 * x) - 1.0

print(f"y = {y}", end="\n\n")


# next one

x = 10
y = 1/(x + (1 / (x + (1 / (x + (1 / x))))))

print(f"y = {y}", end="\n\n")

# next one

Start_hour, start_minutes = 12, 17
Duration = 59

end_hour = (Start_hour + (start_minutes + Duration) // 60) % 24
end_minute = (start_minutes + Duration) % 60

print(f"End Time:- {end_hour}:{end_minute}", end="\n\n")

# next one

n = 101
result = n >= 100
print(result)

