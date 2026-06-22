balance=50000
pin="1234"
Pin=input("enter your pin:")
if pin==Pin:
    while True :
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            print("Your balance is:",balance)
        elif choice==2:
            amount=int(input("Enter amount to withdraw:"))
            if amount>balance:
                print("Insufficient balance")
            else:
                balance-=amount
                print("Withdrawal successful. Your new balance is:",balance)
        elif choice==3:
            amount=int(input("Enter amount to deposit:"))
            balance+=amount
            print("Deposit successful. Your new balance is:",balance)
        elif choice==4:
            print("Thank you for using our service.")
            break
        else:
            print("Invalid choice. Please try again.")