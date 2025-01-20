from datetime import datetime

class Expense:
    """Represents an individual expense."""
    
    def __init__(self, category, description, amount):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.category = category
        self.description = description
        self.amount = amount
