x= 10
n=(1/(x+1/(x+1/(x+1/x))))
print("y =",n)



x = 1.
n = ((3*(x)**3)-(2*(x)**2)+(3*(x))-1)
print("y =",n)

n = 110
x = (100 <= n >=200)
print(x)



hour = 23
min = 58
dur = 642
end_hour = ((hour*60)+58+642)//60%24
end_min = (min+dur)%60
print("event end time is ",end_hour,":",end_min)


hour = int(input("start hour :"))
min = int(input("start min:"))
dur = int(input("event duration:"))
end_hour = ((hour*60)+min+dur)//60%24
end_min = (min+dur)%60
print("event end time is ",end_hour,":",end_min)