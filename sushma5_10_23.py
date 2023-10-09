x = 0.0
print((3*(x*x*x)-2*(x*x)+(3*x)-1), end="\n\n")

x = 1
y1 = (x+(1/x))
y2 = (x+(1/y1))
y3 = (x+(1/y2))
print((1/y3), end='\n\n')

n = +123
print(n >= 100, end="\n\n")


given_hour = 23
given_minutes = 58
duration = 642

end_hour = (given_hour + (given_minutes + duration)// 60) % 24
end_minutes = (given_minutes + duration) % 60
print(f"End Time {end_hour}:{end_minutes}")


