# CS151 Lab 9
Grade: EMRN
Due: Before Next Lab

## Problem
You are organizing a dinner party with assigned seats. Create a program to read in all of the attendees and then output the seat assignments.

## Purpose
This lab gives you practice with: 
* Following problem-solving techniques
* Doing file I/O
* Storing data in lists

## Details

We want to have a class dinner party at the end of the semester. Catering services will provide as many tables as we need, with each table seating five people. Your goal is to determine and output:

1. How many tables are needed. 
2. Who is sitting at each table.


### File details
You have three different files with all the students names as well as the instructor's name for each CS151 instructor.  There is one name per line in a file. All files are of the same format, and if you write your code correctly, it should run for any of the files without needing to change any lines of code!

### Input 
You must ask the user the name of the file to read the names from.

After you find out the name of the file, you can read that file to input the data from the file. Read into a list.

### Output
 
Determine and output how many tables we will need. Fortunately the number of attendees is a multiple of 5 in each file.

We will need name signs to go at each seat. Each sign should have table number, seat number and guest's name. The output on seating assignments should be similar in style to:

```
~~~~~~~~~~~~~~~~~~~~~~~
Table 1, Seat 1, Jones
~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~
Table 1, Seat 2, Smith
~~~~~~~~~~~~~~~~~~~~~~~
```

### Programming Details
Your program must read in all of the information stored in the file, and store it in a list before doing any processing.

You must use for loops.

Make sure your input/output follows good usability rules.

Use iterative development as you design algorithm and write code. Test as you go.

## Design
You must design your functions and their algorithms before you start coding. Think about the tasks that need to be solved. Be sure to look back at yesterday’s notes, as the setup is much the same.


## Steps:
1. Make sure you understand the problem
2. Determine the functions you need to solve this problem. Remember that a function solves a high level task for the program. Then write your algorithm for the function that determines the seating arrangement (you do not need to write the rest of the algorithms, but you do need to figure out what functions you need). **Take turns driving. Have your design approved by the professor before you start your code.**
3. Write your code.  Follow iterative development like you did in design – get one part working completely before moving on to the next part. Test it as you write it! **take turns driving**
4. Test your code to make sure it is working correctly. You may need to add some extra print statements to see what values are being used, or the value of the list (remove them for your final version).  **Be sure to test with all input files.**
5. Write comments in your code to make it clear what it is doing.
6. Write comments for each function in your code. Recall that the following comments should be at the start of each function:
   
```python
# Purpose:  [what problem does the function solve?]
# Parameters: [list each parameter's purpose, not just its name]
# Return: [return type and what it represents]
```

7. Include an updated version of the intro comments. Note the new final line below about "Input files". Be sure to note that you need input files that contain one name per line! 
```python
# Programmers:  [your names here]
# Course:  CS151, Dr. Olsen/ Dr. Kenyon/ Mr. John 
# Due Date: [date assignment is due]
# Lab Assignment:  [number of assignment]
# Problem Statement:  [what problem does your code solve; i.e., calculating inches from centimeters]
# Data In: [what information do you request from the user?]
# Data Out:  [What information do you display for the user?]
# Credits: [Is your code based of an example in the book, in class, or something else?  Reminder: you should never take code from the Internet or another person.]
# Input Files: [description of the format of the input files you need for this program to work]
```


## Submit:
* To Replit
    * Your completed algorithm (algorithm.txt)
    * Your main.py file 
    
* To Moodle
    * A short individual reflection about what you did in lab, what it was like working with your partner, and what you had the most trouble with. (1 per person)


