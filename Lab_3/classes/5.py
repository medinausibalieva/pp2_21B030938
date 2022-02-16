class Account():
    owner = ''
    balance = 0
    
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def show(self):
        return f'Account owner: {self.name} \nAccount balance: {self.balance}' 
    def deposit(self, amount):
        self.balance += amount
        return f'Updated balance: {self.balance}'
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f'Remaining balance: {self.balance}'    
        return f'The operation cannot be performed!'    
person = Account('Medina Usibalieva', 500000)
print(person.show())
print(person.deposit(55500))   
print(person.withdraw(180000))
print(person.withdraw(1700000))     