# tracker.py
from expense import Expense
from storage import load_expenses, save_expenses
from report import show_expenses, show_summary

def main_menu():
    expenses = load_expenses()

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category (Food, Travel, Shopping, etc.): ")
                note = input("Enter note: ")
                expenses.append(Expense(amount, category, note))
                save_expenses(expenses)
                print("✅ Expense added successfully!")
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == "2":
            show_expenses(expenses)

        elif choice == "3":
            show_summary(expenses)

        elif choice == "4":
            print("👋 Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please try again.")
