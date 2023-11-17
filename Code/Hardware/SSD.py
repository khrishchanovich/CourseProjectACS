# Сбор информации о жестком диске

import psutil


def get_disk_info():
    partitions = psutil.disk_partitions()

    for partition in partitions:
        if 'Windows' in partition.fstype:
            continue

        disk_usage = psutil.disk_usage(partition.mountpoint)

        disk_percent = disk_usage.percent
        available_space = f'{disk_usage.free / (1024 ** 3):.2f} GB'
        total_space = f'{disk_usage.total / (1024 ** 3):.2f} GB'

        return disk_percent, available_space, total_space


disk_percent, available_space, total_space = get_disk_info()
print(f'Загрузка жесткого диска: {disk_percent}%')
print(f'Доступно: {available_space}')
print(f'Общее: {total_space}')