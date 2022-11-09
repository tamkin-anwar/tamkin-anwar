class BankAccount:
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else: 
            print("Insufficant Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

savings = BankAccount (.04,2000)
checking = BankAccount (.02,5000)

savings.deposit(100).deposit(500).deposit(1200).withdraw(600).yield_interest().display_account_info()
checking.deposit(525).deposit(450).withdraw(200).withdraw(100).withdraw(30).withdraw(20).yield_interest().display_account_info()

BankAccount.print_all_accounts()