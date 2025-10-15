class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0

    def menu(self):
        user_input = input("""
            Hello, how would you like to proceed?
                1. Enter 1 to create pin
                2. Enter 2 to deposit
                3. Enter 3 to withdraw
                4. Enter 4 to check balance
                5. Enter 5 to exit
            """)
        
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.user_deposit()
        elif user_input == "3":
            self.user_withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("Exit")
        else:
            print("Invalid option! Please try again.")
            self.menu()
    
    def create_pin(self):
        self.pin = input("Enter Your New Pin: ")
        print('Pin Create Successful')
        self.menu()
    
    def user_deposit(self):
        entered_pin = input("Enter your pin: ")
        if entered_pin == self.pin:
            amount = int(input("Enter your deposit Amount: "))
            self.balance += amount
            print("Deposit successful!")
        else:
            print("Invalid Pin! Try Again")
        self.menu()

    def user_withdraw(self):
        entered_pin = input("Enter your pin: ")
        if entered_pin == self.pin:
            amount = int(input("Enter your withdraw amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print(f'Withdrawn {amount} successfully')
            else:
                print("Insufficient balance!")
        else:
            print("Invalid Pin! Try again")
        self.menu()

    def check_balance(self):
        entered_pin = input("Enter your pin: ")
        if entered_pin == self.pin:
            print(f"Your balance: {self.balance}")
        else:
            print("Pin Incorrect!")
        self.menu()

A = ATM()
A.menu()




