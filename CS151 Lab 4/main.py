# Programmers:  Julius Boucke & Ben  Zakielarz
# Course:  CS 151 04 Kenyon
# Due Date: 10/10/23
# Lab Assignment: 4
# Problem Statement:  tell the customer how much they owe for their monthly bill based on their package, and how much data they used
# Data In: package type, coupon y/n, data usage
# Data Out:  total
# Credits: n/a

import math

#initialize variables
data_usage = 0
total_cost = 0
coupon = False

#gives the user the cell package options to choose from
print("Package Options:")
print()
print("Package Green")
print("_____________")
print("$49.99/month, 2GB data provided, $15/GB for additional data")
print()
print("Package Blue")
print("____________")
print("$70/month, 4GB data provided; 10/GB for additional data")
print()
print("Package Purple")
print("______________")
print("99.95/month, unlimited data")
print()
# get package type from user
package = input("What mobile phone provider package are you using? (Input Green, Blue, or Purple):" ).strip().lower()

#calculate total based on package type
if package == "green":
  coupon = input("Do you have a coupon for the Green Package? (Y/N): ").lower() == "y"
  data_usage = float(input("How much data have you used this month?: "))
  if data_usage > 2:
    data_usage -= 2
    data_usage = math.ceil(data_usage)
    total_cost = data_usage * 15
  total_cost += 49.99
  if (total_cost >= 75) and (coupon == True):
    total_cost -= 20
elif package == "blue":
  data_usage = float(input("How much data have you used this month?: "))
  if data_usage > 4:
    data_usage -= 4
    data_usage = math.ceil(data_usage)
    total_cost = data_usage * 10
  total_cost += 70
elif package == "purple":
  total_cost = 99.95
else:
  print("Invalid package name")
  exit()

#output
print()
print("You owe", f'{total_cost:.2f}', "dollars this month based on your package and data usage.")
