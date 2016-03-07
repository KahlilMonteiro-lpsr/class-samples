# makes a class function with an object
class Player(object):
	def __init__(self, name, age, goals, jn, pos):
		self.name = name
		self.age = age
		self.goals = goals
		self.jn = jn
		self.pos = pos
# makes a def function to print the players stats
	def printStats(self):
		print("name: " + (self.name))
		print("age: " + str(self.age))
		print("goals: " + str(self.goals))
		print("jn: " + str(self.jn))
		print("pos: " + (self.pos))

def loadTeam(filename):
	pass


def saveTeam(playerList, filename):
	sauce = open(filename, 'a')
	for t in teamstats:
		sauce.write(t.name + ' ' + str(t.age) + ' ' + str(t.goals) + ' ' + str(t.jn) + ' ' + (t.pos) + '\n')

# makes a print statement to print out the functions to add players
print("Welcome to team manager deluxe!")
print("Do you want to start with a new team or an existing team?")
print("Enter the number of your choice and then press enter")
print("(1) start with a new team")
print("(2) open a file of an existing team")

player_choice = int(input())
if player_choice == 1:
	print("What is the players name?")
        playName = raw_input()
        print("what is the players age?")
        playAge = int(input())
        print("How many goals did the player make?")
        playGoals = int(input())
	print("what is your players jersey number?")
	playjn = int(input())
	print("what is your players position?")
	playpos = raw_input()
if player_choice == 2:
	print("What's the filename for your existing team? Enter your whole name, including its .tmd extension:")
	filename = raw_input() 
	print("What do you want to do? enter the number of your choice and press enter.")
	print("(1) add a player")
	print("(2) print all players")
	print("(3) print average number of goals for all players")
	print("(4) save your playerList to a file")
	print("(5) leave the program (save first so you won't lose your data)")
	player_choice = str(input())
	if player_choice == 1:
		print("What is the players name?")
        	playName = raw_input()
        	print("what is the players age?")
        	playAge = int(input())
        	print("How many goals did the player make?")
        	playGoals = int(input())
	if player_choice == 2:
		print("here are all the players!")
		my_file = open("pumas.tmd", 'r')
		print(my_file.read())
		my_file.close()
