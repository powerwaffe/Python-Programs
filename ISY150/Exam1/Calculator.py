# simple calculator program that uses a menu to calculate user input
# variable for loop
userSelection = 0

# start loop with initial value of 0
while userSelection != 5:
    print('Calculator Program\nPLease Choose an Option:\n\n')
    userSelection = int(input('1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit'))

    # calculate selection
    if userSelection == 1:
        add1 = int(input('Enter first number'))
        add2 = int(input('Enter second number'))
        print(add1, " + ", add2, ' = ', add1 + add2)
    elif userSelection == 2:
        sub1 = int(input('Enter first number'))
        sub2 = int(input('Enter first number'))
        print(sub1, ' - ', sub2, ' = ', sub1 - sub2)
    elif userSelection == 3:
        multi1 = int(input('Enter first number'))
        multi2 = int(input('Enter first number'))
        print(multi1, ' * ', multi2, ' = ', multi1 * multi2)
    elif userSelection == 4:
        divide1 = int(input('Enter first number'))
        divide2 = int(input('Enter first number'))
        print(divide1, ' / ', divide2, ' = ', divide1 / divide2)
    elif userSelection == 5:
        print('Thank you for using my program, goodbye!')
    else:
        print('INVALID INPUT! TRY AGAIN.')
