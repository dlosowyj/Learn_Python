def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" %cheese_count)
    print("You have %d boxes of crackers!" %boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

def this_is_dumb(is_dumb, how_dumb, dumb_adjective):
    if(is_dumb):
        print("I told you this was at least %d dumb. Just %s." %(how_dumb, dumb_adjective))
    else:
        print("Really? You're wrong. This is %s. Like %d dumb points." %(dumb_adjective, how_dumb))

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

is_dumb = input("Is this dumb (Y/N)? ")
if(is_dumb == "Y"):
    is_dumb = True
else:
    is_dumb = False
this_is_dumb(is_dumb, 15, "silly willy")
