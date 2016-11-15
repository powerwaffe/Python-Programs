def main():
    outfile = open('numbers.txt', 'w')

    num1 = int(input('Enter number'))
    num2 = int(input('Enter number'))
    num3 = int(input('Enter number'))

    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    outfile.close()

main()