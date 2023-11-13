import json

# Initialize an empty expense tracker
expense_tracker = []

def add_expense(date, description, category, amount):
    expense = {
        "date": date,
        "description": description,
        "category": category,
        "amount": amount,
    }
    expense_tracker.append(expense)
    print("Expense added successfully!")

def categorize_expense(expense_id, new_category):
    if expense_id >= 0 and expense_id > len(expense_tracker):
        expense_tracker[expense_id]["category"] = new_category
        print("Categorized Succefully! ")
    else:
        print("Invalid")

def view_summary():
    summary = {}
    for expense in expense_tracker:
     category = expense["category"]
     amount = expense["amount"]
     summary[category] = summary.get(category,0) + amount
     print("Summary of spending by category:")
    for category, amount in summary.items():
        print(f"{category}: ${amount:.2f}")
    
# Function to save expense data to a JSON file
def save_data(filename):
    with open(filename, "w") as file:
        json.dump(expense_tracker, file)
    print("Expense data saved to file.")

# Function to load expense data from a JSON file
def load_data(filename):
    global expense_tracker
    try:
        with open(filename, "r") as file:
            expense_tracker = json.load(file)
        print("Expense data loaded from file.")
    except FileNotFoundError:
        print("File not found. No data loaded.")

# Main loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. Categorize Expense")
    print("3. View Summary")
    print("4. Save Data")
    print("5. Load Data")
    print("6. Quit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(date, description, category, amount)
    elif choice == "2":
        expense_id = int(input("Enter expense ID to categorize: "))
        new_category = input("Enter new category: ")
        categorize_expense(expense_id, new_category)
    elif choice == "3":
        view_summary()
    elif choice == "4":
        filename = input("Enter filename to save data: ")
        save_data(filename)
    elif choice == "5":
        filename = input("Enter filename to load data: ")
        load_data(filename)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
     

   