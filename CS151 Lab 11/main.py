# Programmers:  [Andrew, Ben]
# Course:  CS151, Dr. Kenyon
# Due Date: [11/28/2023]
# Lab Assignment:  [11]

#Name of function: read_morse_code
#Purpose: reads in the morse code keys and values from a file and stores keys and vals in a dictionary
#Returns: a decrypted morse code dictionary
def read_morse_code_file(file_path):
  morse_code_dict = {}
  with open(file_path, "r") as file:
    for line in file:
      #split each line into ascii character and Morse code
      ascii_char, morse_code = line.strip().split("  ")
      #store in the dictionary
      morse_code_dict[ascii_char] = morse_code
  return morse_code_dict

#Name of function: translate_morse_code_to_english
#Purpose: translates encrypted morse code to decrypted readable english 
#Returns: whatever the decrypted message is
def translate_morse_code_to_english(file_path, morse_code_dict):
  #open and read the file
  with open(file_path, "r") as file:
    morse_code_strings = file.readlines()

  english_text = ""
  #iterates through the read in strings
  for morse_code_string in morse_code_strings:
      morse_code_words = morse_code_string.strip().split(" ")
      for morse_code_word in morse_code_words:
        if morse_code_word in morse_code_dict.values():
          #find the corresponding key (ASCII character) for the Morse code and then add it to the end of the string initialized  
          english_text += [key for key, value in morse_code_dict.items() if value == morse_code_word][0]
        else:
          #if there's no match, consider it as a space between words
          english_text += " "
      english_text += " "  # add space between lines

  return english_text.strip()

#Name of function: write_translation_to_file
#Purpose: writes the translated text doc to a new file
#Returns: a new file with translated morse code
def write_translation_to_file(output_file_path, translation):
  with open(output_file_path, "w") as output_file:
    output_file.write(translation)

#Name of function:main
#Purpose:considers general operations and routing
#Returns:NA
def main():
  # file_path and the subsequent line used to create a dictionary with corresponding values
  file_path = "morsecode.txt"
  morse_code_dictionary = read_morse_code_file(file_path)
  file = input("Would you like to translate morse code file 1, 2, or 3?: ").strip()
  #checks if user input a 1 2 or 3
  if file in {"1", "2", "3"}:
    output_file_path = input("Enter the name of the output file: ").strip()
    morse_code_file_path = f"morse{file}.txt"
    translation = translate_morse_code_to_english(morse_code_file_path, morse_code_dictionary)
    write_translation_to_file(output_file_path, translation)
    print(f"Translation written to {output_file_path}")
  #otherwise print invalid input and ask again
  else:
    print("\nInvalid Input")
    main()

#call main :3
main()
