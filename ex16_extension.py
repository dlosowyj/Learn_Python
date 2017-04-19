from sys import argv

script, filename = argv

print("We're going to print out %r." %filename)
txt = open(filename)
print(txt.read())
