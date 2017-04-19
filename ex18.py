#Takes args and prints them out. Assumes that args is just 2 in length
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r." %(arg1, arg2))

#Takes arg1 and arg2 and prints them out.
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r." %(arg1, arg2))

#Takes arg1 and prints it out.
def print_one(arg1):
    print("arg1: %r" %arg1)

#Takes no arguments and prints the same message every time.
def print_none():
    print("I got nothin'.")

#Uses the newly created functions.
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
