celsiues = 49.7   # to farhnheit

farnheit = 110.5   # to celcies

Fahrenheit = (celsiues * 9 / 5) + 32

Celsius = (farnheit - 32) * 5 / 9

print(f'Fahrenheit: {round(Fahrenheit, 2)} F')
print(f'Celsius: {round(Celsius, 2)} C', end='\n\n')

# Next one
# "Input" functions:
# Data type conversion;
# input() always takes as strings
# then conversion of data type takes place in next steps where we required.

Kilometers = input('Enter the kilometers: ')     # 12.25
Miles = input('Enter in miles: ')           # 7.38

miles_to_kilometer = float(Miles) * 1.61
kilometer_to_miles = float(Kilometers) / 1.61

print(f"{Miles} miles is {round(miles_to_kilometer,2)} kilometers")
print(f"{Kilometers} kilometer is {round(kilometer_to_miles,2)} miles", end="\n\n")

# Next one
x = input('Enter the value of x: ')   # 0

y = (3.0 * float(x)**3) - (2.0 * float(x)**2) + (3.0 * float(x)) - 1.0

print(f"y = {y}", end="\n\n")

# next one

x = input('Enter value of x: ')      # 10

y = 1/(float(x) + (1 / (float(x) + (1 / (float(x) + (1 / float(x)))))))

print(f"y = {y}", end="\n\n")

# next one

n = input('Enter n value: ')    # 250
result = 100 <= float(n) <= 200
print(result, end='\n\n')

# next one

Start_hour, start_minutes = int(input('Hour: ')), int(input('Minutes: '))           # 12, 17
Duration = int(input('Duration: '))      # 59

end_hour = (Start_hour + (start_minutes + Duration) // 60) % 24
end_minute = (start_minutes + Duration) % 60

print(f"End Time:- {end_hour}:{end_minute}", end="\n\n")

# next one
start_year = int(input('Enter starting year: '))             # 2023
duration_days = int(input('Enter duration days: '))                    # 574

# let assume 365 days per year & 30 days per month
end_year = start_year + (duration_days // 365)
remaining_days = duration_days % 365
end_month = (remaining_days // 30)

print(f'Year = {end_year} & {remaining_days} days', end='\n\n')
print(f'Year & month: {end_year} & {end_month}', end='\n\n')

# Next one

number = int(input('Enter a number: '))

Even_number = (number % 2 == 0)

print(f"The given number {number} is even: {Even_number}")
