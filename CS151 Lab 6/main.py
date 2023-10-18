#Lab 6
#Finn Powers and Ben Zakielarz

# Function to read the balance from the file
def read_balance():
    balance_file = open('balance.txt', 'r')
    balance = float(balance_file.read())
    balance_file.close()
    return balance

# Function to write the balance to the file
def write_balance(balance):
    balance = str(balance)
    balance_file = open('balance.txt', 'w')
    balance_file.write(balance)
    balance_file.close()

# Function to handle the deposit
def deposit(balance):
    deposit_amount = float(input("How much to deposit?"))
    while deposit_amount < 0:
        deposit_amount = float(input("Must be positive, How much to deposit?"))
    balance += deposit_amount
    print("Balance is $", balance)
    return balance

# Function to handle the withdrawal
def withdraw(balance):
    withdraw_amount = float(input("How much to withdraw?"))
    while withdraw_amount < 0:
        withdraw_amount = float(input("Must be positive, How much to withdraw?"))
    balance -= withdraw_amount
    if balance < 0:
        print("You have a negative balance. A 5% charge will occur.")
    print("Balance is $", balance)
    return balance

# Function to check the balance
def check_balance(balance):
    print("Balance is $", balance)
    if balance < 0:
        print("You have a negative balance. A 5% charge will occur.")

# Main ATM functionality
def main():
    print("This program is an ATM")
    balance = read_balance()

    while True:
        print("Please choose what you'd like to do:")
        choice = input("D eposit\nW ithdraw\nB alance\nE xit").upper().strip()

        if choice == "E":
            break
        elif choice == "D":
            balance = deposit(balance)
        elif choice == "W":
            balance = withdraw(balance)
        elif choice == "B":
            check_balance(balance)
        else:
            print("This is not a valid option.")

    print("Thanks for banking")
    write_balance(balance)


main()
