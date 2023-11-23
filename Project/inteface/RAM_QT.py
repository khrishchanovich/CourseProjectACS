import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer
from Project.hardware.RAM import RAM


class RAMMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.ram = RAM()
        self.init_ui()

        # Инициализируем таймер, чтобы обновлять данные каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # 1000 миллисекунд = 1 секунда

    def init_ui(self):
        layout = QVBoxLayout()

        # Добавим метки с информацией о процессоре
        self.label_memory_percent = QLabel(f'Загрузка оперативной памяти: {self.ram.get_memory_percent()}%')
        layout.addWidget(self.label_memory_percent)

        self.label_available_memory = QLabel(f'Доступно: {self.ram.get_available_memory()}')
        layout.addWidget(self.label_available_memory)

        self.label_total_memory = QLabel(f'Общее: {self.ram.get_total_memory()}')
        layout.addWidget(self.label_total_memory)

        self.setLayout(layout)

        self.setWindowTitle('RAMMonitorApp')
        self.setGeometry(100, 100, 400, 300)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 14px;')
        return label

    def update_data(self):
        # Обновляем данные каждую секунду
        self.ram.update_data()
        self.label_memory_percent.setText(f'Загрузка оперативной памяти: {self.ram.get_memory_percent()}%')
        self.label_available_memory.setText(f'Доступно: {self.ram.get_available_memory()}')
        self.label_total_memory.setText(f'Общее: {self.ram.get_total_memory()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ram_monitor_app = RAMMonitorApp()
    ram_monitor_app.show()
    sys.exit(app.exec_())
