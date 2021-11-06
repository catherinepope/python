print("Welcome to Treasure Island")
move1 = input(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right' \n").lower()

if move1 == "right":
    print("Game over!")
elif move1 == "left":
    move2 = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ").lower()
    if move2 == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif move2 == "wait":
        move3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if move3 == "red" or move3 == "blue":
            print("Game over!")
        else:
            print("You win!")

else:
    print("Sorry, I didn't recognise that instruction")


# add some different options

# ascii.co.uk
