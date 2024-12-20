class BankAccount:
   def __init__(self,account_number,balance=0):
        self.account_number=account_number
        self.__balance=balance
   def deposite(self,amount):
         if amount>0:
             self.__balance+=amount
             print(f'deposited:${amount}')
         else:
            print('deposite amount must be positive')    
   def withdrawl(self,amount):
         if amount>0  and amount<=self.__balance:
             self.__balance-=amount
             print(f'withdraw:${amount}')
         else:
            print('invalid or insufficient funds for withdrawl')
   def get_balance(self):
           return self.__balance
account=BankAccount('123456')
account.deposite(500)
account.withdrawl(200)
print('Balance:',account.get_balance())
