# Enter code here
# Read the README for instructions.
# You must write an algorithm and test cases first!

#ask user how many miles they travel, MPG of their car, and the cost of gas per gallon

miles = int(input("How many miles are you travelling?"))
mpg = int(input("what is the MPG of your car?"))
cpg = int(input("what is the cost of gas per gallon?"))

total = (miles/mpg)*cpg
print('You need', total, 'dollars for gas to travel.')
