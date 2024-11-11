# Python Banking Program

def show_balance(balance):
    print(f"Your balance is Ksh{balance:.2f}")


def deposit():
    amount = float(input("Enter amount to deposit: "))
    if amount < 0:
        print("That is invalid")
        return 0
    else:
        return amount


def withdrawal(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("-----------------------------------")
        print("        BANKING PROGRAM")

        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdrawal(balance)
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thankyou have a nice day!!")


if __name__ == '__main__':
    main()
