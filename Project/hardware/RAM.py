# Сбор информации об оперативной памяти

import psutil


class RAM:
    def __init__(self):
        self.memory = None
        self.memory_percent = 0
        self.available_memory = 0
        self.total_memory = 0

        self.get_memory()

    def get_memory(self):
        self.memory = psutil.virtual_memory()

        return self.memory

    def get_memory_percent(self):
        self.memory_percent = self.memory.percent

        return self.memory_percent

    def get_available_memory(self):
        self.available_memory = f'{self.memory.available / (1024 ** 2):.2f} MB'

        return self.available_memory

    def get_total_memory(self):
        self.total_memory = f'{self.memory.total / (1024 ** 2):.2f} MB'

        return self.total_memory

    def display_info(self):
        print(f'Загрузка оперативной памяти: {self.get_memory_percent()}%')
        print(f'Доступно: {self.get_available_memory()}')
        print(f'Общее: {self.get_total_memory()}')
