print("Welcome to treasure island.")
print("Your mission is to find the treasure")
choice=input('you\'re at a crossroad, where do you wnat to go? type"left" or "right".').lower()
if choice=="left":
    choice1=input('You\'ve come to lake. There is an island in the middle of the lake.type"wait" to wait for a boat . type"swim " to swim across.').lower()
    if choice1=="wait":
        choice2=input("You arrive at the island unharmed.There is a house with 3 doors.one red,one yellow,one blue.which colour do you choose? ").lower()
        if choice2=="red":
            print("Its's a room full of fire.Game over.")
        elif choice2=="yellow":
            print("You found the treasure! You win")
        elif choice2=="blue":
            print("You enter a room of beast.Game over.")
        else:
            print("You choose a door that doesn't exist .Game over.")
    else:
        print("You got attacked by an angry fish.game over.")
        
else:
    print("You fell into a hole.Game over")

