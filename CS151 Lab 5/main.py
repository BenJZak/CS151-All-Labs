# Programmers: Jarno, Ben 
# Course:  CS151, Dr. Kenyon
# Due Date: 10/17/23
# Lab Assignment: 5
# Problem Statement: Make a
# Data In: username, password, operation
# Data Out: balance
# Credits: N/A

# ~~~~~~~~~~ Keep this code - read from file
# DO NOT EDIT BELOW THIS LINE
balance_file = open('balance.txt','r') #open for Reading
balance = balance_file.read() #reads value from file
balance_file.close() #shut the door
balance = float(balance) #cast string to float
print("Present Balance is: $",balance)
# DO NOT EDIT ABOVE THIS LINE

# ~~~~~~~~~~ Students, enter code below

username = "bzjo467"
password = "password"

# user identification

user_verification = input("Type your username: ")
password_verification = input("Type your password: ")

# user verification

while user_verification != username or password_verification != password:
  print("Incorrect username or password.")
  user_verification = input("Type your username: ")
  password_verification = input("Type your password: ")

# ATM menu

print("Choose one of the following operations")
print("______________________________________")
print("D - Deposit")
print("W - Withdraw")
print("B - Balance")
print("E - Exit")
print("")

# ATM operations

operation = input("Enter your choice: ").strip().lower()

while operation != "e":
  
  if operation == "d":
    
    deposit = float(input("Enter the amount to deposit: "))
    if deposit < 0:
      print("Invalid deposit amount.")
    else:
      balance += deposit
      print("New balance is: $",balance)
      operation = input("Enter your choice: ").strip().lower()
      
  elif operation == "w":
    
      withdrawal = float(input("Enter the amount to withdrawl: "))
      if withdrawal < 0:
        print("Invalid withdrawl amount.")
      else:
        balance -= withdrawal
        print("New balance is: $",balance)
        if balance < 0:
          print("Warning: Your balance is negative. Your account will be charged with a 5% interest")
        operation = input("Enter your choice: ").strip().lower()
        
  elif operation == "b":
    print("Your current balance is: $",balance)
    operation = input("Enter your choice: ").strip().lower()
  else:
    print("Invalid choice.")
    operation = input("Enter your choice: ").strip().lower()
    
# Thank user

print()
print("Thank you for using the ATM!")


# ~~~~~~~~~~~ Keep this code - write to file, update balance
# DO NOT EDIT BELOW THIS LINE
balance = str(balance) #Text files only hold text, a.k.a. strings
balance_file = open('balance.txt', 'w')  # Open file to Write
balance_file.write(balance)  # Write balance to file
balance_file.close()  # Close the file
# DO NOT EDIT ABOVE THIS LINE





