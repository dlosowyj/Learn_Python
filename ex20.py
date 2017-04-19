#Import the argv variable
from sys import argv

#Sets script and input_file equal to argv
script, input_file = argv

#Prints the file
def print_all(f):
    print(f.read())

#Goes to the first line of the file
def rewind(f):
    f.seek(0)

#Prints the line_count-th line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())

#Opens the given file
current_file = open(input_file)

#Prints the file
print("First let's print the whole file: \n")

print_all(current_file)

#Goes back to the beginning of the file
print("Now let's rewind, kind of like a tape.")

rewind(current_file)

#Prints the first three lines one at a time
print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
