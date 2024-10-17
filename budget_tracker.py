# budget_tracker.py

class BudgetTracker:
    def __init__(self):
        self.budget = 0
        self.expenses = []

    def set_budget(self, amount):
        self.budget = amount
        print(f"Budget set to: ${self.budget}")

    def add_expense(self, description, amount):
        if amount > self.budget:
            print("Expense exceeds the budget!")
        else:
            self.expenses.append({'description': description, 'amount': amount})
            self.budget -= amount
            print(f"Added expense: {description}, Amount: ${amount}")

    def view_budget(self):
        print(f"Remaining budget: ${self.budget}")

    def view_expenses(self):
        print("Expenses:")
        for expense in self.expenses:
            print(f"- {expense['description']}: ${expense['amount']}")


if __name__ == "__main__":
    tracker = BudgetTracker()
    tracker.set_budget(1000)  # Set initial budget
    tracker.add_expense("Groceries", 200)
    tracker.view_budget()
    tracker.view_expenses()
