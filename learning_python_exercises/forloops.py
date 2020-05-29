characters = ['A', 'B', 'C','&', '+', '?']
sum = 0
for  char in characters:
	character = ord(char)
	print (char + ' - ' + str(character))	
	sum += character
print (map(ord, characters))
print (sum)