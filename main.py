from savings_account import SavingsAccount
from menu import show_menu

name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

account = SavingsAccount(name, balance)

while True:

    show_menu()

    choice = input("Enter choice: ")

    if choice == "1":
        amount = int(input("Enter deposit amount: "))
        print(account.deposit(amount))

    elif choice == "2":
        amount = int(input("Enter withdraw amount: "))
        print(account.withdraw(amount))

    elif choice == "3":
        print("Balance:", account.get_balance())

    elif choice == "4":
        print(account.add_interest())

    elif choice == "5":
        account.display_account()

    elif choice == "6":
        break

    else:
        print("Invalid choice")