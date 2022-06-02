letter_number = int(input('Введите порядковый номер буквы в алфавите: '))

abc_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
if letter_number <= len(abc_list):
    print(f'Буква под номером {letter_number}: {abc_list[letter_number - 1]}')
else:
    print(
      f'В алфавите меньше букв ({len(abc_list)})'
    )