def main():
    # Declare variables
    counter = 0
    numbers = 0

    # Open numbers.txt file for reading
    try:
        numbers_file = open('numbers.txt', 'r')

        # read file keep track of counter, accumulate total (use for loop)
        for line in numbers_file:
            numbers += int(line)
            counter += 1

        # Close file
        numbers_file.close()

        # Calculate average
        average = numbers / counter

        # Display the average of the numbers in the file
        print('Average of numbers in file is ', format(average, '.1f'))
    except IOError:
        print('ERROR: Could not open file, check filename.')
    except ValueError:
        print('ERROR: Non-numeric data read from file.')

# Call the main function.main()
main()