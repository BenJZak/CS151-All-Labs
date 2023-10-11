# Programmers:  Ben + Tim
# Course:  Computer Science 151
# Due Date: Tuesday, October 3, 2023, 12:00 AM
# Lab Assignment: Lab 3
# Problem Statement: Calculate the distance traveled based on speed and determine how many points a skier will receive if they went that distance
# Data In: Hill type and speed at the bottom of ramp
# Data Out: Points skier earned and a reactionary statement
# Credits: https://www.fis-ski.com/DB/alpine-skiing/calendar-results.html?categorycode=WC&disciplinecode=&eventselection=&gendercode=&nationcode=&place=&racecodex=&racedate=&saveselection=-1&seasoncode=2022&seasonmonth=X-2022&seasonselection=&sectorcode=AL

import math

#initiate variables that are used in if statements
points = 0
height = 0

#Gather hilltype and speed from user input
hillType = input("What is the hill type of your jump? (Normal/Large): ").strip().lower()
speed = int(input("What speed were you travelling at the end of the ramp: "))

#Calculate the points based on values for the normal hill
if hillType == "normal":
  height = 46
  par = 90
  air_time = math.sqrt((2*height)/9.8)
  distance_traveled = speed * air_time
  points = 60 + (distance_traveled - par)*2

#Calculate the points based on values for the large hill
if hillType == "large": 
  height = 70
  par = 120
  air_time = math.sqrt((2*height)/9.8)
  distance_traveled = speed * air_time
  points = 60 + (distance_traveled - par)*1.8

#depending on the points earned, output different statements to the user
if points >= 61:
  print("Great job doing better than par!")
elif points < 10:
  print("What happened??")
else:
  print("Sorry you didn't go very far :(")

#output the points earned
print()
print("Points:", round(points, 2))
