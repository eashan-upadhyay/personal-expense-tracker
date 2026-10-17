# Personal Expense Tracker

A command-line expense tracking application built with Python. It allows users to manage daily expenses, organize spending by category, and store records locally using JSON.

## Features

- **Add Expenses:** Record an expense with its name, amount, and category.
- **View Expenses:** Display all recorded expenses.
- **Category Totals:** Calculate the total amount spent in each category.
- **Edit Expenses:** Update the name, amount, and category of an existing expense.
- **Delete Expenses:** Remove an expense from the records.
- **Data Persistence:** Save expenses to a JSON file and load them when the application starts.
- **Input Validation:** Handle invalid amounts, empty names and categories, and invalid menu selections.

## Technologies Used

- Python
- JSON
- Python standard library (`json` module)

## Requirements

- Python 3 installed on your computer.

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the application:

   ```bash
   python expense_tracker.py
   ```

4. Follow the on-screen menu to manage your expenses.

## Data Storage

Expense records are stored locally in `expenses.json`. The file is loaded when the application starts, and changes are saved so they remain available across sessions.

## What I Learned

- Working with Python lists and dictionaries.
- Using functions to organize a program.
- Validating user input and handling exceptions.
- Reading and writing JSON data.
- Implementing create, view, update, and delete operations.
- Testing application behavior with valid and invalid inputs.

## Future Improvements

- Add monthly spending summaries.
- Export expense reports.
- Add automated tests.
- Build a graphical user interface.

---

**Author:** Eashan Upadhyay