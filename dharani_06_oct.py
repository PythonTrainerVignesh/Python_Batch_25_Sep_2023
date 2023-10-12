Hello_name = 'Bob'

Return = f'Hello {Hello_name}!'

print(Return, end="\n\n")

# next one

a, b = 'Yo', 'Alice'
ab = a + b
ba = b + a
print(ab + ba, end="\n\n")

# next one

tag = 'i'
name = 'Yay'
start_tag = f'<{tag}>'
end_tag = f'</{tag}>'
make_tags = f'{start_tag}{name}{end_tag}'

print(make_tags, end='\n\n')

# next one

# word = 'Yay'
# out_word = f'[[{word}]]'
# print(out_word, end='\n\n')


# next one
start_year = 2023
duration_days = 574

# let assume 365 days per year & 30 days per month
end_year = start_year + (duration_days // 365)
remaining_days = duration_days % 365
end_month = (remaining_days // 30)

print(f'Year = {end_year} & {remaining_days} days', end='\n\n')
print(f'Year & month: {end_year} & {end_month}', end='\n\n')

# next one
starting_year = 2023
starting_month = 9
duration_day = 765

# let assume 365 days per year & 30 days per month
total_months = (starting_year * 12) + starting_month + (duration_day // 30)
end_years = total_months // 12
end_months = total_months % 12
remaining_day = duration_day - (end_years - starting_year) * 365 - (end_months - starting_month) * 30

print(f'Year & month: {end_years} & {end_months}', end='\n')
print(f'Remaining days = {remaining_day} days', end='\n\n')
