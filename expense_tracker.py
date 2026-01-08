import argparse
import json
import os
from datetime import datetime

FILENAME = "expenses.json"


# Ensure data file exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w") as f:
        json.dump([], f)


def load_expenses():
    with open(FILENAME, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)


def get_next_id(expenses):
    if not expenses:
        return 1
    return max(e["id"] for e in expenses) + 1


def add_expense(description, amount):
    if amount <= 0:
        print("Error: Amount must be positive.")
        return

    expenses = load_expenses()
    expense = {
        "id": get_next_id(expenses),
        "description": description,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {expense['id']})")


def update_expense(expense_id, description, amount):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            if description:
                expense["description"] = description
            if amount is not None:
                if amount <= 0:
                    print("Error: Amount must be positive.")
                    return
                expense["amount"] = amount

            save_expenses(expenses)
            print("Expense updated successfully.")
            return

    print("Error: Expense not found.")


def delete_expense(expense_id):
    expenses = load_expenses()
    new_expenses = [e for e in expenses if e["id"] != expense_id]

    if len(new_expenses) == len(expenses):
        print("Error: Expense not found.")
        return

    save_expenses(new_expenses)
    print("Expense deleted successfully.")


def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("ID  Date        Description  Amount")
    for e in expenses:
        print(f"{e['id']:<3} {e['date']}  {e['description']:<12} ${e['amount']}")


def summary(month=None):
    expenses = load_expenses()
    total = 0

    for e in expenses:
        if month:
            expense_month = int(e["date"].split("-")[1])
            if expense_month != month:
                continue
        total += e["amount"]

    if month:
        month_name = datetime(1900, month, 1).strftime("%B")
        print(f"Total expenses for {month_name}: ${total}")
    else:
        print(f"Total expenses: ${total}")


def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True, type=float)

    # Update
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", required=True, type=int)
    update_parser.add_argument("--description")
    update_parser.add_argument("--amount", type=float)

    # Delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True, type=int)

    # List
    subparsers.add_parser("list")

    # Summary
    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)

    elif args.command == "update":
        update_expense(args.id, args.description, args.amount)

    elif args.command == "delete":
        delete_expense(args.id)

    elif args.command == "list":
        list_expenses()

    elif args.command == "summary":
        summary(args.month)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
