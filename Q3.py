class ATM:
    def __init__(self, password, balance):
        self.password = password
        self.balance = balance
        self.logged_in = False

    def login(self):
        user_password = input("Enter Password: ")

        if user_password == self.password:
            self.logged_in = True
            print("Login Successful")
        else:
            print("Wrong Password")

    def deposit(self):
        if self.logged_in:
            amount = int(input("Enter Deposit Amount: "))
            self.balance += amount
            print("Amount Deposited")
        else:
            print("Please Login First")

    def withdraw(self):
        if self.logged_in:
            amount = int(input("Enter Withdraw Amount: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Please Collect Your Cash")
            else:
                print("Insufficient Balance")
        else:
            print("Please Login First")

    def check_balance(self):
        if self.logged_in:
            print("Current Balance:", self.balance)
        else:
            print("Please Login First")

    def logout(self):
        if self.logged_in:
            self.logged_in = False
            print("Logged Out")
        else:
            print("You are already logged out")

atm = ATM("1234", 50000)

while True:
    print("\n1. Login")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Logout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.login()
    elif choice == 2:
        atm.deposit()
    elif choice == 3:
        atm.withdraw()
    elif choice == 4:
        atm.check_balance()
    elif choice == 5:
        atm.logout()
    elif choice == 6:
        print("Thank You!")
        break
    else:
        print("Invalid Choice")