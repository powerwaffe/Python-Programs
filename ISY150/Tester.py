# This is a comment
print("Fuck all ya'll")
age = 25
print("my age is", age, ', and I like poopin')
name = input('What is my name?\n')
print("Hello", name)
hours = int(input('How many hours \
did you work?\n'))  # \ is used to space sentences
print('Ok ', name, ', you worked ', hours, ' hours.', sep='')   # sep='' can be used to remove spaces or add chars
newHours = hours * hours / 3
print(format(newHours, '.1f')) # rounds float to the first decimal place
