# Сбор информации о графическом процессоре

import GPUtil


class GPU:
    def __init__(self):
        self.gpu_name = None
        self.gpu_load = 0.0
        self.gpu_memory_total = 'N/A'
        self.gpu_memory_used = 'N/A'
        self.gpu_memory_free = 'N/A'
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

    def display_info(self):
        print(f'Графический процессор: {self.get_name()}')
        print(f'Загрузка: {self.get_load():.2f}%')
        print(f'Использовано памяти: {self.get_memory_used()} / {self.get_memory_total()}')
        print(f'Свободно памяти: {self.get_memory_free()}')
