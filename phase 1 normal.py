class Expense:
    def __init__(self, description, amount, paid_by):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by

class User:
    def __init__(self, name):
        self.name = name
        self.expenses = []

users = []

def add_user():
    name = input("Enter user name: ")
    user = User(name)
    users.append(user)

def add_expense():
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    
    print("Select the user who paid:")
    for i, user in enumerate(users):
        print(f"{i+1}. {user.name}")
    
    choice = int(input("Enter choice: "))
    paid_by = users[choice-1]
    
    expense = Expense(description, amount, paid_by)
    
    for user in users:
        if user == paid_by:
            user.expenses.append(expense)
        else:
            share_amount = amount / (len(users) - 1)
            debt_expense = Expense(description, share_amount, paid_by)
            user.expenses.append(debt_expense)

def calculate_owe():
    total_expenses = {}
    
    for user in users:
        total_expense = sum(expense.amount for expense in user.expenses)
        total_expenses[user] = total_expense
    
    average_expense_per_user = sum(total_expenses.values()) / len(users)
    
    print("Expense summary:")
    
    for user in users:
        if total_expenses[user] > average_expense_per_user:
            print(f"{user.name} owes {total_expenses[user] - average_expense_per_user:.2f}")
        elif total_expenses[user] < average_expense_per_user:
            print(f"{user.name} is owed {average_expense_per_user - total_expenses[user]:.2f}")
        else:
            print(f"{user.name} has no debts")

while True:
    print("\nExpense Sharing App")
    print("-------------------")
    print("1. Add User")
    print("2. Add Expense")
    print("3. Calculate Debts")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_user()
    elif choice == 2:
        add_expense()
    elif choice == 3:
        calculate_owe()
    elif choice == 4:
        break