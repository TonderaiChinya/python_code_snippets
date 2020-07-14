names = ['Kamilah', 'Kaylah', 'Thelma', 'Tonderai']
names_2 = ['Kundai', 'Mazvita', 'tonderai']

users = []
for name in names:
    users.append(name.lower())
for name in names_2:
    user = name.lower()
    if user in users:
        print('Username ' + user + ' already exists.')
    else:
        users.append(user)

admin = 'tonderai'
if users:
    for name in sorted(users, reverse=True):
        if name == admin:
            print('Hello admin ' + name.title() + ' Chinya! How are you today?')
        else:
            print('Hello ' + name.title() + ' Chinya! Welcome back.')
else:
    print('There are no active users at the moment.')
