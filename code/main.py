# Teddy Rodd
# Banking App

"""
changes:
Make it so the user can request to cancel their account and withdraw funds. 
The request is sent to admin who can then acc epot the change
"""
from bank import Bank

def main():
    Bank.load_all_accounts() 
    launch_banking_app()
    print("==================================================================================")
    print("Have a great day!")
    print("==================================================================================")

def bank_menu(status):
    while True:

        if status == "USER":
            print("==================================================================================")
            print("--- Bank Menu ---")
            print("(1) Create an account")
            print("(2) Login to Account")
            print("(3) Return to main menu")
            choice = input("Choose: ")
            print("==================================================================================")

            if choice == "1":
                Bank.create_new_account()
            elif choice == "2":
                Bank.login_to_account()
            elif choice == "3":
                return
            else:
                print("Invalid input")


        else:
            print("==================================================================================")
            print("-- Bank Menu Admin ---")
            print("(1) Find account by name")
            print("(2) Remove account")
            print("(3) Show all accounts")
            print("(4) Return to main menu")
            choice = input("Choose: ")
            print("==================================================================================")

            if choice == "1":
                Bank.find_account_by_name()
            elif choice == "2":
                Bank.remove_account()
            elif choice == "3":
                Bank.show_all_accounts()
            elif choice == "4":
                return
            else:
                print("Invalid input")

def launch_banking_app():
        admin_password = "FISH"
        while True:
            print("==================================================================================")
            print("Launch Program as:")
            print("(1) User")
            print("(2) Admin")
            print("(3) Exit Program")
            choice = input("Choose: ")
            print("==================================================================================")

            if choice == "1":
                bank_menu("USER")
            elif choice == "2":
                while True:
                    value = input("Enter Admin Password(Q Return Menu): ").upper()
                    if value == "Q" or value == "QUIT":
                        break
                    elif value != admin_password:
                        print("Invalid Password...")
                    else:
                        print("Login as Admin Granted...")
                        bank_menu("ADMIN")
                        break
            elif choice == "3":
                return
            else:
                print("Invalid Input")

           
if __name__ == "__main__":
    main()