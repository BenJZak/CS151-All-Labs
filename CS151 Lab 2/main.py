# Programmers:  [Savion & Ben]
# Course:  CS151 
# Due Date: 9/26/23
# Lab Assignment: 3
# Problem Statement:  
# Data In:
# Data Out:
country = input("Which country would you like to estimate?")

birthRate = float(input("How many seconds between birthds? "))
deathRate = float(input("How many seconds between each death?"))
immigrants = float(input("What is the rate of immigrants per second?"))
population = float(input("What is the current population?"))
futureYears = float(input("How many years into the future would you like to estimate?"))

estPop = (((31536000/birthRate) - (31536000/deathRate) + (31536000/immigrants))*futureYears) + population

estPop = int(estPop)
futureYears = int(futureYears)

print("The population of", country, "in", futureYears, "will be", estPop)

if(estPop > population):
  print("Population increased!")
elif(estPop < population):
  print("Population decreased!")
else:
  print("Population remained the same?")
