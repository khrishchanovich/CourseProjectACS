import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from Project.hardware.CPU import CPU


class CPUMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.cpu = CPU()
        self.init_ui()

        # Инициализируем таймер, чтобы обновлять данные каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # 1000 миллисекунд = 1 секунда

    def init_ui(self):
        layout = QVBoxLayout()

        # Добавим метки с информацией о процессоре
        self.label_name = QLabel(f'Название процессора: {self.cpu.get_name()}')
        layout.addWidget(self.label_name)

        self.label_percent = QLabel(f'Загрузка процессора: {self.cpu.get_percent()}%')
        layout.addWidget(self.label_percent)

        self.label_frequency = QLabel(f'Тактовая частота процессора: {self.cpu.get_frequency()}')
        layout.addWidget(self.label_frequency)

        self.label_cores = QLabel(f'Количество активных ядер: {self.cpu.get_num_active_cores()}')
        layout.addWidget(self.label_cores)

        self.label_temperature = QLabel(f'Температура: {self.cpu.get_temperature()}')
        layout.addWidget(self.label_temperature)

        self.label_power = QLabel(f'Напряжение: {self.cpu.get_power()}')
        layout.addWidget(self.label_power)

        self.setLayout(layout)

        self.setWindowTitle('CPUMonitorApp')
        self.setGeometry(100, 100, 400, 300)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 14px;')
        return label

    def update_data(self):
        # Обновляем данные каждую секунду
        self.label_name.setText(f'Название процессора: {self.cpu.get_name()}')
        self.label_percent.setText(f'Загрузка процессора: {self.cpu.get_percent()}%')
        self.label_frequency.setText(f'Тактовая частота процессора: {self.cpu.get_frequency()}')
        self.label_cores.setText(f'Количество активных ядер: {self.cpu.get_num_active_cores()}')
        self.label_temperature.setText(f'Температура: {self.cpu.get_temperature()}')
        self.label_power.setText(f'Напряжение: {self.cpu.get_power()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cpu_monitor_app = CPUMonitorApp()
    cpu_monitor_app.show()
    sys.exit(app.exec_())
