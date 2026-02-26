# EXERCISE 2
# AUTOMATIC ATM

account = 1000

while True:
    print("Welcome to the ATM")
    print("1. consulting balance")
    print("2. deposit")
    print("3. withdrawing")
    print("4. exit")
    
    option = input(" Select one option: ")
    if option == "1":
        print(f"consulting balance, your balance is {account}")
        break
    elif option == "2":
        print("depositing")
        deposit = int(input(" enter the amount to deposit: "))
        account += deposit
        print(f"your new balance is {account}")
        break
    elif option == "3":
        print("withdrawing")
        whithdraw = int(input("enter the amount to withdraw: "))
        if whithdraw > account:
            print(" insufficient funds")
            break
        else:
            account -= whithdraw
            print(f"your new balance is {account}")
            break
    elif option == "4":
        print("exiting")
        break