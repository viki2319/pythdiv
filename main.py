from menu import MenuHandler

expense_csv = "expenses.csv"

if __name__ == "__main__":
    menu = MenuHandler(expense_csv)
    menu.display_menu()
