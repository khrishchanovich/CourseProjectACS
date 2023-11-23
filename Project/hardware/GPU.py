# Сбор информации о графическом процессоре

import GPUtil
import wmi


class GPU:
    def __init__(self):
        self.gpu_name = 'N/A'
        self.gpu_load = 'N/A'
        self.gpu_memory_total = 'N/A'
        self.gpu_memory_used = 'N/A'
        self.gpu_memory_free = 'N/A'
        self.clock = 'N/A'
        self.temperature = 0
        self.power = 0
        self.gpu = None

        self.get_gpu()

    def get_gpu(self):
        self.gpu = GPUtil.getGPUs()[0]

        return self.gpu

    def get_name(self):
        self.gpu_name = self.gpu.name

        return self.gpu_name

    def get_load(self):
        self.gpu_load = self.gpu.load * 100

        return self.gpu_load

    def get_memory_total(self):
        self.gpu_memory_total = f'{self.gpu.memoryTotal / 1024:.2f} GB'

        return self.gpu_memory_total

    def get_memory_used(self):
        self.gpu_memory_used = f'{self.gpu.memoryUsed / 1024:.2f} GB'

        return self.gpu_memory_used

    def get_memory_free(self):
        self.gpu_memory_free = f'{self.gpu.memoryFree / 1024:.2f} GB'

        return self.gpu_memory_free

    @staticmethod
    def get_clock_info():
        try:
            w = wmi.WMI(namespace="root/OpenHardwareMonitor")
            sensors = w.Sensor()

            for sensor in sensors:
                if sensor.SensorType == 'Clock' and sensor.Name == 'GPU Core':
                    return sensor.Value

        except Exception as error:
            print(f'Error: {error}')

    def get_clock(self):
        self.clock = self.get_clock_info()

        if self.clock is not None:
            return f'{self.clock:.2f}'
        else:
            return 'Информация не доступна'

    @staticmethod
    def get_gpu_temperature():
        try:
            w = wmi.WMI(namespace="root/OpenHardwareMonitor")
            sensors = w.Sensor()

            for sensor in sensors:
                if sensor.SensorType == 'Temperature' and sensor.Name == 'GPU Core':
                    return sensor.Value

        except Exception as error:
            print(f'Error: {error}')

    def get_temperature(self):
        self.temperature = self.get_gpu_temperature()

        if self.temperature is not None:
            return f'{self.temperature}°C'
        else:
            return 'Информация не доступна'

    @staticmethod
    def get_gpu_power():
        try:
            w = wmi.WMI(namespace="root/OpenHardwareMonitor")
            sensors = w.Sensor()

            for sensor in sensors:
                if sensor.SensorType == 'Power' and sensor.Name == 'GPU Power':
                    return sensor.Value

        except Exception as error:
            print(f'Error: {error}')

    def get_power(self):
        self.power = self.get_gpu_power()

        if self.power is not None:
            return f'{self.power:.2f} W'
        else:
            return 'Информация не доступна'

    def display_info(self):
        print(f'Графический процессор: {self.get_name()}')
        print(f'Загрузка процессора: {self.get_load():.2f}%')
        print(f'Тактовая частота процессора: {self.get_clock()} MHz')
        print(f'Температуры: {self.get_temperature()}')
        print(f'Напряжения: {self.get_power()}')
        print(f'Использовано памяти: {self.get_memory_used()} / {self.get_memory_total()}')
        print(f'Свободно памяти: {self.get_memory_free()}')


# gpu = GPU()
# gpu.display_info()
