import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QComboBox
from PyQt5.QtCore import QTimer
from Project.hardware.RAM import RAM


class RAMMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.ram = RAM()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.setStyleSheet("""
            background-color: #1E1E1E;
            color: white;
            font-size: 16px;
        """)

        self.labels = {
            'Загрузка оперативной памяти': self.create_label(''),
            'Доступно': self.create_label(''),
            'Общее': self.create_label(''),
        }

        self.checkbox_labels = {
            'Загрузка оперативной памяти': QCheckBox('Загрузка оперативной памяти', checked=True),
            'Доступно': QCheckBox('Доступно', checked=True),
            'Общее': QCheckBox('Общее', checked=True),
        }

        for label_text, checkbox in self.checkbox_labels.items():
            checkbox.stateChanged.connect(self.update_visibility)
            layout.addWidget(checkbox)

            # Инициализируем выпадающий список для выбора времени обновления
        self.refresh_time_label = QLabel('Время обновления (секунды):')
        self.refresh_time_combobox = QComboBox()
        self.refresh_time_combobox.addItems(['1', '2', '5', '10', '30'])
        self.refresh_time_combobox.setCurrentIndex(0)
        self.refresh_time_combobox.currentIndexChanged.connect(self.update_refresh_time)
        layout.addWidget(self.refresh_time_label)
        layout.addWidget(self.refresh_time_combobox)

        for label_text, label_widget in self.labels.items():
            layout.addWidget(label_widget)
            label_widget.setStyleSheet("""
                border: 2px solid white;
                padding: 5px;
            """)

        self.setLayout(layout)

        self.setWindowTitle('RAMMonitorApp')
        self.setGeometry(100, 100, 400, 300)

        self.timer.start(1000)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 14px;')
        return label

    def update_data(self):
        self.ram.update_data()
        for label_text, checkbox in self.checkbox_labels.items():
            if checkbox.isChecked():
                if label_text == 'Загрузка оперативной памяти':
                    self.labels[label_text].setText(f'Загрузка оперативной памяти: {self.ram.get_memory_percent()}%')
                elif label_text == 'Доступно':
                    self.labels[label_text].setText(f'Доступно: {self.ram.get_available_memory()}')
                elif label_text == 'Общее':
                    self.labels[label_text].setText(f'Общее: {self.ram.get_total_memory()}')
            else:
                self.labels[label_text].clear()
                self.labels[label_text].show()

    def update_visibility(self):
        self.update_data()

    def update_refresh_time(self):
        refresh_time = int(self.refresh_time_combobox.currentText())
        self.timer.setInterval(refresh_time * 1000)
        self.timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ram_monitor_app = RAMMonitorApp()
    ram_monitor_app.show()
    sys.exit(app.exec_())
