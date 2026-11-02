from bank_account import BankAccount
import json
from pathlib import Path

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
            cls.save_all_accounts()
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
                        print(f"{account.owner}'s account removed")
                        cls.accounts.remove(account)
                        cls.save_all_accounts()
                        return
                print("Account not found")
            else:
                print("Your name must be at least one charactor long")

    @classmethod
    def login_to_account(cls):
        while True:
            while True:
                name = input("Please enter the name associated with the account: ").title()
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
                print("There are no current user accounts")
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
        while True:
            user = input("Enter the name of the account your looking for: ").title()
            if user == "":
                print("You must enter somthing")
                continue

            found = False
            for account in cls.accounts:
                if account.owner == user:
                    found = True
                    print("==================================================================================")
                    print(f"Your search returned:")
                    account.display_info()

            if found == False:
                print("==================================================================================")
                print(f"The account under ({account.owner}) was not found")
            return

    @classmethod
    def show_all_accounts(cls):
        cls.accounts.sort(key=lambda account: account.owner)
        print("All user bank accounts:")
        if not cls.accounts:
            print("No user accounts yet")
        else:
            for account in cls.accounts:
                account.display_info()
        print("==================================================================================")

    @classmethod
    def save_all_accounts(cls):
        script_dir = Path(__file__).resolve().parent
        project_root = script_dir.parent
        file_path = project_root / "data" / "accounts.json"

        data = []
        cls.accounts.sort(key=lambda account: account.owner)
        try:
            with open(file_path,"w") as file:
                for account in cls.accounts:
                    user = {}
                    user["Owner"] = account.owner
                    user["Password"] = account.password
                    user["Balance"] = account.balance
                    data.append(user)

                json.dump(data,file,indent=4)
                print(f"Saved successfully to: {file_path}")

        except FileNotFoundError:
            print("That file was not found")

    @ classmethod
    def load_all_accounts(cls):
        script_dir = Path(__file__).resolve().parent
        project_root = script_dir.parent
        file_path = project_root / "data" / "accounts.json"

        try:
            with open(file_path,"r") as file:
                users = json.load(file)

                for user in users:
                    cls.accounts.append(BankAccount(user["Owner"],user["Password"],user["Balance"]))
                
        except FileNotFoundError:
            print("File not found")
