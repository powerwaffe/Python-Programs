# define main
def main():
    try:
        # open file
        infile = open('charge_accounts.txt', 'r')

        # load contents of file into list
        charge_accounts = infile.readlines()

        # close file
        infile.close()

        # strip '\n'
        index = 0
        while index < len(charge_accounts):
            charge_accounts[index] = charge_accounts[index].rstrip('\n')
            index += 1

        # variable for while loop
        keep_going = 'y'

        while keep_going == 'y':
            # ask user to enter a charge account number
            check_charge = input('Enter charge account number to be checked: ')

            # determine if charge account number matches text file
            if check_charge in charge_accounts:
                print('Valid charge account number!')
            else:
                    print('INVALID charge account number!')

            # ask if user wants to make another selection
            keep_going = input('Would you like to check for another charge account (y or n)')
            if keep_going == 'n':
                print('Thanks for using my program. Goodbye.')
    except IOError:
        print('File not found, check if file exists.')
main()
