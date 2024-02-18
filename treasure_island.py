# welcome user to the game
# ask them if they want to go left or right
# if right --> game over, if left, ask them "swim or wait"
# if they say swim, game over, if they say wait, contine,
# then ask them which door, if they chose red, game over, 
# if they chose blue, game over, yellow, you win


def welcome_to_game():
    print("Welcome to Treasure Island.  Your mission is to find the treasure.")
    print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')

def treasure_island():
    choice1 = input("You're at a crossroad. Where do you want to go? Type left or right ").lower()
    if choice1 == "left":
        choice2 = input('You\'ve come to a lake.  There is an island in the middle of the lake.  Type "wait" to wait for a boat or "swim to swim across ' ).lower()
        if choice2 == "wait":
            print("A boat arrives and brings you safely to the island. ")
            choice3 = input("There are three doors once you reach the island: Red, blue, and yellow.  Pick the correct door to win the game. ").lower()
            if choice3 == "yellow":
                print("You found the Treasure!")
            else:
                print("Wrong door. You lose.")
        else:
            print("You were eaten by a shark.")

    else:
        print("You fell into a hole. Game Over.")

welcome_to_game()
treasure_island()

    


