# report.py
def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n=== All Expenses ===")
    for i, exp in enumerate(expenses, 1):
        print(f"{i}. {exp.category} - ${exp.amount} ({exp.note})")
    print()

def show_summary(expenses):
    total = sum(exp.amount for exp in expenses)
    print(f"\n💰 Total Expenses: ${total}")

    categories = {}
    for exp in expenses:
        categories[exp.category] = categories.get(exp.category, 0) + exp.amount

    print("📊 Expenses by Category:")
    for cat, amt in categories.items():
        print(f"  {cat}: ${amt}")
    print()
