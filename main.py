# Investor class
class Investor:

    balance = 0
    name = ""

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(self.name, ": $", self.balance)

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.deposit(-amount)


def main():
    inv0 = Investor("John", 15)
    inv0.check_balance()

    inv0.deposit(15)
    inv0.check_balance()

    inv0.withdrawal(10)
    inv0.check_balance()


if __name__ == "__main__":
    main()
