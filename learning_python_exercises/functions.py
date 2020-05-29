def echo(message):
	print(message)

def indirect(func, arg):
	func(arg)

schedule =  [(echo, 'welcome to comptech'), (echo, 'thank you for signing in')]

for (func, arg) in schedule:
	apply(func, (arg,))