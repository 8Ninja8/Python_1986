import random

a, b = map(int, input('Задайте диапазон для целых чисел через пробел: ').split())
c = round(random.random() * (b - a) + a)
print(c)

a, b = map(int, input('Задайте диапазон для вещественных чисел через пробел: ').split())
c = random.random() * (b - a) + a
print(c)

lettr_one, lettr_two = input('Задайте диапазон латинских букв через пробел: ').split()
lettr_three = chr(random.randint(ord(lettr_one), ord(lettr_two)))
print(lettr_three)