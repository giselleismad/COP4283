# ===================================================================================================================
# kaylee
# assignment 0
# cop4283
# august 27, 2022
# ===================================================================================================================

# super simple higher lower game to get used to a few basic python
# syntax stuff again after not using for 4 years

mysteryNumber = 531;
guess = None; # declaring without assigning

print("Welcome to higher or lower! Type in a number 0-1000 to start playing!\n");

while guess != 531:
    guess = int(input("Enter a number: "));
    if guess > 1000 or guess < 0: # i forgot you cant use || for or
        print("Oops! You entered an invalid number! Enter a number 0-1000")
    elif guess > 531:
        print("Too high!")
    elif guess < 531: # write elif instead of else if in python
        print("Too low!")
    else:
        print("You won!")








