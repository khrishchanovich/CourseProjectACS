import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from Project.hardware.GPU import GPU


class GPUMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.gpu = GPU()
        self.init_ui()

        # Инициализируем таймер, чтобы обновлять данные каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # 1000 миллисекунд = 1 секунда

    def init_ui(self):
        layout = QVBoxLayout()

        # Добавим метки с информацией о процессоре
        self.label_name = QLabel(f'Название процессора: {self.gpu.get_name()}')
        layout.addWidget(self.label_name)

        self.label_percent = QLabel(f'Загрузка процессора: {self.gpu.get_load()}%')
        layout.addWidget(self.label_percent)

        self.label_frequency = QLabel(f'Тактовая частота процессора: {self.gpu.get_clock()}')
        layout.addWidget(self.label_frequency)

        self.label_temperature = QLabel(f'Температура: {self.gpu.get_temperature()}')
        layout.addWidget(self.label_temperature)

        self.label_power = QLabel(f'Напряжение: {self.gpu.get_power()}')
        layout.addWidget(self.label_power)

        self.label_memory_used = QLabel(f'Использовано памяти: {self.gpu.get_memory_used()} / {self.gpu.get_memory_total()}')
        layout.addWidget(self.label_memory_used)

        self.label_memory_free = QLabel(f'Свободно памяти: {self.gpu.get_memory_free()}')
        layout.addWidget(self.label_memory_free)

        self.setLayout(layout)

        self.setWindowTitle('GPUMonitorApp')
        self.setGeometry(100, 100, 400, 300)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 14px;')
        return label

    def update_data(self):
        # Обновляем данные каждую секунду
        self.label_name.setText(f'Название процессора: {self.gpu.get_name()}')
        self.label_percent.setText(f'Загрузка процессора: {self.gpu.get_load()}%')
        self.label_frequency.setText(f'Тактовая частота процессора: {self.gpu.get_clock()}')
        self.label_temperature.setText(f'Температура: {self.gpu.get_temperature()}')
        self.label_power.setText(f'Напряжение: {self.gpu.get_power()}')
        self.label_memory_used.setText(f'Использовано памяти: {self.gpu.get_memory_used()} / {self.gpu.get_memory_total()}')
        self.label_memory_free.setText(f'Свободно памяти: {self.gpu.get_memory_free()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gpu_monitor_app = GPUMonitorApp()
    gpu_monitor_app.show()
    sys.exit(app.exec_())
