


class BankAccount:
    population=0

    def __init__(self, name, int_rate, balance,):
        self.int_rate = int_rate
        self.balance = balance 
        self.name= name
        BankAccount.population+=1

    @classmethod
    def BankAccount_total(cls):
        print(f'Total acounts {cls.population}')

    def deposit(self, amount):
        self.balance= self.balance + amount
        print(f'You deposited *${amount}*')
        print(f'Your new balance is *{self.balance}*')
        return self

    def withdraw(self, amount):
        if amount>self.balance:
            self.balance= self.balance - amount-5
            print(f'*WARNING* You have overdrawed *-${amount}* Charging a $5 overdraft fee')
            print('Unsufficient Funds! U --->BROKE<---')
        else:
            self.balance= self.balance - amount
            print(f'You have withdrawed *${amount}*')

        return self

    def display_account_info(self,):
        print(f'acount Name {self.name} balance*${self.balance}* interest rate*{self.int_rate}* ')
        

    def yield_interest(self):
        if self.balance > 0:
            self.yield_interest=self.balance * self.int_rate
            print(f'Your yield interest Yielded ${self.yield_interest} ')
            print(f'Your new balance is ${self.balance}')
        else:
            print('Unsufficient Funds! U --->BROKE<---')
        return self

kevin=BankAccount('kevin',0.01,0)
kevin.deposit(600).deposit(600).deposit(600).withdraw(10). yield_interest()

kevin1=BankAccount('kevin',0.01,0)
kevin1.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest()
BankAccount.BankAccount_total()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name,0.02, 0),
    # other methods
    def make_deposit(self, amount):
        self.account.balance += amount
        print(f'You deposited *${amount}*')
        print(f'Your new balance is *{self.account.balance}*')
    def make_withdrawal(self, amount):
        self.account.balance-=amount
        print(f'You withdrawal *${amount}*')
        print(f'Your new balance is *{self.account.balance}*')
    def display_user_balance(self,):
        print(self.account.balance)



wells=User('acccount','jdhasdff@gsdsa.com')
print(wells.name)
print(kevin.balance)
wells.make_withdrawal(150)
wells.display_user_balance()