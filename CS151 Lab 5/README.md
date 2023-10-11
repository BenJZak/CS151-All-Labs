# Lab5
Grade: EMRN  
Due: Before Next Lab

## Problem: 
Build a simulation of an ATM (Automatic Teller Machine), where users can see their balance, deposit (e.g. add money to the account), or withdraw (e.g. take money from the account).

## Purpose: 
This lab gives you practice with:
* Designing and programming loops
* Re-using many of the other aspects of Python we've learned so far
* Testing code
* Error checking
* Brief experience with reading and writing text files

## Details:

The initial balance is stored in a text file (balance.txt) and updated at the end of the program. The first time you run the program the balance is $1000; after that, it will be whatever the balance ended as the last time you ran the program. *You do NOT need to write any code related to interacting with the file; it is written for you. You can assume you have balance available at the start of your steps.*

You should make up a password for your user to enter -- your choice. The user must enter username and password. If the entered password is wrong, keep asking.

The user can choose any of the following options as they interact with your program:
* D - Deposit
* W - Withdraw
* B - give Balance
* E - Exit   (loop until choice is E - sentinel value)

After the user inputs an option, you do the correct task related to that action. Then they get to choose an action again. Only when they choose to exit does it stop looping.

### Error Checking
Unfortunately, users often don't pay attention to what they are typing. Give an error and ask them to try again when

1. choice is not D,W,B or E. Case should not matter for D/W/B/E choice.
2. a negative number is given for amount to deposit or withdraw
3. a wrong password is entered.
4. The balance becomes negative. Warn them that they will be charged 5% interest (do not actually bother calculating this, it's just an output).

### Design Hints
Start by thinking of the tasks for this problem. Then think how you'd solve a task, which may end up as your algorithm for that section. Focus on what it needs to do without the loops or error checking, then once that makes sense add in the looping and then the error checking.

If you find yourself doing the same set of steps many times, perhaps even just with different numbers, then those set of steps should probably be in a loop.

## Steps:
1. Understand the problem
2. Write an algorithm in algorithm.txt showing the steps the program will go through to solve this problem.
3. Test that your algorithm works by walking through it with example input, and re-reading the requirements above.
4. When you think your algorithm is correct, ask the lab instructor to approve it. **The lab instructor must approve your algorithm before you code**
5. Write your code following your algorithm and using good usability principles. 
6. Properly comment your code with intro comments and line comments
7. We're going to take a break from flowcharts for this lab. Write a set of test cases to test that your program works correctly. Make sure you fully test the error checking aspects of your program, and that you have at least one test that goes into each if statement option. You are welcome to draw a flowchart to help you ensure you have tested all paths, but you don't need to turn it in. Save test cases into testcases.xlsx.


## Submit:
1. To Replit:  
  * Your Python file (main.py)
  * Your algorithm (algorithm.txt)
2. To Moodle:  
  * Reflection (1 per partner): Discuss what you learned in lab, what it was like working with your partner, and what caused you the most trouble in lab.
  * Your test cases (1 per group; testcases.xlsx)

