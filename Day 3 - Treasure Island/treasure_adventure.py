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
/______/______/______/______/______/______/______/______/______/______/_____/__
*******************************************************************************
''')
print("Welcome to Treasure Island!")
print("Find the treasure!\n")

print("You wash up on shore, stranded. You find a map on the beach, it appears to be of the island your on. It has patches missing, but it has a big red X.")
first = input("Do you want to follow the map, or try to swim out to find help?\n\tType \"map\" or \"swim\" ").lower()
if first == "map":
  print("Good Choice! You arrive at a missing patch of the map and see a cave in front of you. Do you go inside?")
  second = input("\tType \"cave\" or \"stay\" ").lower()

  if second == "cave":
    print("Its dark in the cave, but you find a skeleton holding a lighter. Do you take it?")
    third = input("\tType \"take\" or \"no\" ").lower()

    if third == "take":
      print("You take the ligher and use it to see in the cave, unfortunately the cave was filled with natural gas and you burn to death. Game over!")
    elif third == "no":
      print("You stumble through the cave, and kick something that sounds almost hollow. Do you investigate or run away?")
      fourth = input("\tType \"investigate\" or \"run\" ").lower()

      if fourth == "investigate":
        print('''
                __________________
              .-'  \ _.-''-._ /  '-.
            .-/\   .'.      .'.   /\-.
          _'/  \.'   '.  .'   './  \'_
          :======:======::======:======:  
          '. '.  \     ''     /  .' .'
            '. .  \   :  :   /  . .'
              '.'  \  '  '  /  '.'
                ':  \:    :/  :'
                  '. \    / .'
                    '.\  /.'   
                      '\/'
        ''')
        print("You found the treasure! You win!")
      elif fourth == "run":
        print("You run out of the cave, but trip in the dark and suffer from internal bleeding. Game over!")
      else:
        print("Invalid move.")
    else:
      print("Invalid move.")
      
  elif second == "stay":
    print("A bear arrives and eats you. Game over!")
  else:
    print("Invalid move.")
elif first == "swim":
  print("You get too tired and drown Game over!")
else:
  print("Invalid move.")
