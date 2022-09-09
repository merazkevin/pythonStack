


class BankAccount:
    population=0

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 
        print(f'Welcome your acccount Balance is *${balance}*')
        print(f'Welcome your acccount interest rate is *%{int_rate}*')
        BankAccount.population+=1

    # @classmethod
    def BankAccount_total(cls):
        print(f'Total acounts {cls.population}')

    def deposit(self, amount):
        self.balance= self.balance + amount
        print(f'You deposited ***{amount}***')
        print(f'Your new balance is ***{self.balance}***')
        return self

    def withdraw(self, amount):
        self.balance= self.balance - amount
        print(f'You have withdrawed ***{amount}***')
        print(f'Your new balance is ***{self.balance}***')
        return self

    def display_account_info(self):
        print(f'Your new balance is ***{User.self.account}***')
        

    def yield_interest(self):
        self.yield_interest=self.int_rate*self.balance
        self.balance= self.balance + self.yield_interest
        print(f'Your yield interest total is ***{self.yield_interest}***')
        print(f'Your new balance is ***{self.balance}***')
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    # other methods
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account)
        return self

    def make_withdraw(self, amount):
        self.account.balance+=amount
        return self

    def display_user_balance(self, balance):
        print(self.account.balance)
        return self

kevin=User('kevin', 'jfhdks@hfsdj.com')
kevin.make_deposit(100)
meraz=BankAccount(.02,0).deposit(180).deposit(1001).withdraw(233).withdraw(93).withdraw(3).yield_interest().display_account_info()

# BankAccount.BankAccount_total()