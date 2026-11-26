class Category():
    def __init__(self,name):
        self.name = name
        self.ledger = []
    

    def deposit(self, amount, description=''):
        self.ledger.append({'amount' : amount, 'description' : description})
        
    def withdraw(self, amount, description=''):
        total = 0
        for item in self.ledger: 
            total += item['amount']
        if total >= amount:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total
    
    def transfer(self, amount, category):
        if self.withdraw(amount, f"Transfer to {category.name}"):
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()
        
    def __str__(self):
        output = f"{self.name:*^30}\n"
        for item in self.ledger:
            output += f"{(item['description'])[:23]:<23}{item['amount']:>7.2f}\n"
        
        output += f"Total: {self.get_balance():.2f}"
        return output

def create_spend_chart(categories):
    withdrawals = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item['amount'] < 0:
                spent += -item['amount']
        withdrawals.append(spent)

    total_spent = sum(withdrawals)
    percentages = []
    for spent in withdrawals:
        perct = int((spent / total_spent) * 100) // 10 * 10
        percentages.append(perct)

    chart = "Percentage spent by category\n"
    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for pct in percentages:
            if pct >= level:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_len - 1:
            chart += "\n"

    return chart