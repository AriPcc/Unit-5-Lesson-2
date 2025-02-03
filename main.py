# *****************************************************************************
def main():
    # Declare variables
    budget = 0.0
    total = 0.0
    entry = 1.0

    # Print welcome message
    print("This program will calculate whether your monthly expenses are over "
    "or under budget.\n")

    # Get budget
    budget = float(input("Enter your budget for the month: "))

    # Get expenses until they enter 0
    while entry != 0:
        if total == 0:
            entry = float(input("Begin entering expenses (0 when finished): "))
        else:
            entry = float(input("Next expense (0 when finished): "))
        total += entry
        print("Current total: $", str(format(total, ".2f")), "\n", sep = "")
    
    # Display results
    print("\nWith a budget of $", str(format(budget, ".2f")), ", your expenses"
    " added up to $",
     str(format(total, ".2f")), sep = "")
    print("You're ", sep = "", end = "")
    if budget - total > 0:
        print("$", str(format(budget - total, ".2f")), " under budget.\n", sep 
        = "")
    elif budget - total < 0:
        print("$", str(format(abs(budget - total), ".2f")), " over budget.\n", 
        sep = "")
    else:
        print("exactly within budget.\n")
    
    # Print goodbye message
    print("See you next month!")
main()