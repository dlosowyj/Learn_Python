#Adds a and b
def add(a, b):
    print("ADDING %d + %d." %(a, b))
    return a + b

#Subtracts b from a
def subtract(a, b):
    print("SUBTRACTING %d - %d." %(a, b))
    return a - b

#Multiplies a by b
def multiply(a, b):
    print("MULTIPLYING %d * %d." %(a, b))
    return a * b

#Divides a by b
def divide(a, b):
    print("DIVING %d / %d." %(a, b))
    return a / b

#Sets a bunch of variables to the outputs of the above functions
print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#Prints the variables just calculated
print("Age: %d, Height: %d, Weight: %d, IQ: %d." %(age, height, weight, iq))

#Dumb puzzle. Start from the innermost parentheses and work outwards.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, ". Can you do it by hand?")
