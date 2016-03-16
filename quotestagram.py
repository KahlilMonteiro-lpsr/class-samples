# quotestagram.py
# the best quote-sharing service

class Quote(object):

	def __init__(self, quotetext, user_posted, location, num_likes):

		self.quote_text = quotetext
		self.user_posted = user_posted
		self.location = location
		self.num_likes = num_likes

	# adds one to the 'like' count
	def like(self):
		self.num_likes = self.num_likes + 1
	
	# takes one away from the 'like' count
	def un_like(self):
		self.num_likes = self.num_likes - 1

	# prints the full quote
	def show_quote(self):
		print("U: " + self.user_posted)
		print("L: " + self.location)
		print("Q: " + self.quote_text)
		print("Likes: " + str(self.num_likes))

# add some quotes
x = Quote("Nothing with shawn.", "kevin_is_kool", "San Francisco", 0)
y = Quote("work hard play hard.", "adam_chapman", "chicago", 11) 
z = Quote("ball is life.", "kahlilgotskills", "richmond", 25)

# print our quotes
z.show_quote()
  
# put our Quotes into a list
my_quotes = []
my_quotes.append(x)
my_quotes.append(y)
my_quotes.append(z)
user_quote = "Hello. How are you?"
speaker = "Adele"
location = "london"

my_quotes.append(Quote(user_quote, speaker, location, 0))

# call our show_quote function for all of our Quote objects
for q in my_quotes:
	q.show_quote()


