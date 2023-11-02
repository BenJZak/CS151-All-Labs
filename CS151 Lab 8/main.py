import random


def occurence(rollResults, rollOccurence):
  for i in range(len(rollResults)):
    rollResults[i] = random.randint(1,6) + random.randint(1,6)
  count = 0
  diceVal = 2
  while count < 11:
    rollOccurence[count] = rollResults.count(diceVal)
    count += 1
    diceVal += 1
  print(rollOccurence)
  print()
  count = 0
  diceVal = 2
  while count < 11:
    if count < 8:
      print("Sum of", diceVal, "","*"*rollOccurence[count])
    else:
      print("Sum of", diceVal, "*"*rollOccurence[count])
    count += 1
    diceVal += 1

def main():
  diceAmount = int(input("How many dice would you like to roll?: "))
  print()

  rollResults = [0]*diceAmount
  rollOccurence = [0]*11
  occurence(rollResults, rollOccurence)

main()
