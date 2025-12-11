num = int(input('Введите число '))
num_3 = num
num_last_digit = num
num_even_digit = num
num_products_over_7 = num
num_sum_over_5 = num
num_0_5 = num

count_3 = 0
while num_3 > 10:
    new_last_digit = num_3 % 10
    if new_last_digit == 3:
        count_3 += 1
    num_3 //= 10
print('Количество цифры 3 в числе: ',count_3)

last_digit = num_last_digit % 10
count_last_digit = 0
while num_last_digit > 10:
    new_last_digit = num_last_digit % 10
    if last_digit == new_last_digit:
        count_last_digit += 1
    num_last_digit //= 10
print('Последнее цифра встречается: ', count_last_digit, 'раз')

count_even_digit = 0
while num_even_digit > 10:
    new_last_digit = num_even_digit % 10
    if new_last_digit % 2 == 0:
        count_even_digit += 1
    num_even_digit //= 10
print("Колличество четных цифр в числе равно:", count_even_digit)

count_sum_digit_over_5 = 0
while num_sum_over_5 > 10:
    new_last_digit = num_sum_over_5 % 10
    if new_last_digit > 5:
        count_sum_digit_over_5 += new_last_digit
    num_sum_over_5 //= 10
print('Сумма цифр больших 5 равна: ', count_sum_digit_over_5)

count_product_digit_over_7 = 1
while num_products_over_7 > 10:
    new_last_digit = num_products_over_7 % 10
    if new_last_digit > 7:
        count_product_digit_over_7 *= new_last_digit
    num_products_over_7 //= 10
print('Произведение цифр больших 7: ',count_product_digit_over_7)

count_digit_5_0 = 0
while num_0_5 > 10:
    new_last_digit = num_0_5 % 10
    if new_last_digit == 5 or new_last_digit == 0:
        count_digit_5_0 += 1
    num_0_5 //= 10
print('Цифры 0 и 5 встречаются ', count_digit_5_0, 'раз')
