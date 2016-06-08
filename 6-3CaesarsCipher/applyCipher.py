# applyCipher.py
# A program to encrypt/decrypt user text
# using Caesars Cipher
#
# Author: rc.monteiro.kahlil [at] leadps.org
import string
#  makes a mapping of alphabet to decoded alphabet
# arguments: key
# returns: dictionary of mapped letters
def createDictionary(key):
	alphabet = list(string.ascii_lowercase)
	alphabet1 = {}
	num = 0
	for n in alphabet:
		alphabet1[n] = (alphabet[(key + num) % 26])
		num += 1
	return alphabet1

# receive: user's encrypted message
# arguments: none
# return: encoded messge
def getMessage(message):
	return message

# for each letter in the message, decodes and record
# arguments:encoded message, dictionary
# returns decoded message
def decodedMessage(message, dictionary):
	code = ''
	for m in message:
		newCode = dictionary[m]
		code = code + newCode
	return code

# outputs the message to the terminal 
# arguments: decoded message
# returns: none
def printMessage(decodemessage):
	print(decodemessage)

# execution starts here

# ask user for key
print("What key would you like to use decode?(1-25)")
key = int(raw_input())
print("What message would you like to decode?")
message = raw_input()
print("Here's the decoding of your message:")

dictionary = createDictionary(key)
encodeMessage = getMessage(message)
decodeMessage = decodedMessage(encodeMessage, dictionary)
printMessage(decodeMessage)
