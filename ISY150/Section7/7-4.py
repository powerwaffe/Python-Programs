def main():
    # list to be calculated
    print('Enter 20 numbers. Press ENTER after each number')
    number_list = get_numbers()

    # total of list
    total = sum(number_list)

    # get length of list
    length = len(number_list)

    print('Enter 20 numbers and press ENTER after each')

    # print lowest number in list
    print('Lowest number in list: ', min(number_list))

    # print highest number in list
    print('Highest number in list: ', max(number_list))

    # print sum of numbers in list
    print('Sum of numbers in list: ', total)

    # print average of numbers in list
    print('Average of numbers in list: ', total / length)


# get numbers function
def get_numbers():
    # initialize list
    my_list = []

    # loop counter
    counter = 0

    # get numbers from user
    while counter != 20:
        numbers = int(input('Enter a number: '))
        my_list.append(numbers)
        counter += 1

    # return list to main
    return my_list

main()
