class BankAccount:
    # __init__ method accepts an argument for the accounts balance, it is assigned to __balance attribute
    def __init__(self, bal):
        self.__balance = bal

    # the deposit method makes a deposit into the account
    def deposit(self, amount):
        self.__balance += amount

    # the withdraw method withdraws an amount from the account
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Error: Insufficient funds")

    # the get_balance method returns the account balance
    def get_balance(self):
        return self.__balance
