correct_pin="1234"
balance = 10000

entered_pin=input("Enter your PIN : ")

if entered_pin == correct_pin :
    print("PIN Verified")

    amount=int(input("Enter the amount withdraw : Rs."))

    if amount<=0:
        print("Amount should be greater than zero")

    else :
        if amount<= balance :
            if amount % 100 == 0 :
                balance -= amount
                print("Withdrawal Successfull")
                print("Remaining Balance : Rs.",balance)
            else :
                print("Amount must be in multiple of 100")
        else :
            print("Insufficient Balance")
            print("Current Balance : Rs.",balance)
else :
    print("Incorrect PIN")

