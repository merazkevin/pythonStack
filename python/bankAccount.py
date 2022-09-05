class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance 
        print(f'Welcome your acccount Balance is *${balance}*')
        print(f'Welcome your acccount interest rate is *%{int_rate}*')
        # don't worry about user info here; we'll involve the User class soon

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
        print(f'Your new balance is ***{self.balance}***')
        return self

    def yield_interest(self):
        self.yield_interest=self.int_rate*self.balance
        self.balance= self.balance + self.yield_interest
        print(f'Your yield interest total is ***{self.yield_interest}***')
        print(f'Your new balance is ***{self.balance}***')
        return self



kevin=BankAccount(.1,0).deposit(100).deposit(25).deposit(7.82).yield_interest().display_account_info()
meraz=BankAccount(.1,0).deposit(180).deposit(1001).withdraw(233).withdraw(93).withdraw(3).yield_interest().display_account_info()


