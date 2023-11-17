# Сбор информации об оперативной памяти

import psutil


def get_memory_info():
    memory = psutil.virtual_memory()

    memory_percent = memory.percent
    available_memory = f'{memory.available / (1024 ** 2):.2f} MB'
    total_memory = f'{memory.total / (1024 ** 2):.2f} MB'

    return memory_percent, available_memory, total_memory

memory_percent, available_memory, total_memory = get_memory_info()
print(f'Загрузка оперативной памяти: {memory_percent}%')
print(f'Доступно: {available_memory}')
print(f'Общее: {total_memory}')