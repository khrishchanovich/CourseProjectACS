# Сбор информации о процессоре

import psutil
import multiprocessing


def get_cpu_info():
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()

    cpu_frequency = f'{cpu_freq.current:.2f} MHz' if cpu_freq.current else 'N/A'

    num_active_cores = multiprocessing.cpu_count()

    return cpu_percent, cpu_frequency, num_active_cores


cpu_percent, cpu_frequency, num_active_cores = get_cpu_info()
print(f'Загрузка процессора: {cpu_percent}%')
print(f'Тактовая частота процессора: {cpu_frequency}')
print(f'Количество активных ядер: {num_active_cores}')
