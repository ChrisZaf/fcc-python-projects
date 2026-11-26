My Budget App project from freeCodeCamp.

- Category class: Tracks deposits, withdrawals, and transfers between different budget categories using a ledger.
- Receipt output: Printing a `Category` object formats the ledger into a 30-character wide receipt showing each transaction and the remaining balance.
- create_spend_chart function: Takes a list of categories and builds a bar chart comparing the percentage spent in each category (rounded down to the nearest 10)
  (was unnecessarily painful to do) 

If you wanna try it out: 

from budget_app import Category, create_spend_chart

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")

clothing = Category("Clothing")
food.transfer(50, clothing)

print(food)
print(create_spend_chart([food, clothing]))
