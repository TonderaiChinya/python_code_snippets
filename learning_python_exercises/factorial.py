def factorial(x):
	if x == 0:
		return 1
	return x * factorial(x - 1)


x = int(input('Enter your number: '))
print(factorial(x))
