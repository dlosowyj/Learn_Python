from sys import exit

# Gloabl variable to keep track of the choice of room
climber = False

# Handle the problems of the climbing room
def climbing_room():
    # The global identifier is necessary to adust the global variable's value
    global climber 
    climber = True

    print("Welcome to the climbing room!")
    
    # Keep looping until a suitable option is chosen
    while True:
        print("Do you prefer climbing or top roping?")
        choice = input("> ")

        if choice == "top roping":
            print("You climb up to the top and find a spectacular view.")
            mountain_view()
        elif choice == "bouldering":
            print("You're jacked as hell, but you should probably rest.")
            take_break("Your arms are pumped.")
        else:
            print("That's not climbing. Try again, you dumb kayaker.")

# Handle the problems of the running room
def running_room():
    print("Welcome to the running room!")

    # Keep looping until a suitable option is chosen
    while True:
        print("Do you want to do a long, slow run or do some HIIT?")
        choice = input("> ")

        if choice == "long, slow run":
            print("You run up a nice road to the top of a mountain.")
            mountain_view()
        elif choice == "HIIT":
            print("That was a mistake.")
            take_break("You threw up.")
        else:
            print("What the hell are you, a kayaker?")

# Handle problems on the mountain, if this was reached
def mountain_view():
    print("At the top of the mountain you find a dragon.")
    print("What do you do?")

    # Keep looping until a suitable option is chosen
    while True:
        choice = input("> ")
        
        if choice == "climb back down" and climber:
            print("The dragon respects your expertise and gives you a crisp high five.")
            take_break("Time to go home.")
        elif choice == "climb back down" and not climber:
            print("The dragon admires your courage and gives you a clean fist/claw bump.")
            take_break("Time to go home.")
        elif choice == "run" and not climber:
            print("You're super tired. The dragon flies you home.")
            take_break("Time to go home.")
        elif choice == "run" and climber:
            print("You look ridiculous running. The dragon asks you to stop.")
            take_break("Time to learn how to run.")
        else:
            print("Why are you so uninteligible?")

# Start the program by asking for a choice of room
def start():
    print("Hey! There are two rooms in front of you.")
    print("Do you want to go to the climbing or running room?")
    
    choice = input("> ")

    if choice == "climbing":
        climbing_room()
    elif choice == "running":
        running_room()
    else:
        print("Well now you get nothing.")
        take_break("Walk home in shame.")

# Exit the program nicely
def take_break(reason):
    print(reason, "good job!")
    exit(0)

start()
