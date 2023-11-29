# Programmers: Ben Zakielarz and Ned Dietz
# Course:  CS151 Dr. Kenyon 
# Due Date: 11/21/23
# Lab Assignment: 10
# Problem Statement: Take the information from the file containing movie information and transcribing it to a file that contains the movie information along with the net profit from the films screenings (gross - budget)
# Data In: Read the contents of the [movies.csv] file and procure the movie information that contains the net profit from the provided movie information. 
# Data Out: Movie information including the net profit for each of the movies and which movie had the highest or lowest net profit. 
# Input Files: [movies.csv]

# Purpose: Asks the user for the name of the file they want to be written into the new file [file.csv]
# Parameters: NA
# Return: Returns the name of the file [filename]
def get_file():
  #Get user input for the name of the file.
  filename = input("What is the name of the file you want to read?: ")
  #Error checking against poor user input situated in a while loop.
  while not filename == "movies.csv":
    filename = input("Invalid file. Please enter the filename that you want to read: ")
  #Returns the correct file name to be used later.
  return filename

# Purpose: Opens the user's chosen file for reading and adds the information from that file into a list called [movies]. Includes measures to defend against poor user input (choosing a file that doesn't exist or doesn't contain the proper information). 
# Parameters: Uses the user's choice of file [filename]
# Return: Returns the filled list that is read from the chosen file. 
def read(filename):
  #Create empty list that will store the read in information from the user's chosen file. 
  movies = []
  try: 
    #Open and read each line of movies.csv.
      file = open(filename, 'r')
      for line in file:
        data = line.split(",")
        movies.append(data)
      file.close()
  except:
      print("File not found")
  #Return the now filled movies list.
  return movies

# Purpose: Calculates the profit for each film (summation of gross profits and subtracting the budget of the film) and adds this value to a new empty list called [profit list].
# Parameters: Reads in the [movies] list from the {read} function to determine how long the for loop will run for. 
# Return: The list containing the total profit information for each movie. 
def get_profit(movies):
  #Create empty list that will contain the calculated profits for each movie.
  profit_list = []
  for i in movies:
    #Takes the value of the budget for the movie from the second index of the list.
    budget = int(i[2])
    #Determines the total revenue by adding the values of index 3 and 4 (domestic and international sales).
    gross = (int(i[3]) + int(i[4]))
    #Calculates the profit.
    profit = gross - budget
    profit_list.append(profit)
  #Returns the completed list with the calculated profits. 
  return profit_list

# Purpose:  [what problem does the function solve?]
# Parameters: [list each parameter's purpose, not just its name]
# Return: [return type and what it represents]
def write_profit(movies, profit_list):
  fd = open("file.csv", 'w')
  for i in range(len(movies)):
    write = (f"\n{movies[i]}, The profit from this movie is: ${profit_list[i]} \n")
    fd.write(write)
  fd.close()

# Purpose: Find the highest profit movie from the calculated profits. 
# Parameters: [Profit_list] and [movies] values being used to find the maximum profit. 
# Return: Prints out the highest grossing film and the value in the consolse. 
def get_big_movie(movies, profit_list):
  #Uses the max function to find the largest profit value.
  largest = max(profit_list)
  highest = 0 
  profit_length = len(profit_list)
  #Creates a loop that matches the name of the movie to the corresponding highest profit movie.
  for profit in range(profit_length):
    if profit_list[profit] == max(profit_list):
      print(f"The movie with the highest profit is: {movies[profit][1]} with ${largest}.\n[All movie info: {movies[profit]}]\n")

# Purpose: Find the lowest profit movie from the calculated profits. 
# Parameters: [Profit_list] and [movies] values being used to find the lowest profit. 
# Return: Prints out the lowest grossing film and the value in the consolse. 
def get_small_movie(movies, profit_list):\
  #Uses the min function to determine the lowest profit value from the profit list. 
  smallest = min(profit_list)
  lowest = 0 
  profit_length = len(profit_list)
  #Creates a loop that matches the name of the movie to the corresponding lowest profit movie.
  for profit in range(profit_length):
    if profit_list[profit] == min(profit_list):
      print(f"The movie with the lowest profit is: {movies[profit][1]} with ${smallest}.\n[All movie info: {movies[profit]}]\n")

# Purpose: Contain the above functions to be called. Includes a message that is dispalyed to the user that explains the purpose of the program. 
# Parameters: NA 
# Return: Prints a message to the user explaining the purpose of the program to the user. 
def main():
  print("This program will print information about movies from a file!")
  grab_file = get_file()
  print("You can find your information from movies.csv in file.csv in the files bar on the left side of your screen.\n")
  scan_file = read(grab_file)
  calculate_profit = get_profit(scan_file)
  include_profit = write_profit(scan_file, calculate_profit)
  find_highest_profit = get_big_movie(scan_file, calculate_profit)
  find_lowest_profit = get_small_movie(scan_file, calculate_profit)

main()
