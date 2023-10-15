count = 0
while True:
    number = int(input("enter a number?:"))
    if number != 0:
        number = number + 1
        if number % 2 == 0:
            numbers = number // 2
            print("login successful")
        else:
            number = 3 * number + 1
            print(number)
            continue
        print("try again")

n = 0
while n < 5:
    n = n + 1
    print("hello world!.")

n = 0
while n < 5:
    n = n + 1
    print("hello world!.")
     







