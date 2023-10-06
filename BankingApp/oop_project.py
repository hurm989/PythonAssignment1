from main import *

Dave=BankAccount(1000,"Dave")
Sara=BankAccount(1000,"Sara")

Dave.getBalance()
Sara.getBalance()

# Dave.deposit(500)
Sara.deposit(200)

Dave.withdraw(10000)

Dave.transfer(1000,Sara)
Dave.transfer(100,Sara)

Jim=InterestRewardAcc(1000,'Jim')

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100,Dave)

Blaze=SavingAcc(1000,"Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(1000,Sara)