from Bank_accounts(CODE) import *

Sonu = Bank_accounts(1000,"Sonu")
Monu = Bank_accounts(2000,"Monu")

Sonu.get_balance()
Monu.get_balance()

Sonu.deposit(500)

Sonu.withdraw(1000000)

Sonu.transfer(50000,Monu)
Sonu.transfer(500,Monu)


Jim = Interest_reward_account(1000,"Jim")

Jim.get_balance()

Jim.deposit(100)

Jim.transfer(200,Sonu)


Tinku = Saving_account(5000,"Tinku")

Tinku.get_balance()

Tinku.deposit(500)

Tinku.transfer(2000,Monu)

Tinku.get_balance()

Tinku.withdraw(5000)


Jim.withdraw(300)
