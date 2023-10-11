###### To View this document properly, click on the "eyeball" icon next to README.md above

# Lab 1 -- Learning to use Python Math, Input, and Output

* Grade: EMRN										
* Due: At the start of next lab

## Purpose: 

This assignment is aimed at giving you experience with Python math, variables, and user input. It will also give you more practice with learning to write and use test cases.

## Problem:

You are planning a road trip and need to figure out the cost for gas for your trip. You will need to know how many miles you will travel, the miles per gallon (MPG) of your car, and the cost of gas. Your program should work for any values of miles, MPG, and gas cost without needing to modify the code between runs. 

For the sake of this assignment we'll assume that all gas everywhere during a single trip has the same price, and that you always get exactly the same MPG on a particular trip.

## Requirements:

1.	Follow good programming practices.
2.	Follow the process below, including meeting all detailed requirements.
3.	Properly use variables, input, math, and output.
4.	Complete a set of test cases, and use them to test that your program works correctly. Fix any errors.
5.	Remember to perform pair programming, and be a good partner. When 1/2 the code is written, or 1/2 of class is over, switch drivers. 

## Details: 

You will write your program in the "pair programming" mode: one of you is the driver while the other is the navigator.

1.	Make sure you *understand the problem* you are being asked to solve. What are the input(s), output(s), and calculation(s)?

2.  *Driver 1 Write Test Cases*: create a series of test cases in Excel to use to determine that your program works correctly.  The first one is provided later in this document. You need to complete three others; there are suggestions in the test case details below. Have excel calculate the answer for you.

3.	*Driver 2 Complete the algorithm* for your calculations that is started in algorithm.txt – given the three starting values, what steps must you go through to get the answer you need? **Whoever didn't type the majority of the test cases, should type the algorithm** Your program should do ALL of the calculations for you, and should work for ANY valid inputs. Note algorithm.txt can be found under files. 

4. **Show your algorithm to Lab Instructor and get his/her approval BEFORE you start writing code**

5.	*Drivers take turns writing Code*: Edit `main.py`, and follow your approved algorithm to write your code. You may assume that your input will always be an integer, so that it is safe to typecast. Whoever has done the least typing at this point should start as driver.
   
    1.  Recall how input works in Python. There was an example on page 1 of Class Notes #3, as well as on in your zyBook 1.3. You need two steps so that the values become numerical.
    2.  Recall how math works in Python. Look back at your prep, or the book. Math symbols that may be helpful in this assignment include `+, -, *, /`.

6.	*Fix interpreter errors*: Run your program and fix any errors that appear.

7.	*Test:* Once your code runs and you think it’s complete, test it using your test cases -- run, give the input value as input, and see if you get the right output. If not, you need to fix the error(s) in your code!

8.	Make sure you’ve created a human readable essay (i.e. your program). Did you follow the code readability guidelines from Class Notes #3? If not, fix your code so that it is readable. You should have comments above each chunk of code!

9.	Include an updated version of the intro comments below at the very top of your Python file. Do not include the brackets `[` and `]` but replace them with what is asked for inside of them. Be sure to keep the titles at the start of each line. 
  ```
  # Programmers:  [your names here]
  # Course:  CS151, Dr. Olsen or Dr Kenyon or Mr Nweke 
  # Due Date: 9/XX/2023
  # Lab Assignment: 1
  # Problem Statement: [describe what task this program performs]
  # Data In: [list the type of information your user input requests]
  # Data Out:  [list the type of information output with print]
  # Credits: [Is your code based on an example in the book, in class, or something else?]
  ```

10.	Once you are done in lab, if you haven’t finished the assignment yet, you can work on the assignment later with your partner. Remember to SUBMIT when it's ready to be graded, and by the start of the next lab class.

### Test Cases:

You should create an Excel File and name it with parter last names. 
1. one row per test case  
2. one column each for description, each input, and each output  

Here's what the start of your Excel file should look like, with an example first test case and suggestions for additional test cases you will need to complete (see this in the rendered markdown for it to look like a table):

  |Test Description                 | in:miles  | in:MPG  | in:price  | out:cost|
  |----                             |----       | ----    | ----      | ----    |
  |Price is 1, we need 1 gallon     | 30        | 30      | 1         | 1       |
  |Zero miles, price is 1           |           |         |           |         |
  |Number of miles is greater than MPG |        |         |           |        |
  |Number of miles is less than MPG |           |         |           |       |


## What to Submit:

1.	In replit:

    1. Completed .py file  
    2. algorithm.txt 

2. To Moodle in the Lab1 assignment (only one partner needs to do this): An Excel file with your test cases.  
 
3. To Moodle in the Lab1 assignment: An individual reflection on the lab (at most 1 page in Word or PDF), answering the following questions:  
      1.  How was the experience working with your partner?   
      2.  What did you learn in this lab?   
      3.  How did you follow the first 3 rules of programming?   

As a reminder, reflections count toward your participation grade.
