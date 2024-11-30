#Banking Program
def show_balance():
    print(f"Your balance is Rs {balance}")

def deposit():
    global balance  
    amount = float(input("Enter the amount to deposit:"))
    if amount < 0:
        print("That's not a valid amount")
    else:
        balance += amount
        print(f"Rs {amount} deposited successfully!")

def withdraw():
    global balance 
    amount = float(input("Enter the amount to withdraw:"))
    if amount > balance:
        print("Insufficient funds")
    elif amount < 0:
        print("Amount must be greater than 0")
    else:
        balance -= amount
        print(f"Rs {amount} withdrawn successfully!")

balance = 0
is_running = True

while is_running:
    print("\nWelcome")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter Your choice (1-4): ")
    if choice == '1':
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        is_running = False
        print("Thank You")
    else:
        print("Invalid Choice! Try Again!")