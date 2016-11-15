# Variables to hold values
celsius = 0.0
fahrenheit = 0.0

# Ask user for input
celsius = float(input('Enter Celsius to be converted to Fahrenheit\n'))

# Convert Celsius to Fahrenheit
fahrenheit = (9/5) * celsius + 32

# Output result
print(celsius, 'degrees Celsius converted to Fahrenheit is', format(fahrenheit, '.1f'),
      'degrees Fahrenheit')
