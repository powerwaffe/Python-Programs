# Ask for input
weight = int(input('What is the weight of your package?\n'))

# Process statement and print result
if weight <= 2:
    print('Your shipping charges come to $1.50')
elif 2 < weight <= 6:
    print('Your shipping charges come to $3.00')
elif 6 < weight <= 10:
    print('Your shipping charges come to $4.00')
else:
    print('Your shipping charges come to $4.75')
