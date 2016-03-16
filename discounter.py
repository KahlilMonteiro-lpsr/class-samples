# find out the price from user
print("what is the price?")
price = int(input())


# calculate discount price
discount_price = .9 * price

# if user gets a discount, tell them.
# if not, tell them.
if price > 1000:
	print("your price is " + str(discount_price))
else:
	print("sorry you don't get the discount")
