# Ask for input
milesDriven = int(input('How many miles driven?'))  # ask for miles and store value
gallonsUsed = int(input('How many gallons of fuel were used?'))  # ask for gallons used and store value

# Formula for MPG
milesPerGal = milesDriven / gallonsUsed

# Print result
print('You used', format(milesPerGal, '.2f'), 'miles per gallon')
