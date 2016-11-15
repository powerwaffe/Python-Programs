# define main function
def main():
    feet = float(input("Enter feet to be converted to inches:"))
    feet_to_inches(feet)
    print(feet, 'feet is equal to', feet_to_inches(feet), 'inches')


# define conversion function
def feet_to_inches(feet):
    return feet * 12


# call main
main()
