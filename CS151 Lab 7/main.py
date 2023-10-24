# Programmers: Ben, Bonita
# Course:  CS151, Dr. Kenyon
# Due Date: 10/31/23
# Lab Assignment: 7
# Problem Statement: Design, write, and test a program that calculates the cost of 
# buying flooring for your friend’s house
# Data In: type of flooring, length and width of room
# Data Out: cost per room and total cost of flooring
# Credits: N/A


# Purpose:  Ask for prefered floor type and outputs cost based on it 
# Parameters: No parameters
# Return: Returns cost based on choice input

def floorType():
  type = input("What floor type would you prefer: ").lower().strip()
  # Makes sure valid floor type is input
  while type != "hardwood" and type != "carpet" and type != "tile":
    print("\nInvalid Type\n")
    type = input("What floor type would you prefer: ").lower().strip()
  if type == "hardwood":
    return 1.39
  elif type == "carpet":
    return 3.99
  else:
    return 4.99

# Purpose:  Returns a cost of a room based length and width and prints it out to user
# Parameters: cost and count (for room number)
# Return: Returns cost of one room 

def area(cost, count):
  len = float(input("What is the length of the room(in ft)?: "))
  wid = float(input("What is the width of the room(in ft)?: "))
  # Makes sure length and width are valid numbers
  while (len < 0 or wid < 0):
    print("\nInvalid length or width; must be postitve\n")
    len = float(input("What is the length of the room(in ft)?: "))
    wid = float(input("What is the width of the room(in ft)?: "))
  totCost = round(cost * len * wid, 2)
  print(f"Room {count} will cost {totCost}")
  return totCost

# Purpose:  Prints opening statements and calls the previously defined functions 5 times
# Parameters: No parameters
# Return: Outputs total cost at the end of the program

def main():
  # Opening statements
  print("----------------")
  print("Welcome! This program will calculate flooring prices for each of your rooms.")
  print("----------------")
  print("Hardwood - $1.39 per sq/ft\nCarpet - $3.99 per sq/ft\nTile - $4.99 per sq/ft")
  print("----------------")
  
  count = 1
  totalCost = 0
  # Calls functions 5 times
  while count < 6:
    type = floorType()
    print()
    cost = area(type, count)
    print()
    totalCost += cost
    count += 1
  print("Your total cost will be", totalCost)
  print("Thank you for using the program!")

main()
