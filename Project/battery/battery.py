from datetime import timedelta

import psutil


class Battery:
    def __init__(self):
        self.battery = None
        self.percent = 0
        self.power_plugged = ''
        self.time_left = ''

        self.get_battery()

    def update_data(self):
        self.get_battery()
        self.get_time_left()

    def get_battery(self):
        try:
            self.battery = psutil.sensors_battery()

            return self.battery
        except Exception as error:
            print(f'Отсутствует батарея: {error}')

    def get_percent(self):
        if self.battery is not None:
            self.percent = self.battery.percent

            return self.percent
        else:
            return 'Нет информации о батарее'

    def get_power_plugged(self):
        if self.battery is not None:
            self.power_plugged = self.battery.power_plugged

            return self.power_plugged
        else:
            return 'Нет информации о батарее'

    def get_time_left(self):
        power = self.get_power_plugged()
        if self.battery is not None:
            if not power:
                time_left = timedelta(seconds=self.battery.secsleft) if self.battery.secsleft is not None else None

                if time_left is not None:
                    hours, remainder = divmod(time_left.seconds, 3600)
                    minutes, seconds = divmod(remainder, 60)

                    self.time_left = f'{int(hours)}:{int(minutes)}:{int(seconds)}'
                    return self.time_left
                else:
                    return 'Недоступно'
            else:
                return 'Устройство подключено к сети'
        else:
            return 'Нет информации о батарее'

    def display_info(self):
        print(f'Уровень заряда батареи: {self.get_percent()}%')
        print(f'Подключено к сети: {"Да" if self.get_power_plugged() else "Нет"}')
        print(f'Прогноз времени до разрядки: {self.get_time_left()}')


battery_info = Battery()
battery_info.display_info()
