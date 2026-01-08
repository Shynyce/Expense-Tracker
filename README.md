# Expense Tracker CLI

A simple command-line expense tracker that helps you manage and summarize your expenses.  
You can add, update, delete, and view expenses, as well as generate total and monthly summaries.

Built using **Python** and the **standard library only**.

---

## Features

- Add new expenses with a description and amount
- Update existing expenses
- Delete expenses
- View all expenses
- View total expense summary
- View expense summary for a specific month (current year)
- Persistent storage using a local JSON file

---

## Requirements

- Python 3.7 or higher
- No external dependencies

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/expense-tracker-cli.git
   cd expense-tracker-cli
````

2. Verify Python installation:

   ```bash
   python3 --version
   ```

---

## Usage

Run the application from the command line:

```bash
python expense_tracker.py <command> [options]
```

---

## Commands

### Add an Expense

```bash
python expense_tracker.py add --description "Lunch" --amount 20
```

### Update an Expense

```bash
python expense_tracker.py update --id 1 --description "Lunch with friends" --amount 25
```

### Delete an Expense

```bash
python expense_tracker.py delete --id 2
```

### List All Expenses

```bash
python expense_tracker.py list
```

### View Total Expense Summary

```bash
python expense_tracker.py summary
```

### View Monthly Expense Summary

```bash
python expense_tracker.py summary --month 8
```

---

## Expense Data Structure

Each expense contains the following fields:

* `id` – Unique identifier
* `description` – Expense description
* `amount` – Expense amount
* `date` – Date added (`YYYY-MM-DD`)

Example:

```json
{
  "id": 1,
  "description": "Lunch",
  "amount": 20,
  "date": "2024-08-06"
}
```

---

## Data Storage

Expenses are stored in a local file named `expenses.json`.
The file is automatically created if it does not exist.

---

## Error Handling

* Prevents negative or zero amounts
* Handles invalid commands and arguments
* Gracefully reports non-existent expense IDs

---

## Project Structure

```
expense-tracker-cli/
│
├── expense_tracker.py
├── expenses.json
└── README.md
```

---

## License

This project is open-source and intended for learning and personal use.

```

If you want, I can also:
- Rename commands to a global `expense-tracker` executable
- Add screenshots / demo output
- Tailor this exactly for **roadmap.sh submission**
```
