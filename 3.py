money = int(input('Введите цену за услугу ведьмака '))
coin_1 = 0
coin_5 = 0
coin_10 = 0
coin_25 = 0
while money > 0:
    if money - 25 >= 0:
        money -= 25
        coin_25 += 1
    elif money - 10 >= 0:
        money -= 10
        coin_10 += 1
    elif money - 5 >= 0:
        money -= 5
        coin_5 += 1
    elif money - 1 >= 0:
        money -= 1
        coin_1 += 1
print(f'''Вы должны заплатить ведьмаку:
{coin_25} монет по 25
{coin_10} монет по 10
{coin_5} монет по 5
{coin_1} монет по 1''')
