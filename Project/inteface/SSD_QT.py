import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from Project.hardware.SSD import SSD
import psutil


class SSDMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

        # Инициализируем таймер, чтобы обновлять данные каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # 1000 миллисекунд = 1 секунда

    def init_ui(self):
        layout = QVBoxLayout()

        # Получаем информацию о всех дисках
        partitions = psutil.disk_partitions()

        # Создаем экземпляр класса SSD для каждого диска
        for partition in partitions:
            disk_info = SSD(partition)

            # Добавляем метки с информацией о каждом диске
            label_device = QLabel(f'Диск {disk_info.partition.device}:')
            layout.addWidget(label_device)

            label_percent = QLabel(f'Загрузка жесткого диска: {disk_info.get_percent()}%')
            layout.addWidget(label_percent)

            label_available_space = QLabel(f'Доступно: {disk_info.get_available_space()}')
            layout.addWidget(label_available_space)

            label_total_space = QLabel(f'Общее: {disk_info.get_total_space()}')
            layout.addWidget(label_total_space)

            # Разделитель между дисками
            layout.addWidget(QLabel('---------------------------------'))

        self.setLayout(layout)

        self.setWindowTitle('DiskMonitorApp')
        self.setGeometry(100, 100, 400, 300)

    def update_data(self):
        # Обновляем данные каждую секунду
        self.init_ui()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    disk_monitor_app = SSDMonitorApp()
    disk_monitor_app.show()
    sys.exit(app.exec_())
