# Lab 10

Grade: EMRN

**Due:** By start of next lab

## Problem

In this lab assignment you will analyze data on movies, their budgets, and their profits

## Purpose

In this lab you will practice:

1. working with files
2. working with lists of lists

## Details

Provided in this repl is a file named "movies.csv" which contains information regarding approximately 600 movies. Each line contains comma-separated values about each movie in the following order:

* Release Date
* Movie	Budget
* Domestic Gross (e.g. money brought in from theaters)
* Worldwide Gross (e.g. money brought in from theaters)

Write a program which, given the name of a file of this format and the name of an output file, writes all movie information from the input file to the output file, but also adds a new column with the movie's profit (computed as box office worldwide gross minus the budget). Additionally, the program should determine which movie had either the highest profit or the lowest profit (you choose which one you'd like to do!) and output to the console all information related to that movie. 

### Programming Hint

The `split()` string function can split on something other than whitespace. You just pass the thing you want to split on as an argument when you call it.

### Error Checking
Unfortunately, you don’t really trust your user to follow the directions in your program, so you need to protect your program from bad user input.  You must continue asking for a file name until you are given one that exists for the input file. You do NOT need to check the name of the output file, because Python creates your output file for you if it doesn't exist.

### Output
The information you output to the file should be comma delimited (i.e. have a comma separating each value). There should be one movie per line. Remember that you can use string concatentation with "+" to combine two strings together before writing.

## Testing

You can use Excel to determine what your answers should be. Open the movies.csv file in Excel, and save it as an Excel file somewhere other than your repository. You should create a new column that is profit. Then calculate what the highest/lowest revenue should be. These are your value to test that your program correctly finds.

## Steps

We are going to do a new type of iterative development this lab:

1. Make sure you understand the problem
2. Code your main.py file while only writing the first 3 functions: a function to read in the filename from the user, a function to read the data from the file into a list of lists, and main to call these functions. **take turns driving**
3. Test that your code works correctly by adding in output in main.
4. Only once your code works, create algorithm.txt and plan how you will solve ONE of the tasks you need to do with this data (e.g. writing the data plus profit to a new file, OR finding the highest/lowest revenue movie). 
5. Write your code to solve this one task following your algorithm. Test it. **whoever didn't drive on the algorithm, should drive on the code**
6. Now write your algorithm for the remaining task. **whoever didn't write the last algorithm, writes this one**
7. Write your code for this remaining task. Test it. **whoever didn't write the code in step 5, writes this code**

You should be commenting your code as you go, but if you haven't already done so, make sure you put in all of the comments you need:
1. Comments within each function
2. Comments at the start of each function (purpose, paramters, return value)
3. Intro comments


## Submission

* To Replit:
  * algorithm.txt
  * main.py
* To Moodle:
  * Your excel file with solution values as described above (one per group)
  * Your reflection on what you learned in the lab and what it was like working with your partner (one per person)