import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QComboBox
from PyQt5.QtCore import QTimer
from Project.hardware.GPU import GPU


class GPUMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.gpu = GPU()
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
            'Название видеокарты': self.create_label(''),
            'Загрузка видеокарты': self.create_label(''),
            'Тактовая частота видеокарты': self.create_label(''),
            'Температура': self.create_label(''),
            'Напряжение': self.create_label(''),
            'Использовано памяти': self.create_label(''),
            'Свободно памяти': self.create_label(''),
        }

        self.checkbox_labels = {
            'Название видеокарты': QCheckBox('Название видеокарты', checked=True),
            'Загрузка видеокарты': QCheckBox('Загрузка видеокарты', checked=True),
            'Тактовая частота видеокарты': QCheckBox('Тактовая частота видеокарты', checked=True),
            'Температура': QCheckBox('Температура', checked=True),
            'Напряжение': QCheckBox('Напряжение', checked=True),
            'Использовано памяти': QCheckBox('Использовано памяти', checked=True),
            'Свободно памяти': QCheckBox('Свободно памяти', checked=True),
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

        self.setWindowTitle('GPUMonitorApp')
        self.setGeometry(100, 100, 400, 300)

        self.timer.start(1000)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 14px;')
        return label

    def update_data(self):
        for label_text, checkbox in self.checkbox_labels.items():
            if checkbox.isChecked():
                if label_text == 'Название видеокарты':
                    self.labels[label_text].setText(f'{label_text}: {self.gpu.get_name()}')
                elif label_text == 'Загрузка видеокарты':
                    self.labels[label_text].setText(f'{label_text}: {self.gpu.get_load()}%')
                elif label_text == 'Тактовая частота видеокарты':
                    self.labels[label_text].setText(f'{label_text}: {self.gpu.get_clock()}')
                elif label_text == 'Температура':
                    self.labels[label_text].setText(f'{label_text}: {self.gpu.get_temperature()}')
                elif label_text == 'Напряжение':
                    self.labels[label_text].setText(f'{label_text}: {self.gpu.get_power()}')
                elif label_text == 'Использовано памяти':
                    self.labels[label_text].setText(f'{label_text}: {self.gpu.get_memory_used()}')
                elif label_text == 'Свободно памяти':
                    self.labels[label_text].setText(f'{label_text}: {self.gpu.get_memory_free()}')
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
    gpu_monitor_app = GPUMonitorApp()
    gpu_monitor_app.show()
    sys.exit(app.exec_())
