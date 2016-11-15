# define main function
def main():
    selection = 0
    while selection != 5:
        # call menu function
        menu()

        # input for menu AND loop
        selection = int(input())

        if selection == 1:
            # grab two values and store them separately
            num1, num2 = get_numbers()
            # add then display
            display_results(add(num1, num2))
        elif selection == 2:
            # grab two values and store them separately
            num1, num2 = get_numbers()
            # subtract then display
            display_results(subtract(num1, num2))
        elif selection == 3:
            # grab two values and store them separately
            num1, num2 = get_numbers()
            # multiply then display
            display_results(multiply(num1, num2))
        elif selection == 4:
            # grab two values and store them separately
            num1, num2 = get_numbers()
            # divide then display
            display_results(divide(num1, num2))
        elif selection == 5:
            print('Thanks for using my program! Goodbye.')
            break
        else:
            print('WARNING!! INVALID INPUT.\n')


# print a menu
def menu():
    print('Calculator Program\nPLease Choose an Option:\n\n')
    print('1)Addition\n2)Subtraction\n3)Multiplication\n4)Division\n5)Exit')


# get numbers from user
def get_numbers():
    num1 = int(input('Enter first number'))
    num2 = int(input('Enter second number'))
    return num1, num2


# return addition of two integers
def add(num1, num2):
    return num1 + num2


# return subtraction of two integers
def subtract(num1, num2):
    return num1 - num2


# return multiplication of two integers
def multiply(num1, num2):
    return num1 * num2


# return division of two integers
def divide(num1, num2):
    return num1 / num2


# print answer in argument
def display_results(answer):
    print(answer)


# call main function
main()
