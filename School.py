age = input('Enter your age: ')

if age.isdigit():
    if int(age) >= 18:
        License = input('Do you have a license (yes/no): ')
        if License == 'yes':
            print('You are eligible to drive.')
        elif License == 'no':
            LLR = input('Do you have LLR (yes/no): ')
            if LLR == 'yes':
                print('You are eligible to drive with a pillion rider.')
            elif LLR == 'no':
                print('You are not eligible to drive. Go & apply for a LLR first.')
            else:
                print('Invalid input.')
        else:
            print('Invalid input.')
    else:
        print('You are not eligible.')
else:
    print('Invalid input.')
