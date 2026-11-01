from bank_account import BankAccount

class Bank():

    accounts = []

    @classmethod
    def create_new_account(cls):
        while True:
            while True:
                name = input("Please enter name for new account: ").title()
                if name != "":
                    unique = True
                    for account in cls.accounts:
                        if name == account.owner:
                            unique = False

                    if unique == True:
                        break
                    else:
                        print("That name is already in use, pick another one")

                else:
                    print("Your name must be at least one charactor long")
            while True:
                password1 = input("Please enter new password: ")
                password2 = input("Please confirm your password again: ")
                if password1 == password2:
                    break
                else:
                    print("Please make sure the values you entered match")
            while True:
                try:
                    balance = float(input("Enter initial amount to deposite into new account:"))
                    if balance >= 0:
                        break
                    else:
                        print("The amount may not be less than zero")
                except ValueError:
                    print("You may only enter numeric values")

            cls.accounts.append(BankAccount(name,password2,balance))
            return

    @classmethod
    def remove_account(cls):
        while True:
            name = input("Please enter name of account to remove(Q to Quit): ").title()
            if name == "Q" or name == "Quit":
                return
            elif name != "":
                for account in cls.accounts:
                    if name == account.owner:
                        print(f"{account.name}'s account removed")
                        cls.accounts.remove(account)
                        return
                print("Account not found")
            else:
                print("Your name must be at least one charactor long")

    @classmethod
    def login_to_account(cls):
        while True:
            while True:
                name = input("Please enter the name associated with the account: ")
                if name != "":
                    break
                else:
                    print("The name must be at least one charactor long")
            while True:
                password = input("Please enter the pasword: ")
                if password != "":
                    break
                else:
                    print("The name must be at least one charactor long")
            if not cls.accounts:
                print("The user name and password does not match any on file")
                return
            else:
                for index, account in enumerate(cls.accounts):
                    if account.owner == name and account.password == password:
                        account.menu()
                        return
                    elif index == len(cls.accounts) - 1:
                        print("The user name and password does not match any on file")
                        return
    
                    
                

                    
  
                    

    @classmethod
    def find_account_by_name(cls):
        pass

    @classmethod
    def show_all_accounts(cls):
        pass

    @classmethod
    def save_all_accounts(cls):
        pass

    @ classmethod
    def load_all_accounts(cls):
        pass
