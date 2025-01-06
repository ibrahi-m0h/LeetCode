# You have a monthly budget, and you're tracking your expenses. Write a program that:

# Displays your current budget.
# Allows you to calculate the remaining budget after making a specific purchase.
# Outputs the updated remaining budget after deducting the expense.
# For example, if your starting budget is $3500.75 and you spend $9 on a shirt, the program should display the new remaining budget after the expense. Use functions to organize your code for displaying the budget and calculating the updated amount.

# Target Output:
# Your remaining budget is: $3500.75
# Your remaining budget is: $3491.75

# Define global variables
current_budget = 3500.75
shirt_expense = 9

def print_current_budget():
    print(f"The current budget is ${current_budget}")

# Create function to calculate the updated budget remaining after expense:

def deduct_budget(budget, expense):
    return budget - expense


remaining_budget = deduct_budget(current_budget, shirt_expense)


print_current_budget()
print(f"The remaining budget after shirt purchase is ${remaining_budget}")

