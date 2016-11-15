# Ask user for length and width of rectangle one
rectangleOneLength = int(input('Enter length of first rectangle'))
rectangleOneWidth = int(input('Enter width of the first rectangle'))

# Ask user for length and width of rectangle two
rectangleTwoLength = int(input('Enter length of second rectangle'))
rectangleTwoWidth = int(input('Enter width of second rectangle'))

# Calculate area of rectangles
areaOfRectangleOne = rectangleOneLength * rectangleOneWidth
areaOfRectangleTwo = rectangleTwoLength * rectangleTwoWidth
print('\nArea of rectangle one =', areaOfRectangleOne, '\nArea of rectangle two =', areaOfRectangleTwo)

# Compare and find which rectangle has the greater area (>) or if they are similar (==)
if areaOfRectangleOne > areaOfRectangleTwo:
    print('**Rectangle one is larger than rectangle two**')
elif areaOfRectangleOne < areaOfRectangleTwo:
    print('**Rectangle two is larger than rectangle one**')
else:
    print('**Rectangle one and rectangle two are of similar areas**')

