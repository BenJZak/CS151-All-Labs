# Lab7

Grade: EMRN
Due: Before Next Lab

## Problem: 
Your friend just bought a new house, but all of the rooms have carpet or laminate that is horribly dirty and gross.  They need your help to know how much it will cost to re-do all of the floors!  They want to put hardwood, carpet, or tile in each of the rooms of their house.  They have all of the dimensions of the rooms, which are conveniently all rectangles! Their house has 5 rooms in it.

## Purpose: 
This lab gives you practice with:
* Designing and programming functions
* Re-using many of the other aspects of Python we've learned so far
* Testing code

## Details:

### Input and Output
You need to design, write, and test a program that calculates the cost of buying flooring for your friend’s house.  For each room you need to find out from the user the width (in terms of feet as a real number), the length (in terms of feet as a real number), and the flooring type (hardwood, carpet, or tile). The cost for each flooring type is set per square foot: Hardwood costs $1.39/sqft; carpet costs $3.99/sqft; and tile costs $4.99/sqft. You should output to your user the cost for each room, and then the overall cost as well.

### Error Checking
Unfortunately, you don’t really trust your friend to follow the directions in your program, so you need to protect your program from bad user input.  Use loops to force a valid flooring option and a valid dimension. Your program should work no matter what case they type the flooring option, or if they put extra whitespace before or after the word (so for example, "  HaRDwood  " should work for "hardwood").

### Design Hints
Start by thinking of the tasks for this problem. Then think how you'd solve a task, which may end up as your algorithm for that function. Write up the functions and their algorithms that you've thought of, then see what you are missing, or what seems like it needs to be moved to another function. Think about parameters (data your function needs to be able to run), and returned values (data the function gives back to whatever function calls it).

**If you find yourself doing the same set of steps many times, perhaps even just with different numbers, then those set of steps should probably be a function that you call in each of those places of your program.**

## Program Requirements:
When you plan your solution, you must take the following into account:  

1. Your program must be designed using functions. All code except a single function call to main must be in a function.
2. Your program must use a main function that actually does something. Do not have main just make a single call to another function and that's it.
3. Your program must include everything discussed above in the details section, including all error checking.

Functions now need to have function comments above them, similar to what we saw in the last set of lecture notes and in the solution to last week's lab. Above every function should be comments like the below:

```python
# Purpose:  [what problem does the function solve?]
# Parameters: [list with purpose in the same order they appear in the function header]
# Return: [return value, it's type, and what it represents]
```

## Steps:
1. Understand the problem
2. Write an algorithm in algorithm.txt showing the steps the program will go through to solve this problem, and the functions that will be used. For each function you need to note the name, parameters, returned value, and algorithm. All steps in your algorithm should be part of a function. **Take turns being driver for functions -- each partner should be writing the algorithm for half of the functions**
3. Test that your algorithm works by walking through it with example input, and re-reading the requirements above.
4. When you think your algorithm is correct, ask the lab instructor to approve it. *The lab instructor must approve your algorithm before you code*
5. Write your code following your algorithm and using good usability principles in main.py. **Take turns being driver -- each partner should code exactly half of the functions**
6. Properly comment your code with intro comments, **function comments**, and line comments
7. We're going to take a break from flowcharts for this lab. Write a set of test cases to test that your program works correctly. Make sure you fully test the error checking aspects of your program, and that you have at least one test that goes into each if statement option. You are welcome to draw a flowchart to help you ensure you have tested all paths, but you don't need to turn it in. Save test cases into testcases.xlsx.


## Submit:
1. To Replit:  
  * Your Python file (main.py)
  * Your algorithm (algorithm.txt)
2. To Moodle:  
  * Reflection (1 per partner): Discuss what you learned in lab, what it was like working with your partner, and what caused you the most trouble in lab. Also, what was different about using functions?
  * Your test cases (1 per group; testcases.xlsx)

