
def diamond_room():
  print("You are now in a room filled with diamonds!")
  print("There is a door too!")
  print("What would you like to do? (1 or 2)")
  print("1). Take some diamonds and go through the door.")
  print("2). Just go through the door.")

  answer = input()
  
  if answer == "1":
    print("These diamonds are harmful diamond.The moment you touched it, it was killed you.")
  elif answer == "2":
    print("Nice, You are a lucky person because you are honest.")
    print("Game over")
  else:
    print("Please type the right number.")

def bear_room():
  print("There is a bear here.")
  print("Behind the bear is another door.")
  print("The bear is eating tasty honey!")
  print("What would you like to do? (1 or 2)")
  print("1). Take the honey.")
  print("2). Killthe bear.")

  answer = input()
  
  if answer == "1":
    print("The bear killed you.")
    print("Game over")
  elif answer == "2":
    print("You are a lucky man.You entered to another room.")
    print("you are now inside of the diamond room.")
    diamond_room()
  else:
    print("Don't you know how to type a number?")

def monster_room():

  print("Now you entered into room of a monster.")
  print("The monster is sleeping.")
  print("Behind the monster, there is another door. What would you like to do? (1 or 2)")
  print("1). Go through the door silently.")
  print("2). Kill the monster and show your courage!")

  answer = input()


  if answer == "1":
    diamond_room()
  elif answer == "2":
    print("The monster was hungry, he ate you.")
    print("Game over")
  else:
    print("please type a right number.")



def start():
  print("You are standing in a dark room.")
  print("There is a room in your left and right.")
  print("which room do you like to proceed? [L or R]")

  answer = input()

  if answer == "L":
    bear_room()
  elif answer == "R":
    monster_room()
  else:
    print("Don't you know how to type something properly?")

start()
