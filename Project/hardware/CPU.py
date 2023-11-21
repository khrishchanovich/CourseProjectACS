# Сбор информации о процессоре

import psutil
import multiprocessing
import wmi


class CPU:
    def __init__(self):
        self.cpu_percent = 0
        self.cpu_frequency = 'N/A'
        self.num_active_cores = 0
        self.temperature = 'N/A'

    def get_percent(self):
        self.cpu_percent = psutil.cpu_percent(interval=1)

        return self.cpu_percent

    def get_frequency(self):
        cpu_freq = psutil.cpu_freq()
        self.cpu_frequency = f'{cpu_freq.current:.2f} MHz' if cpu_freq.current else 'N/A'

        return self.cpu_frequency

    def get_num_active_cores(self):
        self.num_active_cores = multiprocessing.cpu_count()

        return self.num_active_cores

    @staticmethod
    def get_cpu_temperature():
        try:
            w = wmi.WMI(namespace="root/OpenHardwareMonitor")
            sensors = w.Sensor()

            for sensor in sensors:
                if sensor.SensorType == 'Temperature' and sensor.Name == 'CPU Package':
                    return sensor.Value

        except Exception as error:
            print(f'Error: { error }')

    def get_temperature(self):
        self.temperature = self.get_cpu_temperature()

        if self.temperature is not None:
            return f'{self.temperature}°C'
        else:
            print('Информация о температуре не доступна')

    def display_info(self):
        print(f'Загрузка процессора: {self.get_percent()}%')
        print(f'Тактовая частота процессора: {self.get_frequency()}')
        print(f'Количество активных ядер: {self.get_num_active_cores()}')
        print(f'Температура: {self.get_temperature()}')

cpu = CPU()
cpu.display_info()