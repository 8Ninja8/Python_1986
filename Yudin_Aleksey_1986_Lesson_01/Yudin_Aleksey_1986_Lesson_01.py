print("Задача_1")
duration = int(input("Введите продолжительность,сек:"))

# минута
one_minute = 60
# час
one_hour = 3600
# день
one_day = 86400


if duration < one_minute:
    print(f"{duration} сек.")

elif one_minute <= duration < one_hour:
    total_minutes = duration // one_minute
    total_seconds = duration % one_minute
    print(f"{total_minutes} мин. {total_seconds} сек.")

elif one_hour <= duration < one_day:
    total_hours = duration // one_hour
    duration = duration % one_hour
    total_minutes = duration // one_minute
    total_seconds = duration % one_minute
    print(f"{total_hours} ч. {total_minutes} мин. {total_seconds} сек.")

elif one_day <= duration:
    total_days = duration // one_day
    duration = duration % one_day
    total_hours = duration // one_hour
    duration = duration % one_hour
    total_minutes = duration // one_minute
    total_seconds = duration % one_minute
    print(f"{total_days} д. {total_hours} ч. {total_minutes} мин. {total_seconds} сек.")

