import csv
import os

# File to store expenses
EXPENSES_FILE = "expenses.csv"

# Function to add an expense
def add_expense(description, amount, date):
    with open(EXPENSES_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([description, amount, date])
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses():
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded yet.")
        return
    
    with open(EXPENSES_FILE, "r") as file:
        reader = csv.reader(file)
        print("\n--- Expense List ---")
        total = 0
        for row in reader:
            if row:
                print(f"Description: {row[0]}, Amount: ₹{row[1]}, Date: {row[2]}")
                total += float(row[1])
        print(f"\nTotal Expenses: ₹{total}")

# Function to show menu
def menu():
    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            desc = input("Enter description: ")
            amt = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(desc, amt, date)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
menu()
