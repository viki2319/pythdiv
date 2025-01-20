from tracker import ExpenseTracker

class MenuHandler:
    """Handles user interaction."""
    
    def __init__(self, file_name):
        self.tracker = ExpenseTracker(file_name)

    def display_menu(self):
        """Displays the menu and handles user input."""
        while True:
            print("\n=== Personal Expense Tracker ===")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. View Summary")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == "1":
                self.tracker.add_expense()
            elif choice == "2":
                self.tracker.view_expenses()
            elif choice == "3":
                self.tracker.view_summary()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
