class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amt}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Calculate spending (withdrawals only) per category
    spendings = []
    for category in categories:
        spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spendings.append(spent)
    
    total_spent = sum(spendings)
    
    # Calculate percentages rounded down to the nearest 10
    percentages = []
    for s in spendings:
        if total_spent > 0:
            pct = int((s / total_spent) * 100)
            percentages.append((pct // 10) * 10)
        else:
            percentages.append(0)

    # Build chart lines from 100 down to 0
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += str(i).rjust(3) + "| "
        for pct in percentages:
            if pct >= i:
                res += "o  "
            else:
                res += "   "
        res += "\n"

    # Add horizontal bar line
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Write category names vertically
    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        res += "     "
        for name in names:
            if i < len(name):
                res += name[i] + "  "
            else:
                res += "   "
        if i < max_len - 1:
            res += "\n"

    return res
