# Dummy variable for loop
celsius = 0

# Template
print("Celsius\t\tFahrenheit")
print("----------------------")

# For loop to print Celsius to Fahrenheit table
for celsius in range(0, 21, celsius + 1):
    fahrenheit = (9/5) * celsius + 32
    print(celsius, "\t\t\t", format(fahrenheit, '.1f'))
