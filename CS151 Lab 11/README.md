# Lab 11 MORSE CODE
* Grade: EMRN	
* Due: Before next lab class

## Problem
Someone has converted your files using a cipher! Ciphers have been very popular for millenia as a way to hide information. Can you create a program to convert them back to plain English??

## Purpose
This lab gives you practice with: 
* Using dictionaries
* Following problem-solving techniques
* Creating functions
* Doing file I/O

## Details
Morse code is a code for representing letters such that it can be communicated via blinking lights or sounds. 
There are only 2 symbols: dots (.) and dashes (-). A specific ordering of dots and dashes represents a particular letter, number, or symbol. You can see an example of morse code as a communication signal at https://www.youtube.com/watch?v=_J8YcQETyTw&ab_channel=DaveHimslef.

Open your `morsecode.txt` file to see the conversions. You have all English letters, the digits of base 10, and a few punctuation symbols. This file tells you how to convert between Morse code and English, with a *tab* between the two columns.

The files you must convert are written in Morse Code with a space between the letters, with one word per line.

## Design
**For this lab you MUST use iterative development. You must work on your algorithms in a specific order. See the Steps, and FOLLOW them.** 

Your program will first read in `morsecode.txt` to learn the conversions – think about the best way to store this information. 

Then it will ask the user for the name of a file that is written in Morse code, convert it to English, and write the English conversion out to a NEW file (whose name is also chosen by the user).

Your program MUST ask for the following information from the user: the name of your file that shows the conversions (e.g. `moresecode.txt` in this case), the name of the input file that is written in morse code, and the name of the output file. 

## Steps:
**Take turns driving by function.** Every time you move to a new function, change who is typing. Just move the keyboard over, you don't need to swap seats.

1. Make sure you understand the problem
2. Design: You will need functions to do: file name input error checking, storing conversion information from morsecode.txt, reading in the morse code text, converting from morse to English and writing that conversion to a file, and main. For the design phase, you need to determine the parameters, return types, and general approach for each function (including the data structure to use). A full algorithm is not required.
3. *You should not need more than 15 minutes for the design step.* Ask questions if you get stuck! **Show the professor your design.** 
4. Follow iterative development! Write one function at a time, updating main to call the functions as you go, getting it to work before moving on. First should be file name input, and then reading in morsecode.txt and storing appropriately for later use. **switch drivers between functions**
5. Put output in main to test that your function to store you conversion from morsecode to letters is correct. You can delete this output once you've determined your code works so far.
6. Next write the function for converting a file written in morsecode to a file written in English. Test it to see that it works.
7. Write comments in your code to make it clear what it is doing.
8. Write comments for each function in your code. 
9. Include an updated version of the header comments. Be sure to note that you need input files in the "Other files" part! 

## Programming Hints
The code for this assignment is fairly short, but there are a few little things that might trip you up when you go to code your algorithm. Here are a few hints to help with that issue:
* Be careful how you name the variables in your for loops. Meaningful naming will make coding it correctly a LOT easier.
* The letter and morse code value in the file are separated by a tab. A tab is just another form of whitespace.
* You will need to strip both the key and the value after reading it from the file to remove whitespace. Otherwise your code won’t be able to find the answer correctly.

## Submit:
1. To Replit:
* Your main.py file 

2. To Moodle:
* (1 per person) A short individual reflection including:
  *  what you did in lab, what it was like working with your partner, and what you had the most trouble with. 
  * What was written in each of the files written in Morse code? (Just give a brief description, don’t need to print out text)
  * How would you modify the code so that it could convert in the other direction (from English to Morse)? (The change is minor)
  * Could this Python program be used to convert from a different code other than Morse code? Why or why not?

