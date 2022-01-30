 # Урок 2
 # "Задание_1"
print(f'Тип выражения 15 * 3 {type(15 * 3)}')
print(f'Тип выражения 15 / 3 {type(15 / 3)}')
print(f'Тип выражения 15 // 2 {type(15 // 2)}')
print(f'Тип выражения 15 ** 2 {type(15 ** 2)}')


# "Задание_2"
def get_sign(x):
    if x[0] in '+-':
        return x[0]
weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(weather):
    sign = get_sign(weather[i])
    if weather[i].isdigit() or (sign and weather[i][1:].isdigit()):
        if sign:
            weather[i] = sign + weather[i][1:].zfill(2)
        else:
            weather[i] = weather[i].zfill(2)

        weather.insert(i, '')
        i += 2

    i += 1
print(weather)

weather = ['в', '5', 'часов', '17', 'минут','температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate (weather):
    if s.isdigit():
        weather[i] = f'"{int(s):02d}"'
    elif s[1:].isdigit():
        weather[i] = f'"{s[0]}{int(s[1:]):02d}"'
    print(weather[i], end=' ')
print('\n', weather)
#
# # "Задание_4"
first_list = ['инженер-конструктор Игорь',
              'главный бухгалтер МАРИНА',
              'токарь высшего разряда нИКОЛАЙ',
              'директор аэлита']

for elmnt in first_list:
    first_name = elmnt.split()[-1].capitalize()
    print(f'Привет, {first_name}!')

# Задание_5
price = [2.30, 150.30, 87.25, 50.47, 111.99, 5.55, 32.32, 99.99, 0.55, 89.90]
# 5.1
res = ''
for p in price:
    res += f'{int(p)} руб. {int(p * 100 % 100):02} коп., '
    # print(f'{int(p)} руб. {int(p * 100 % 100):02} коп.', end=', ')
print(res[:-2])

# 5.2
print('\n', f'Цены: {price} id списка: {id(price)}')
price.sort()
print('\n', f'Цены по возрастанию: {price} id списка: {id(price)}')

# 5.3
new_price = sorted(price, reverse=True)
print('\n', f'Цены по убыванию: {new_price} id списка: {id(new_price)}')