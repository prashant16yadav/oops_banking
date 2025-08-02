class balance_exception(Exception):
    pass

class Bank_accounts:
    def __init__(self,initialAmount,name):
        self.balance = initialAmount
        self.name = name
        print(f"\nAccount '{self.name}' created.  Balance = ${self.balance:.2f}")


    def get_balance(self):
        print(f"\nAccount = '{self.name}'  Balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance+= amount
        print("\nDeposit Complited.")
        self.get_balance()


    def viable_transaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise balance_exception(
                f"\nSorry '{self.name}' you only has a balance of {self.balance:.2f}"
                )
        
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print("\nwithdraw complited.")
            self.get_balance() 
        except balance_exception as error:
            print(f"\nwithdraw interrupted :{error}")


    def transfer(self,amount,account):
        try:
            print("\n\n********** \n\nBegining transfer..🚀")
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Completed!✅\n**********")
        except balance_exception as error:
            print(f"\nTransfer Interrupted❌")


class Interest_reward_account(Bank_accounts):
    def deposit(self, amount):
        self.balance += (amount *1.05)
        print(f"\n deposit completed! , {amount} + 5% interest ")
        self.get_balance()


class Saving_account(Interest_reward_account):
    def __init__(self, initialAmount, name):
        super().__init__(initialAmount, name)
        self.fee = 5

    def withdraw(self, amount):
        
        try:
            self.viable_transaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            self.get_balance()
            print("\nWithdraw Completed!")
        except balance_exception as error:
            print(f'\nWithdraw interrupted: {error}')






