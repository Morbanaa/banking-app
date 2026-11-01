class BankAccount():
    def __init__(self,owner,password,balance):
        self.owner = owner
        self.password = password
        self.balance = balance

    def deposite(self):
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                self.balance += amount
            else:
                print("You must enter an amount greater than zero...")
        except ValueError:
            print("You must enter a numeric value")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount > self.balance:
                print("Not enough funds...")
            else:
                self.balance -= amount
        except ValueError:
            print("You must enter a numeric value")

    def change_password(self):
        while True:
            password = input("Enter current password(Q to Quit): ")
            if password == self.password:
                while True:
                    password1 = input("Please enter new password(Q to Quit): ")
                    password2 = input("Please confirm your password again(Q to Quit): ")
                    
                    values = ["Q","q","quit","QUIT","Quit"]
                    if password1 in values or password2 in values:
                        return
                    elif password1 == password2:
                        self.password = password2
                        return
                    else:
                        print("Please make sure the values you entered match")
            elif password == "Q" or password == "q":
                return
            else:
                print("Sorry that password does not match") 

    def display_info(self):
        print("==================================================================================")
        print(f"Owner: {self.owner}  ||  Balance: {self.balance}")

    def menu(self):
        while True:
            self.display_info()
            print("(1) Deposit")
            print("(2) Withdraw")
            print("(3) Change Password")
            print("(4) Return to bank menu")
            choice = input("Choose: ")
            print("==================================================================================")

            if choice == "1":
                self.deposite()
            elif choice == "2":
                self.withdraw()
            elif choice == "3":
                self.change_password()
            elif choice == "4":
                return
            else:
                print("Invalid input")