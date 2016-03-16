print("How old are you?")
age = int(input())

print("What's your GPA?")
GPA = float(input())

# if GPA is over 3.0 and age is 16, accept
if GPA > 3.0 and age > 16:
	print("Congrats, you have been accepted to columbia!") 
else:
	print("Sorry, guess you'll have to go to harvard instead.")
