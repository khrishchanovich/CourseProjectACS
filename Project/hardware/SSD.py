# Сбор информации о жестком диске

import psutil


class SSD:
    def __init__(self):
        self.partitions = None
        self.disk_usage = None
        self.disk_percent = 0
        self.available_space = 'N/A'
        self.total_space = 'N/A'

        self.get_partitions()
        self.get_disk()

    def get_partitions(self):
        self.partitions = psutil.disk_partitions()

        return self.partitions

    def get_disk(self):
        for partition in self.partitions:
            if 'Windows' in partition.fstype:
                continue

            self.disk_usage = psutil.disk_usage(partition.mountpoint)

        return self.disk_usage

    def get_percent(self):
        self.disk_percent = self.disk_usage.percent

        return self.disk_percent

    def get_available_space(self):
        self.available_space = f'{self.disk_usage.free / (1024 ** 3):.2f} GB'

        return self.available_space

    def get_total_space(self):
        self.total_space = f'{self.disk_usage.total / (1024 ** 3):.2f} GB'

        return self.total_space

    def display_info(self):
        print(f'Загрузка жесткого диска: {self.get_percent()}%')
        print(f'Доступно: {self.get_available_space()}')
        print(f'Общее: {self.get_total_space()}')


disk_info = SSD()

disk_info.display_info()
