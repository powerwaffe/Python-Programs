# Ask user for a month, day, and a two digit year in numeric form
month = int(input('Enter a month in numeric form:\n'))
day = int(input('Enter a day in numeric form:\n'))
year = int(input('Enter two digit year (i.e. 20XX):\n'))

# Calculate month times day
checkYear = month * day

# IF checkYear equals year, print that the date is magic, otherwise print that it is not
if year == checkYear:
    print('The date is magic!')
else:
    print('Not so magical year')