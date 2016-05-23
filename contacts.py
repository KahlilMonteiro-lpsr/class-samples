class Number(object):
 def __init__(self, name, number):
  self.name = name
  self.number = number

 def printContacts(self):
  print("Welcome to Contacts")
  print("What would you like to do?")
  print("(1) Add a phone number.")
  print("(2) Print the full list of contacts.")
  print("(3) Enter a name to retrieve that contact's phone number.")
  print("(4) Exit the Contacts app.")

contacts = []

contact_numbers = int(input())

while contact_numbers != (3):
  if player_choice == 1: 
    print("What is the contacts name?")
    playName = raw_input()
    print("what is the contacts number?")
    playAge = int(input())
  
  elif contact_number == 2:
	for num in contacts:
		num.printContacts()
