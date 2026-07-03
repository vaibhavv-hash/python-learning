balance = 1000
while True:
    print("\n=====Welcome to ATM=====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    print("5. Reset balance")
    choice = int(input("Choose : "))
    if choice == 4:
        print("Thank you for using ATM")
        break
    if choice == 1:
        print("Current Balance : ", balance)
    if choice == 2:
        deposit = int(input("Enter amount to deposit : "))
        balance += deposit
        print("Deposit Successful")
        print("Current Balance : ", balance)
    if choice == 3:
        withdrawal = int(input("Enter the amount to withdraw : "))
        if withdrawal <= balance:
            balance = balance - withdrawal
            print("Successfully withdrew the amount")
            print("current balance : ", balance)
        else:
            print("Insufficient balance")