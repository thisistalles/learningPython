class Bank:
    def __init__(self):
        self.cach = 300
    
    def check_balance(self):
        print(f'your cach: {self.cach}')

    def withdraw(self,value):
        if not value > self.cach:
            self.cach -= value
            self.check_balance()
            print(f'your withdraw is {value}')
        else:
            print("you can't make the withdrawal")

    def create_deposit(self,value):
        self.cach += value
        self.check_balance()

bank = Bank()

while True:
    print("\n-Enter 1 to check balance\n-Enter 2 to withdraw\n-Enter 3 to create deposit\n-Enter 4 to exit")
    option = int(input("\n> "))

    if option == 1:
        bank.check_balance()
    elif option == 2:
        value = int(input("Enter a withdrawal amount: "))
        bank.withdraw(value)
    elif option == 3:
        value = int(input("Enter a deposit amount: "))
        bank.create_deposit(value)
    elif option == 4:
        break
#thiscl