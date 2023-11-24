# Сбор информации о процессоре

import platform
import psutil
import wmi


class CPU:
    def __init__(self):
        self.cpu_name = 'N/A'
        self.cpu_percent = 0
        self.cpu_frequencies = []
        self.num_active_cores = 0
        self.temperature = 0
        self.power = 0

    def get_name(self):
        self.cpu_name = platform.processor()
        return self.cpu_name

    def get_percent(self):
        self.cpu_percent = psutil.cpu_percent(interval=1)
        return self.cpu_percent

    def get_cpu_frequency(self):
        try:
            w = wmi.WMI(namespace="root/OpenHardwareMonitor")
            sensors = w.Sensor()

            self.cpu_frequencies = []
            for core_num in range(1, self.get_num_active_cores() + 1):
                core_name = f'CPU Core #{core_num}'
                for sensor in sensors:
                    if sensor.SensorType == 'Clock' and sensor.Name == core_name:
                        self.cpu_frequencies.append(sensor.Value)
        except Exception as error:
            print(f'Error: {error}')

    def get_frequency(self):
        self.get_cpu_frequency()
        if self.cpu_frequencies:
            total_frequency = sum(self.cpu_frequencies)
            average_frequency = total_frequency / len(self.cpu_frequencies)
            return f'{average_frequency:.2f} MHz'
        else:
            return 'Информация не доступна'

    def get_num_active_cores(self):
        self.num_active_cores = psutil.cpu_count(logical=True)
        if self.num_active_cores:
            return self.num_active_cores
        else:
            return 'Информация не доступна'

    @staticmethod
    def get_cpu_temperature():
        try:
            w = wmi.WMI(namespace="root/OpenHardwareMonitor")
            sensors = w.Sensor()

            for sensor in sensors:
                if sensor.SensorType == 'Temperature' and sensor.Name == 'CPU Package':
                    return sensor.Value

        except Exception as error:
            print(f'Error: {error}')

    def get_temperature(self):
        self.temperature = self.get_cpu_temperature()

        if self.temperature is not None:
            return f'{self.temperature}°C'
        else:
            return 'Информация не доступна'

    @staticmethod
    def get_cpu_power():
        try:
            w = wmi.WMI(namespace="root/OpenHardwareMonitor")
            sensors = w.Sensor()

            for sensor in sensors:
                if sensor.SensorType == 'Power' and sensor.Name == 'CPU Package':
                    return sensor.Value

        except Exception as error:
            print(f'Error: {error}')

    def get_power(self):
        self.power = self.get_cpu_power()

        if self.power is not None:
            return f'{self.power:.2f} W'
        else:
            return 'Информация не доступна'

    def display_info(self):
        print(f'Название процессора: {self.get_name()}')
        print(f'Загрузка процессора: {self.get_percent()}%')
        print(f'Частоты процессора: {self.get_frequency()}')
        print(f'Количество активных ядер: {self.get_num_active_cores()}')
        print(f'Температуры: {self.get_temperature()}')
        print(f'Напряжения: {self.get_power()}')


cpu = CPU()
cpu.display_info()
