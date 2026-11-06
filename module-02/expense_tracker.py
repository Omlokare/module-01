"""A beginner command-line expense tracker. Run with: python expense_tracker.py"""

import csv
from pathlib import Path

DATA_FILE = Path("expenses.csv")
FIELDS = ["description", "category", "amount"]


def load_expenses():
    """Load saved expense rows from the CSV file."""
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def save_expenses(expenses):
    """Write all expense rows to the CSV file."""
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    """Ask for expense details and append a valid row."""
    description = input("What was the expense? ").strip()
    category = input("Category (for example, food or travel): ").strip()
    if not description or not category:
        print("Description and category cannot be empty.")
        return

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Please enter a valid number for the amount.")
        return
    if amount < 0:
        print("Amount cannot be negative.")
        return

    expenses.append({
        "description": description,
        "category": category,
        "amount": f"{amount:.2f}",
    })
    save_expenses(expenses)
    print("Expense saved.")


def show_expenses(expenses):
    """Print the saved expenses and their total."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nYour expenses:")
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['description']} ({expense['category']}) "
            f"- ${float(expense['amount']):.2f}"
        )
    total = sum(float(expense["amount"]) for expense in expenses)
    print(f"Total: ${total:.2f}")


def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker")
        print("1. Add an expense")
        print("2. View expenses and total")
        print("3. Exit")
        choice = input("Choose 1, 2, or 3: ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
