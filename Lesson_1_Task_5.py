chars = 'abcdefghijklmnopqrstuvwxyz'

char_range = input('Задайте диапазон букв латинского алфавита через пробел : ').split(' ')
print(char_range)
a = chars.index(char_range[0]) + 1
b = chars.index(char_range[1]) + 1


c = b - a

print('Первая буква: {} - находится на {} позиции,\n\
Вторая буква {} - находится на {} позиции.\n\
Расстояние между ними {}'.format(char_range[0], a, char_range[1], b, c))