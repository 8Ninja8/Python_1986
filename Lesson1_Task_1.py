numb = input('Введите трехзначное число:\n')

if numb.isdigit():
    if len(numb) != 3:
        print('Нужно ввести ТРЕХзначное число.')
    else:
        mult = 1
        summ = 0
        for i in numb:
            summ += int(i)
            mult *= int(i)
        print(f'Сумма цифр цисла {numb} = {summ}, произведение = {mult}')
else:
    print('Введите ЧИСЛО согласно условию')