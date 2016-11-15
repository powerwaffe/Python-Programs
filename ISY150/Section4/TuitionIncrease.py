# print tuition and declare its increase
print("Tuition will increase by 3% per year for the next 5 years.")

# print starting tuition amount
print("Current tuition for full-time students will start at $8,000.")

# initialize tuition and tuition increase variable
tuition = 8000
tuitionIncrease = 0.03

#  print headings using tabs
print("\nYear\t\tProjected Tuition (per semester)")
print("--------------------------------------------")

# 5 year tuition loop
for year in range(1, 6):
    increasedTuition = tuition + (tuition * tuitionIncrease)
    tuition += tuition * tuitionIncrease

    # print tuition increase
    print(year, "\t\t\t", format(increasedTuition, ".2f"))
