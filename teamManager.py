 # makes a class function with an object
 class Player(object):
  def __init__(self, name, age, goals):
   self.name = name
   self.age = age
   self.goals = goals
   # makes a def function to print the players stats
   def printStats(self):
    print("name: " + (self.name))
    print("age: " + str(self.age))
    print("goals: " + str(self.goals))
# makes a print statement to print out the functions to add players
print("Welcome to fifa training camp, can you help us get some new players")
print("(1) add a player")
print("(2) print all players")
print("(3) exit fifa")
# makes a list function
playGame = []
# makes player_choice into an integer
player_choice = int(input())
# makes a while statement that makes player_choice stop the code after the user finishes making players
while player_choice != (3):
# makes a if statement so if the user wants to enter a player, they enter the number one
  if player_choice == 1:
# asks the user the question that asks the user for the players name 
    print("What is the players name?")
# makes playName into a string
    playName = input()
# asks the user the question that asks the user for the players age
    print("what is the players age?")
# makes playAge in an integer
    playAge = int(input())
# asks the user the question that asks the user how many goals the player has made
    print("How many goals did the player make?")
# makes playGoals into an integer
    playGoals = int(input())
    
    playGame.append(Player(playName, playAge, playGoals))
    print("What do you want to do now?")
    player_choice = int(input())
  elif player_choice == 2:
    for k in playGame:
      k.printStats()
      print("What do you want to do now?")
      player_choice = int(input())
