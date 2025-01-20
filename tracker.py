from collections import defaultdict
from expense import Expense
from file_manager import ExpenseFileManager

class ExpenseTracker:
    """Manages expense operations."""
    
    def __init__(self, file_name):
        self.file_name = file_name
        ExpenseFileManager.init_file(file_name)
    
    def add_expense(self):
        """Adds a new expense."""
        print("\nAdding new expense:")
        
        # Predefined categories
        categories = ['Food', 'Transport', 'Entertainment', 'Bills', 'Shopping', 'Other']
        print("Available Categories:")
        for idx, category in enumerate(categories, start=1):
            print(f"{idx}. {category}")
        
        try:
            category_choice = int(input("Enter category number (1-6): "))
            category = categories[category_choice - 1] if 1 <= category_choice <= len(categories) else 'Other'
        except ValueError:
            print("Invalid input. Using 'Other'.")
            category = 'Other'
        
        description = input("Enter description: ")
        while True:
            try:
                amount = float(input("Enter amount: "))
                if amount > 0:
                    break
                print("Amount must be positive.")
            except ValueError:
                print("Invalid input. Enter a number.")
        
        expense = Expense(category, description, amount)
        ExpenseFileManager.write_expense(self.file_name, expense)

    def view_expenses(self):
        """Displays all expenses."""
        print("\nViewing all expenses:")
        expenses = ExpenseFileManager.read_expenses(self.file_name)
        if not expenses:
            print("No expenses recorded.")
            return
        
        total_expense = 0
        for row in expenses:
            print(f"Date: {row[0]}, Category: {row[1]}, Description: {row[2]}, Amount: {row[3]}")
            total_expense += float(row[3])
        print(f"\nTotal Expense: ${total_expense:.2f}")

    def view_summary(self):
        """Displays summary of expenses by category."""
        print("\nExpense Summary by Category:")
        expenses = ExpenseFileManager.read_expenses(self.file_name)
        if not expenses:
            print("No expenses recorded.")
            return
        
        summary = defaultdict(float)
        for row in expenses:
            summary[row[1]] += float(row[3])
        
        for category, total in sorted(summary.items(), key=lambda x: x[1], reverse=True):
            print(f"Category: {category}, Total Expense: ${total:.2f}")
