import math


class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def get_balance(self):
        balance = 0
        for item in self.ledger:
                balance += item["amount"]
        return balance

    def get_total_spending(self):
        total_spending = 0
        for item in self.ledger:
            if item["amount"] < 0:
                total_spending -= item["amount"]
        return total_spending

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for item in self.ledger:
            items += f"{item['description'][:23]:<23}" + f"{item['amount']:>7.2f}\n"
            total += item['amount']
        output = title + items + "Total: " + str(total)
        return output
                
def create_spend_chart(categories):
    total_spending = sum(category.get_total_spending() for category in categories)
    percentages = [int(category.get_total_spending() / total_spending * 100) for category in categories]
    percentages = [math.floor(p / 10) * 10 for p in percentages]
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"
    return chart