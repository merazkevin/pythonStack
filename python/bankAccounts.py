


class BankAccount:
    population=0

    def __init__(self, name, int_rate, balance,):
        self.int_rate = int_rate
        self.balance = balance 
        self.name= name
        print(f'Welcome your acccount Balance is *${balance}*')
        print(f'Welcome your acccount interest rate is *%{int_rate}*')
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
kevin1=BankAccount('kevin',0.01,0)

kevin.deposit(600).deposit(600).deposit(600).withdraw(10). yield_interest()

kevin1.deposit(100).deposit(100).withdraw(10).withdraw(10).withdraw(10).withdraw(10).yield_interest()

BankAccount.BankAccount_total()


# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account = BankAccount(int_rate=0.02, balance=0)
#     # other methods
    
#     def make_deposit(self, amount):
#         self.account.deposit(amount)
#         print(self.account)
#         return self

#     def make_withdraw(self, amount):
#         self.account.balance+=amount
#         return self

#     def display_user_balance(self, balance):
#         print(self.account.balance)
#         return self

