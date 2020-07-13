names = ['Kamilah', 'Kaylah', 'Thelma', 'Tonderai']
for name in names:
    print('Hello ' + name + '! How are you today?')

names_2 = ['Kundai', 'Mazvita', 'Chinya']
for name in names_2:
    names.append(name)

names.insert(0, 'Family Names')
print(sorted(names, reverse=True))
