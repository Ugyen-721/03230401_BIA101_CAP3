# Github Repo link: https://github.com/Ugyen-721/03230401_BIA101_CAP3
# Your Name: Ugyen Dendup
# Your Section: BBI B 
# Your Student ID Number: 03230401
################################
# REFERENCES
#https://www.w3schools.com/python/python_conditions.asp
#https://www.w3schools.com/python/python_while_loops.asp
#https://youtu.be/GqBoZZ6ZJxk?si=YcKMe6_q7qyTlUts
#https://youtu.be/uq7-ZiKlacw?si=o2cWFcTfSYzM8OVt
#https://youtu.be/-gjxg6Pln50?si=PLbLZHewHY2sQmsL
################################
# SOLUTION
# The Solution Score: 489577
################################

def process_line(line): #This line defines a function named process_line that takes a single argument named line
  line_str = str(line) #This line converts the input line argument (which might not be a string) into a string type and stores it in the variable line_str. This ensures we can work with string characters for processing.
  left, right = 0, len(line_str) - 1  #left is set to 0, which represents the starting index of the string.
                                      #right is set to the length of the string (len(line_str)) minus 1
  

#This code scans a string using two pointers to find the first and last digit characters, 
#exiting the loop when both are found.
  while left <= right:                  
    if not line_str[left].isdigit():
      left += 1
    elif not line_str[right].isdigit(): 
      right -= 1 
    else:
      break

#No digits found, skip line
  if left > right:  
    return None

#This code extracts the first and last digits from the string, combines them into a two-digit number, and returns it.
  first_digit = int(line_str[left])
  last_digit = int(line_str[right])
  two_digit_number = first_digit * 10 + last_digit
  return two_digit_number

#Sets up a variable to hold the running total of all two-digit numbers found.
total_sum = 0

#This code opens a text file, iterates through each line, 
#calls the process_line function to extract two-digit numbers, 
#and adds those values to a running total.
with open(r"C:\Users\user\Desktop\BIA 101\401.txt") as input_file:
  for line in input_file:
    two_digit_value = process_line(line.strip())  # Remove trailing newline
    if two_digit_value:
      total_sum += two_digit_value

print("The total sum of from the given input file 401.txt is", total_sum)
