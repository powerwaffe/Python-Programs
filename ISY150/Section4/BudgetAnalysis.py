# Ask for input
budget = float(input("Enter amount budgeted for the month: "))
total = 0.0
spent = float(input("Enter an amount spent(0 to quit)"))
# Loop
while spent != 0:
    # Calculate and ask for input
    total += spent
    spent = float(input("Enter an amount spent(0 to quit)"))

    # Conditional statement to check if over, under, or budget met
    if total == budget and spent == 0:
        print("Budgeted : $", format(budget, ".2f"))
        print("Amount spent: $", format(total, ".2f"))
        print("Spending matches budget, well done.")
    elif total < budget and spent == 0:
        print("Budgeted : $", format(budget, ".2f"))
        print("Amount spent: $", format(total, ".2f"))
        print("Spending is $", format(budget - total, ".2f"), "under budget, nice.")
    elif total > budget and spent == 0:
        print("Budgeted : $", format(budget, ".2f"))
        print("Amount spent: $", format(total, ".2f"))
        print("Spending is $", format(total - budget, ".2f"), "over budget, not good.")
