import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtCore import QTimer
from Project.battery.battery import Battery


# Создаем класс для отображения информации о батарее в интерфейсе
class BatteryMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.battery = Battery()
        self.init_ui()

        # Инициализируем таймер, чтобы обновлять данные каждую секунду
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(1000)  # 1000 миллисекунд = 1 секунда

    def init_ui(self):
        layout = QVBoxLayout()

        # Добавляем метку с уровнем заряда
        self.label_percent = QLabel(f'Уровень заряда батареи: {self.battery.get_percent()}%')
        layout.addWidget(self.label_percent)

        # Добавляем полосу прогресса для отображения уровня заряда
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(self.battery.get_percent())
        layout.addWidget(self.progress_bar)

        # Добавляем метку с информацией о подключении к сети
        self.label_power_plugged = QLabel(f'Подключено к сети: {"Да" if self.battery.get_power_plugged() else "Нет"}')
        layout.addWidget(self.label_power_plugged)

        # Добавляем метку с временем до разрядки
        self.label_time_left = QLabel(f'Прогноз времени до разрядки: {self.battery.get_time_left()}')
        layout.addWidget(self.label_time_left)

        self.setLayout(layout)

        self.setWindowTitle('BatteryMonitorApp')
        self.setGeometry(100, 100, 400, 300)

    def update_data(self):
        self.battery.update_data()
        self.label_percent.setText(f'Уровень заряда батареи: {self.battery.get_percent()}%')
        self.progress_bar.setValue(self.battery.get_percent())
        self.label_power_plugged.setText(f'Подключено к сети: {"Да" if self.battery.get_power_plugged() else "Нет"}')
        self.label_time_left.setText(f'Прогноз времени до разрядки: {self.battery.get_time_left()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    battery_monitor_app = BatteryMonitorApp()
    battery_monitor_app.show()
    sys.exit(app.exec_())
