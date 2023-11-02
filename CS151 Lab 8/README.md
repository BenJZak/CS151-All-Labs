# CS151 Lab 8

* Grade EMRN 
* Due: Before Next Lab

## Problem
Dr. K. is obsessed with playing backgammon and understanding the probability and distribution of rolling dice. Create a program to display the distribution of rolls of two dice.

## Purpose
This lab gives you practice with: 

  * Lists
  * Functions
  * Loops (possibly nested)
  * Random numbers

## Details
Write a program to simulate rolling a pair of 6-sided dice based on how many times a user requests the dice to be rolled. 
Ask the user how many rolls to do (one roll means one pair of dice are rolled). Every time a pair is rolled, get the sum of the 2 numbers from that roll, and keep track of the sums in a list.
The sums of the rolls will vary from 2 to 12 (do you understand why?). 

After gathering the data, create a chart like the one below to display the distribution of rolls at the end of the program. For example: if a 2 was rolled twice, there should be two "*" after "Sum of 2". Actual results will vary, but you should follow the same style.


### Output

In the output below, the `[2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1] ` is outputting the number of rolls per potential total. Your values will likely be different.

The output should be similar to the following in style:
```
Rolling 100 pairs of dice                                                                                             
[2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1]                                                                                
Sum of 2  **
Sum of 3  ********
Sum of 4  ***********
Sum of 5  ***********
Sum of 6  ***************
Sum of 7  ***************
Sum of 8  *****************
Sum of 9  *********
Sum of 10 *******
Sum of 11 ****
Sum of 12 *   
```

### Programming Tips

* You can use methods from the random module such as random.randint to simulation a die roll. Look up how to use this function if you don't remember.
* You should make sure the user enters a valid value for number of rolls. Make them try again until they enter a valid value.
* The only user input should be the number of rolls. Don't ask the user to do something for every die roll.
* You must use functions in your program. All code must be in a function other than imports. Don't forget main!


## Design
You should use iterative development for this problem. We suggest using the following smaller problems to help you devise a solution: How would you roll one die? Two dice? A hundred times? How would you increment the value in the list? How would you print the corresponding asterisks?

## Steps:
1. Make sure you understand the problem
2. Write your algorithm in algorithm.txt. Get your lab instructor's approval. Use functions. **Take turns driving**
3. Write your code in main.py to match your algorithm. Writing each piece and then testing it before moving on is a great way to do iterative development. To succeed on this lab it is crucial that you get each piece working before moving on to the next. **Take turns driving**
4. Write comments in your code to make it clear what it is doing. Don't forget function comments (purpose, parameters, return) above every function.


## Submit:
* To Replit
  * Your completed algorithm (algorithm.txt)
  * Your main.py file 
* To Moodle
  * A short individual reflection about what you did in lab, what it was like working with your partner, what you had the most trouble with, and what did you observe when you increase or decrease the number of rolls? (1 per person)



