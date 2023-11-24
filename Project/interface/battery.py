# battery_monitor.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QProgressBar, QCheckBox, QComboBox
from PyQt5.QtCore import QTimer, Qt

from Project.battery.battery import Battery

class BatteryMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.battery = Battery()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)

        self.init_ui()

    def init_ui(self):
        self.setStyleSheet('''
            QWidget { background-color: #1E1E1E; color: white; font-size: 16px; }
            QLabel { border: 2px solid white; padding: 5px; }
            QProgressBar { 
                border: 2px solid white; 
                padding: 5px;
                text-align: center;
            }
            QProgressBar::chunk {
                background-color: #1E90FF;
            }
        ''')

        main_layout = QVBoxLayout(self)

        # Добавляем флажки для выбора отображаемых меток
        self.checkbox_labels = {
            'Уровень заряда': QCheckBox('Уровень заряда', checked=True),
            'Прогноз времени работы': QCheckBox('Прогноз времени работы', checked=True),
            'Подключено к сети': QCheckBox('Подключено к сети', checked=True),
        }

        for checkbox in self.checkbox_labels.values():
            checkbox.stateChanged.connect(self.update_visibility)
            main_layout.addWidget(checkbox)


        # Инициализируем выпадающий список для выбора времени обновления
        self.refresh_time_label = QLabel('Время обновления (секунды):')
        self.refresh_time_combobox = QComboBox()
        self.refresh_time_combobox.addItems(['1', '2', '5', '10', '30'])
        self.refresh_time_combobox.setCurrentIndex(0)
        self.refresh_time_combobox.currentIndexChanged.connect(self.update_refresh_time)
        main_layout.addWidget(self.refresh_time_label)
        main_layout.addWidget(self.refresh_time_combobox)

        # Добавляем виджеты монитора батареи
        self.label_percent = QLabel(f'Уровень заряда батареи: {self.battery.get_percent()}%')
        main_layout.addWidget(self.label_percent)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(self.battery.get_percent())
        self.progress_bar.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.progress_bar)

        self.label_power_plugged = QLabel(f'Подключено к сети: {"Да" if self.battery.get_power_plugged() else "Нет"}')
        main_layout.addWidget(self.label_power_plugged)

        self.label_time_left = QLabel(f'Прогноз времени работы: {self.battery.get_time_left()}')
        main_layout.addWidget(self.label_time_left)

        self.setLayout(main_layout)
        self.setWindowTitle('BatteryMonitorApp')
        self.setGeometry(100, 100, 400, 300)

        self.timer.start(1000)

    def update_data(self):
        self.battery.update_data()

        for label_text, checkbox in self.checkbox_labels.items():
            if checkbox.isChecked():
                if label_text == 'Уровень заряда':
                    self.label_percent.setText(f'Уровень заряда батареи: {self.battery.get_percent()}%')
                    self.progress_bar.setValue(self.battery.get_percent())
                elif label_text == 'Прогноз времени работы':
                    self.label_time_left.setText(f'Прогноз времени работы: {self.battery.get_time_left()}')
                elif label_text == 'Подключено к сети':
                    if self.battery.get_power_plugged():
                        self.label_power_plugged.setText('Подключено к сети: Да')
                    else:
                        self.label_power_plugged.setText('Подключено к сети: Нет')
                    self.label_power_plugged.show()
            else:
                if label_text == 'Уровень заряда':
                    self.label_percent.clear()
                    self.label_percent.show()
                    self.progress_bar.setValue(0)
                elif label_text == 'Прогноз времени работы':
                    self.label_time_left.clear()
                    self.label_time_left.show()
                elif label_text == 'Подключено к сети':
                    self.label_power_plugged.clear()

    def update_visibility(self):
        self.update_data()

    def update_refresh_time(self):
        refresh_time = int(self.refresh_time_combobox.currentText())
        self.timer.setInterval(refresh_time * 1000)
        self.timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    battery_monitor_app = BatteryMonitorApp()
    battery_monitor_app.show()
    sys.exit(app.exec_())
