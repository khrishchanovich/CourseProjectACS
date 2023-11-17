import psutil
import datetime


def get_battery_info():
    try:
        battery = psutil.sensors_battery()
        percent = battery.percent
        power_plugged = battery.power_plugged
        secs_left = battery.secsleft

        return percent, power_plugged, secs_left
    except Exception as e:
        print(f'Ошибка при пролучении информации о батарее: {e}')


def calculate_time_left(secs_left):
    if secs_left is not None:
        hours, remainder = divmod(secs_left, 3600)
        minutes, seconds = divmod(remainder, 60)

        time_left = f'{int(hours)}:{int(minutes)}:{int(seconds)}'
        return time_left
    else:
        return 'Недоступно'


battery_info = get_battery_info()

if battery_info:
    percent, power_plugged, secs_left = battery_info
    time_left = calculate_time_left(secs_left)

    print(f'Уровень заряда батареи: {percent}%')
    print(f'Подключено к сети: {"Да" if power_plugged else "Нет"}')
    print(f'Прогноз времеги до разрядки: {time_left}')