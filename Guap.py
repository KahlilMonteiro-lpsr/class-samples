# for every roll of paper towels, you get a $0.25 rebate
# but if you buy more than 10 rolls, you get a $0.35 rebate for each one

# but if you're a value club member,
# you get a $2.00 rebate for buying at least one roll


# find out the user is a value club member
print("are you a value club member? respond yes or no.")
club = raw_input()

# find out how many rolls of paper towels user bought
print("how many rolls of paper towels did you buy?")
rolls = int(raw_input())


# if they're in the club, they get an extra $2
if club == "yes":
	print("in the club")
	if rolls > 10:
	   rebate = rolls * .35 + 2
	else:
           rebate = rolls * .25 + 2
  
else:
	# do this now:
	if rolls < 10:
		print("not in the club")

# print rebate
print("your rebate is $" + str(rebate))
