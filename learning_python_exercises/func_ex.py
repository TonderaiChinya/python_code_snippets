def adder(*args):
	if type(args) is int:
		sum = 0
		for x in args:
			sum += x
	return sum
	elif type(args) is str:
		list = []
		for item in args:
			list.append(item)
	return list
	else:
		pass

	

x1 =  adder(5)
x2 =  adder('hi', '!')
x3 =  adder(5.4, 6.9)

print(x1)