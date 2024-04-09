'''python program to replicate banking system with
1. a/c login
2. amut depo
3. amut withdraw'''


class BankAccount:

    def __init__(self, account_no, pin_no, balance_amount):
        self.account_no = account_no
        self.pin_no = pin_no
        self.balance_amount = balance_amount

    def account_login(self):
        x = int(input("Enter your account number: "))
        y = int(input("Enter your pin number: "))
        if x == self.account_no and y == self.pin_no:
            print("Login successful")
        else:
            print("Invalid account or pin number")

    def cash_depo(self, amount):
        if amount > 0:
            self.balance_amount += amount
            print("New balance:", self.balance_amount)
        else:
            print("Invalid entry")

    def cash_withdrawal(self, amount):
        if amount > 0 and amount <= self.balance_amount:
            self.balance_amount -= amount
            print("Debited amount is:", amount)
        else:
            print("Insufficient balance")

account_no = 3100001998
pin_no = 6865
balance_amount = 5000

# Account login
user1 = BankAccount(account_no, pin_no, balance_amount)
user1.account_login()

# Amount depositing
amount_depo = int(input("Enter depositing amount: "))
user1.cash_depo(amount_depo)

# Amount withdrawal
amount_withdraw = int(input("Enter withdrawal amount: "))
user1.cash_withdrawal(amount_withdraw)



