def main():
    keep_asking = 'y'

    while keep_asking == 'y':

        # ask for date input
        user_input = input('Enter date in the form of mm/dd/yyyy')

        # split string
        date = user_input.split('/')

        # print formatted date with name
        if date[0] == '01':
            print('January', date[1], ',', date[2])
        elif date[0] == '02':
            print('February', date[1], ',', date[2])
        elif date[0] == '03':
            print('March', date[1], ',', date[2])
        elif date[0] == '04':
            print('April', date[1], ',', date[2])
        elif date[0] == '05':
            print('May', date[1], ',', date[2])
        elif date[0] == '06':
            print('June', date[1], ',', date[2])
        elif date[0] == '07':
            print('July', date[1], ',', date[2])
        elif date[0] == '08':
            print('August', date[1], ',', date[2])
        elif date[0] == '09':
            print('September', date[1], ',', date[2])
        elif date[0] == '10':
            print('October', date[1], ',', date[2])
        elif date[0] == '11':
            print('November', date[1], ',', date[2])
        elif date[0] == '12':
            print('December', date[1], ',', date[2])
        else:
            print('INCORRECT FORMAT!!')

        keep_asking = input('Would you like to enter another date? y or n').lower()

main()