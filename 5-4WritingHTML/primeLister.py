# takes myNum an integer
# returns true if myNum is prime
# returns false if myNum is composite
allnums = range(1, 10000)
def isPrime(myNum):
	for n in range(2, myNum):
		if myNum % n == 0:
			return False
	return True 

myFile = open("prime.txt", "w")
for n in allnums:
	if isPrime(n):
		myFile.write(str(n) + "\n")

myFile.close()
