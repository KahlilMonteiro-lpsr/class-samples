 self.age = age
    self.goals = goals
  def printStats(self):
    print("name: " + (self.name))
    print("age: " + str(self.age))
    print("goals: " + str(self.goals))
    
print("Welcome to fifa training camp, can you help us get some new players")
print("(1) add a player")
print("(2) print all players")
print("(3) exit fifa")
playGame = []
player_choice = int(input())
while player_choice != (3):
  if player_choice == 1:
    print("What is the players name?")
    playName = input()
    print("what is the players age?")
    playAge = int(input())
    print("How many goals did the player make?")
    playGoals = int(input())
    playGame.append(Player(playName, playAge, playGoals))
    print("What do you want to do now?")
    player_choice = int(input())
  elif player_choice == 2:
    for k in playGame:
      k.printStats()
      print("What do you want to do now?")
      player_choice = int(input())
