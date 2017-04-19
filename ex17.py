#Import the argv variable and the exists function
from sys import argv
from os.path import exists

#Set script, from_file, and to_file equal to the arguments
script, from_file, to_file = argv

#Tell the user we're going to copy the from_file to to_file
print("Copying from %s to %s." %(from_file, to_file))

#Get the text from the from_file
indata = (open(from_file)).read()

#Check if the to_file exists. Copy the files if it does.
if(exists(to_file)):
    out_file = open(to_file, 'w')
    out_file.write(indata)

    print("Alright, all done.")
    out_file.close()
else:
    print("%s doesn't exist." %to_file)
