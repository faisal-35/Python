class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self._account_holder = account_holder
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
        else:
            print('Invalid balance amount. Balance cannot be negative.')

    def get_account_holders(self):
        return self._account_holder

    def deposite(self, amount):
        if amount > 0:
            self._balance += amount
            print(f'deposited: ${amount}')
        else:
            print('Deposit amount must be positive')

    def withdrawl(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f'withdrawn: ${amount}')
        else:
            print('Invalid or insufficient funds for withdrawal')


# Testing the code
account = BankAccount('123456', 'Alice', 100)
print('Account holder:', account.get_account_holders())
print('Balance:', account.get_balance())
account.deposite(50)
print('Balance after deposit:', account.get_balance())
account.withdrawl(30)
print('Balance after withdrawal:', account.get_balance())
