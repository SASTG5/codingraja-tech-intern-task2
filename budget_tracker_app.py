#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []
        self.load_data()

    def load_data(self):
        try:
            with open('budget_data.txt', 'r') as file:
                lines = file.readlines()
                for line in lines:
                    timestamp, category, amount, transaction_type = line.strip().split(',')
                    transaction = {'timestamp': timestamp, 'category': category, 'amount': float(amount),
                                   'type': transaction_type}
                    self.transactions.append(transaction)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open('budget_data.txt', 'w') as file:
            for transaction in self.transactions:
                file.write(f"{transaction['timestamp']},{transaction['category']},{transaction['amount']},{transaction['type']}\n")

    def add_transaction(self, category, amount, transaction_type, date_str):
        try:
            date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            print("Invalid date format. Please use the format DD-MM-YYYY.")
            return

        timestamp = date_obj.strftime('%Y-%m-%d %H:%M:%S')
        transaction = {'timestamp': timestamp, 'category': category, 'amount': amount, 'type': transaction_type}
        self.transactions.append(transaction)
        self.save_data()

    def calculate_balance(self):
        income = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'income')
        expenses = sum(transaction['amount'] for transaction in self.transactions if transaction['type'] == 'expense')
        balance = income - expenses
        return balance

    def display_spending_trends(self):
        categories = set(transaction['category'] for transaction in self.transactions if transaction['type'] == 'expense')
        print("Spending Trends:")
        for category in categories:
            total_spent = sum(transaction['amount'] for transaction in self.transactions
                              if transaction['category'] == category and transaction['type'] == 'expense')
            print(f"{category}: Rs.{total_spent}")

    def display_budget_summary(self):
        balance = self.calculate_balance()
        print(f"\nCurrent Balance: Rs.{balance}")
        print("Transactions:")
        for transaction in self.transactions:
            formatted_date = datetime.strptime(transaction['timestamp'], '%Y-%m-%d %H:%M:%S').strftime('%d-%m-%Y')
            print(f"{formatted_date} | {transaction['category']} | {transaction['amount']} | {transaction['type']}")
        self.display_spending_trends()

def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n--- Budget Tracker Menu ---")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Display Budget Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category = input("Enter income category: ")
            amount = float(input("Enter income amount: "))
            date_str = input("Enter income date (DD-MM-YYYY): ")
            budget_tracker.add_transaction(category, amount, 'income', date_str)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            date_str = input("Enter expense date (DD-MM-YYYY): ")
            budget_tracker.add_transaction(category, amount, 'expense', date_str)
        elif choice == '3':
            budget_tracker.display_budget_summary()
        elif choice == '4':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()


# In[ ]:




