name = ''
count = 0
while name != 'левон':
    name = input('Введите имя Левон или Александра: ').lower()
    count += 1
    if name == 'александра':
        number_1 = count
    elif name == 'левон':
        number_2 = count
print(number_2 - number_1 - 1)
