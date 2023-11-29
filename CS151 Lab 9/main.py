# Programmers: Ayana Thompson, Ben Zakielarz, Jarno Ottati
# Course: CS151, Dr. Kenyon
# Due Date: 11/14/2023
# Lab Assignment: 9
# Problem Statement: You are organizing a dinner party with assigned seats. Create a program to read in all of the attendees and then output the seat assignments.
# Data In: list of people user wants to invite
# Data Out: How many tables are needed, and who is sitting at each table
# Credits: Based of an example in class notes
# Input Files: kenyon.txt , nweke.txt , olsen.txt

# Purpose: list of Kenyon's students
# Parameters: none
# Return: values
def kenyon():
  fd = open("kenyon.txt", 'r')
  values = fd.readlines()
  fd.close()
  return values

# Purpose: list of Olsen's students
# Parameters: none
# Return: values
def olsen():
  fd = open("olsen.txt", 'r')
  values = fd.readlines()
  fd.close()
  return values

# Purpose: list of Nweke's students
# Parameters: none
# Return: values
def nweke():
  fd = open("nweke.txt", 'r')
  values = fd.readlines()
  fd.close()
  return values

# Purpose:  assign how many tables are needed
# Parameters: values of a list
# Return: 
def amountTables(values):
  index = 0
  for num in range(1, int(len(values) / 5) + 1):
    for i in range(1, 6):
      print("~~~~~~~~~~~~~~~~~~~~~~")
      print(f"Table {num}, Seat {i}, {values[index]}", end='')
      index += 1
  print("\n~~~~~~~~~~~~~~~~~~~~~~")

# Purpose: call main function
# Parameters: none
# Return: main()
def main():
  values = []
  print("This program will help organize your dinner party with assigned seats\n")
  print("Kenyon's Classes - 45 People\nNweke's Class - 25 People\nOlsen's Class - 35 People\n")
  invitees = input("Who would you like to invite, or type exit to stop:").lower().strip()
  while invitees != "exit":
    if invitees == "kenyon":
      values.extend(kenyon())
    elif invitees == "nweke":
      values.extend(nweke())
    elif invitees == "olsen":
      values.extend(olsen())
    else:
      print("\nInvalid Input, please input the name of the class section ONLY (no s at the end)\n")
    invitees = input("Who would you like to invite, or type exit to stop:").lower().strip()
  amountTables(values)
main()
