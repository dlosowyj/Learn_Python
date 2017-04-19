#Import the argv variable from the sys package
from sys import argv

#Set script and filename equal to the first and second arguments
script, filename = argv

#Print out the file name and give users instructions
print("We're going to erase %r." %filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#Wait for the user to hit enter (or really any button) or ctrl-c
input("?")

#Open the file in write mode
print("Opening the file...")
target = open(filename, "w")

#Delete the file by truncating everything after the current (i.e. before the first) line
print("Truncating the file. Goodbye!")
target.truncate()

#Give user information
print("Now I'm going to ask you for three lines.")

#Get three strings and store in line1, line2, line3
line1 = input("Line 1: ")
line2 = input("LIne 2: ")
line3 = input("Line 3: ")

#Give user information
print("I'm going to write these to the file.")

#Write the three input strings to the bare file
target.write("%s\n%s\n%s\n" %(line1, line2, line3))

#Close the file
print("And finally, we close it.")
target.close()
