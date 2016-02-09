print("Welcome to the haiku generator")
print("provide the first line of your haiku:")
firstline = raw_input()

print("provide the second line of your haiku:")
secondline = raw_input()

print("provide the third line of your haiku:")
thirdline = raw_input()

print("what file would you like to write your haiku to?")
filename = raw_input()

my_file = open(filename, 'w')

my_file.write(str(firstline) + '\n')
my_file.write((secondline) + '\n')
my_file.write((thirdline) + '\n')

my_file.close()
