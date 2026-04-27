# write a python code to impliment bank account system recuirement create a class with private variable and impliment seposte withdraw and check balance
class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to the Machine")
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\nAmount Deposited:", amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\nYou Withdrew:", amount)
        else:
            print("\nInsufficient balance")
    def display(self):
        print("\nNet Available Balance =", self.balance)
if __name__ == "__main__":
    s = BankAccount()  
    s.deposit()        
    s.withdraw()       
    s.display()        