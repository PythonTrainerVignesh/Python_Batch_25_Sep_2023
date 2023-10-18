# #while loop & for loop
# secret_no = 0
# while True:
#     secret_no == secret_no + 10
#     if secret_no > 100:
#         break
#     else:
#         print(secret_no)
#
#
# number = 2
# while True:
#     number == number + 1
#     if number > 12:
#         break
#     else:
#         print(f"2 x {number} = {number * 2}")
#
# number = 0
# while True:
#     number = number + 2
#     if number > 100:
#         break
#     else:
#         print(f"{number}", end = ', ')
# #
# while True:
#     username = input('enter username:')
#     if username == 'admin':
#         password = input('enter password:')
#         if password == 'admin':
#              print('login successful')
#              break
#         else:
#              print("incorrect password")
#     else:
#         print("try again")

#
# while True:
#    start = int(input("enter number to start:"))
#    stop = int(input("enter number to stop:"))
#    start = start - 1
#    if start <= stop:
#        break
#    else:
#        print("start again:", end = '\n\n')
#
#
# number = 11
# while True:
#       number = number - 1
#       if number <= 0:
#           break
#       else:
#            print("number:")
#
# start = 10
# stop = 0
# while start > stop:
#     start = start - 1
#     print(start)
# else:
#     print("exciting program..")
#
# start = 0
# stop = 10
# while start < stop:
#     start = start + 2
#     print(start)
# else:
#     print("exciting program..")
#
# count = 0
# while True:
#     count = count + 1
#     user_name = input("enter user_name?:")
#     pass_count = 0
#     if user_name == 'admin':
#         count = 0
#         while pass_count > 3:
#             pass_count = pass_count + 3
#             password = input("enter password:")
#             if password == 'admin':
#                 print("login successful:")
#     if count > 4:
#         print("to many wrong questions,try again after 5 minutes.")
#         break

count = 0
while True:
    count = count + 1
    licence = input("do u have a licence?:")
    if licence == 'yes':
        break
        print("you are eligible to drive")
        count = 0
    while licence != 'yes':
        count >3;
        llr = input("do u have a llr")
        if llr == 'yes':
         print ("you are eligible to drive")
         break
        if count > 4:
            print("to many wrong questions.try again.")

