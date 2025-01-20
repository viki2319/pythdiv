import csv
from os import path

class ExpenseFileManager:
    """Handles file operations for expenses."""
    
    @staticmethod
    def init_file(file_name):
        """Initializes the CSV file with headers if it doesn't exist."""
        if not path.exists(file_name):
            try:
                with open(file_name, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Date", "Category", "Description", "Amount"])
                    print("New expense file created.")
            except Exception as e:
                print(f"Error creating file: {e}")

    @staticmethod
    def write_expense(file_name, expense):
        """Writes a new expense to the CSV file."""
        try:
            with open(file_name, mode='a', newline="") as file:
                writer = csv.writer(file)
                writer.writerow([expense.date, expense.category, expense.description, expense.amount])
                print("Expense successfully saved!")
        except Exception as e:
            print(f"Error saving expense: {e}")

    @staticmethod
    def read_expenses(file_name):
        """Reads all expenses from the CSV file."""
        try:
            with open(file_name, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                return list(reader)
        except Exception as e:
            print(f"Error reading expenses: {e}")
            return []
