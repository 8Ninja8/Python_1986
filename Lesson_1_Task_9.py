number_1, number_2, number_3 = [x for x in input('Введите три числа, через пробел: ').split()]

if number_2 < number_1 < number_3 or number_3 < number_1 < number_2:
    print(f'Среднее: {number_1}')
elif number_1 < number_2 < number_3 or number_3 < number_2 < number_1:
    print(f'Среднее: {number_2}')
else:
    print(f'Среднее: {number_3}')
