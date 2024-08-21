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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left", "right", or "straight".\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across. '
                    'Type "build" to build a raft.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is a house with 3 doors. One red, "
                        "one yellow, and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print('''
                ________
               |  FIRE  |
               |  _/  \_|
               |  / .-. \\
               |  \ `-' /
               |___`"`___|
               |   . .   |
               |  '   '  |
               |         |
               |_________|
            ''')
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print('''
             .-""""""-.
           .'          '.
          /   O      O   \\
         :           `    :
         |                |   
         :    .------.    :
          \  '        '  /
           '.          .'
             '-......-'
            ''')
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print('''
               (    )
              (((  )))
              (O)  (O)
                |  |
                |  |
                |  |
                |  |
              .-'  `-.
             /        \\
            |          |
            | |      | |
            | |      | |
            |_|      |_|
            '-'      '-'
            ''')
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    elif choice2 == "swim":
        print("You got attacked by an angry trout. Game Over.")
    elif choice2 == "build":
        print('''
                ~~~~~~~
             ~~~~~~~~~~~~
          ~~~~~~~~~~~~~~~~
       ~~~~~~~~~~~~~~~~~~~~~
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        ''')
        choice3 = input("You successfully built a raft and crossed the lake. "
                        "Now, you see two paths: one leading into a dark forest, "
                        "another to a mountain. Which path do you take? "
                        "Type 'forest' or 'mountain'.\n").lower()
        if choice3 == "forest":
            print("You got lost in the forest. Game Over.")
        elif choice3 == "mountain":
            print('''
                     .       .
                    / `.   .' \\
            .---.  <    > <    >  .---.
            |    \  \ - ~ ~ - /  /    |
             ~-..-~             ~-..-~
          \~~~\.'                    `./~~~/
           \__/                        \__/
            /                  .-    .  \\
     _._ _.-    .-~ ~-.       /       }   \/~~~/
    (   ~.-~       }~ ~ ~-._/       /    \__/
     `\  {       }                 /     |
       \  ~-.__  _-~ ~-          .-~ ~   |
        ~ ~-._~\  \      }-.._ .~         |
             \  \  \     }~ ~ ~-.._   _.-~
              \ `\  ~-.__.-~ ~-.    ~-. ~~-._
               `~ ~-.~ ~-.__.-~ ~-._   ~-.__.~\\
                  ~-._~ ~-.__.-~ ~-.__.-~ ~-.~\\
                      ~-._~ ~-.__.-~ ~-.__.~-.~\\
                          ~-._~ ~-.__.-~ ~-.__.~\\
            ''')
            print("You climb the mountain and discover a hidden cave filled with glowing crystals and mysterious "
                  "artifacts. ")
            choice4 = input("Do you 'take' the crystals, 'explore' further, or 'leave'?\n").lower()
            if choice4 == "take":
                print("The crystals start glowing brighter, enveloping you in light. You are transported to another "
                      "dimension filled with endless adventures! You Win!")
            elif choice4 == "explore":
                print('''
                     /`\\  /`\\
                  .-'`  `""`  `"-.
                .`                `.
                /                    \\
               /                      \\
              ;                        ;
              |                        |
              |       ________         |
              |      |   _    |        |
              |      |  |_)   |        |
              |      |  |_    |        |
              |      |________|        |
              |                        |
              |                        |
              |                        |
              |                        |
              :                        :
               \                      /
                \                    /
                 `-.______________.-
                ''')
                print("You find a hidden chamber filled with ancient technology and blueprints for inventions beyond "
                      "imagination. You Win!")
            elif choice4 == "leave":
                print("You decide it's better not to mess with things you don't understand. You leave the mountain "
                      "safely and live to tell the tale.")
            else:
                print("You hesitated too long. The cave collapses and you are trapped. Game Over.")
        else:
            print("You chose a path that doesn't exist. Game Over.")
    else:
        print("You made an invalid choice and lost. Game Over.")

elif choice1 == "right":
    print("You fell into a quicksand pit. Game Over.")

elif choice1 == "straight":
    print("You found an old map that leads you to a hidden treasure chest. Inside, you find a portal to an "
          "intergalactic adventure. You Win!")
else:
    print("You stumbled around and got lost. Game Over.")
