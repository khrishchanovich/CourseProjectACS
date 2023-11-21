import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer
from Project.hardware.CPU import CPU  # Замените your_cpu_module на имя файла, в котором находится ваш класс


class CPUInfoWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Информация о процессоре')
        self.setGeometry(100, 100, 400, 200)

        self.cpu = CPU()  # Создаем экземпляр вашего класса

        self.cpu_percent_label = QLabel('Загрузка процессора: N/A')
        self.cpu_freq_label = QLabel('Тактовая частота процессора: N/A')
        self.num_active_cores_label = QLabel('Количество активных ядер: N/A')
        self.temperature = QLabel('Температура: N/A')

        layout = QVBoxLayout()
        layout.addWidget(self.cpu_percent_label)
        layout.addWidget(self.cpu_freq_label)
        layout.addWidget(self.num_active_cores_label)
        layout.addWidget(self.temperature)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cpu_info)
        self.timer.start(1000)  # Обновление каждую секунду

        self.update_cpu_info()

    def update_cpu_info(self):
        cpu_percent, cpu_frequency, num_active_cores, temperature = self.get_cpu_info()

        self.cpu_percent_label.setText(f'Загрузка процессора: {cpu_percent}%')
        self.cpu_freq_label.setText(f'Тактовая частота процессора: {cpu_frequency}')
        self.num_active_cores_label.setText(f'Количество активных ядер: {num_active_cores}')
        self.num_active_cores_label.setText(f'Температура: {temperature}')

    def get_cpu_info(self):
        cpu_percent = self.cpu.get_percent()
        cpu_frequency = self.cpu.get_frequency()
        num_active_cores = self.cpu.get_num_active_cores()
        temperature = self.cpu.get_temperature()

        return cpu_percent, cpu_frequency, num_active_cores, temperature


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cpu_info_window = CPUInfoWindow()
    cpu_info_window.show()
    sys.exit(app.exec_())
