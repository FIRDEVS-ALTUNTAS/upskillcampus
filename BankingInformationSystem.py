class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def open_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print("Account opened successfully.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print("Deposit successful. Current balance:", self.accounts[account_number])
        else:
            print("Account does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print("Withdrawal successful. Current balance:", self.accounts[account_number])
            else:
                print("Insufficient funds.")
        else:
            print("Account does not exist.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print("Current balance:", self.accounts[account_number])
        else:
            print("Account does not exist.")

# Örnek Kullanım
bank = Bank("MyBank")
bank.open_account("12345", 1000)
bank.deposit("12345", 500)
bank.withdraw("12345", 200)
bank.check_balance("12345")
