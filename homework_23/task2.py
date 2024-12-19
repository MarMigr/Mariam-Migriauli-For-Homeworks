class BankAccount:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("საკმარისი თანხა არ არის")

    def get_balance(self):
        return f"თქვენს ანაგრიშზე არსებული თანხა: {self.balance}"


account = BankAccount(895)
account.deposit(150)
print(account.get_balance())
account.withdraw(300)
print(f"ბალანსი თანხის გამოტანის შემდეგ: {account.get_balance()}")
account.withdraw(2000)
print(f"თანხის გამოტანა  შეუძლებელია-: {account.get_balance()}")
