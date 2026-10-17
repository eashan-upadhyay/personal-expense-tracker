import json

try:
    with open("expenses.json", "r") as file:
        expense_records = json.load(file)
except FileNotFoundError:
    expense_records = []

print("Welcome to Eashan's Expense Tracker")
print("-----------------------------------")
print("Hello, Eashan!")


def add_expense():
    while True:
        expense = input("What did you spend money on? ").strip()

        if expense.strip() != "":
            break

        print("Expense name cannot be empty. Try again.")

    while True:
        try:
            amount = float(input("How much did you spend? "))

            if amount <= 0:
                print("Amount must be greater than zero. Try again.")
                continue

            break

        except ValueError:
            print("Please enter a valid number. Try again.")

    while True:
        category = input("What category is this expense? ").strip()

        if category.strip() != "":
            break

        print("Category cannot be empty. Try again.")

    expense_record = {
        "expense": expense,
        "amount": amount,
        "category": category
    }

    expense_records.append(expense_record)

    print("Expense added successfully!")

def view_expenses():
    print("\n========== EXPENSE SUMMARY ==========")

    if not expense_records:
        print("There are no expenses to display.")
    else:
        for record in expense_records:
            print(f'{record["expense"]}: ₹{record["amount"]:.2f} ({record["category"]})')

    print("=====================================")

def show_category_totals():
    category_totals = {}

    for record in expense_records:
        category = record["category"]
        amount = record["amount"]

        if category in category_totals:
            category_totals[category] = category_totals[category] + amount
        else:
            category_totals[category] = amount

    print("\n====== CATEGORY TOTALS ======")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")

    print("=============================")

def delete_expense():
    if not expense_records:
        print("There are no expenses to delete.")
        return

    print("\n========== DELETE EXPENSE ==========")

    for i, record in enumerate(expense_records, start=1):
        print(f'{i}. {record["expense"]}: ₹{record["amount"]:.2f} ({record["category"]})')

    choice = input("Enter the number of the expense to delete: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if choice < 1 or choice > len(expense_records):
        print("Invalid expense number.")
        return 

    index = choice - 1

    deleted_expense = expense_records.pop(index)
    print(f'{deleted_expense["expense"]} deleted successfully!')    
    
    with open("expenses.json", "w") as file:
        json.dump(expense_records, file, indent=4)

def edit_expense():
    if not expense_records:
        print("There are no expenses to edit.")
        return
        
    print("\n========== EDIT EXPENSE ==========")

    for i, record in enumerate(expense_records, start=1):
        print(f'{i}. {record["expense"]}: ₹{record["amount"]:.2f} ({record["category"]})')    

    choice = input("Enter the number of the expense to edit: ")

    try:
        choice = int(choice)
    except ValueError:
        print("Please enter a valid whole number.")
        return
    
    if choice < 1 or choice > len(expense_records):
        print("Invalid expense number.")
        return

    index = choice - 1
    record = expense_records[index]

    while True:
        new_name = input("Enter the new expense name: ").strip()

        if new_name.strip() != "":
            break
        else:
            print("Expense name cannot be empty. Try again.")

    while True:
        try:
            new_amount = float(input("Enter the new expense amount: "))

            if new_amount <= 0:
                print("Amount must be greater than zero. Try again.")
                continue

            break

        except ValueError:
            print("Please enter a valid number. Try again.")

    while True:
        new_category = input("Enter the new expense category: ").strip()

        if new_category.strip() != "":
            break
        else:
            print("Category cannot be empty. Try again.")

    record["expense"] = new_name
    record["amount"] = new_amount
    record["category"] = new_category

    print("Expense updated successfully!")

    with open("expenses.json", "w") as file:
        json.dump(expense_records, file, indent=4)

while True:
    print("\n========== EXPENSE TRACKER ==========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Category Totals")
    print("4. Delete Expense")
    print("5. Edit Expense")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        show_category_totals()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        edit_expense()
    
    elif choice == "6":
        with open("expenses.json", "w") as file:
            json.dump(expense_records, file, indent=4)

        print("Thank you for using Eashan's Expense Tracker!")
        break
    else:
        print("Invalid menu choice. Please select an option from 1 to 6.")