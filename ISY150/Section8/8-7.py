def main():
    try:
        # open file
        infile = open('text.txt', 'r')

        # read file
        file = infile.read()

        # counters for file
        count_upper = 0
        count_lower = 0
        count_digits = 0
        count_whitespace = 0

        # iterate through each character in file
        for ch in file:
            if ch.isupper():
                count_upper += 1
            elif ch.islower():
                count_lower += 1
            elif ch.isdigit():
                count_digits += 1
            elif ch.isspace():
                count_whitespace += 1

        # print results
        print('Number of uppercase characters =', count_upper)
        print('Number of lowercase characters =', count_lower)
        print('Number of digits =', count_digits)
        print('Number of whitespace characters =', count_whitespace)

        # close file
        infile.close()

    except IOError:
        print('File not found')

main()
