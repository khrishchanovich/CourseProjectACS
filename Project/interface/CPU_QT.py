import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QCheckBox, QComboBox
from PyQt5.QtCore import QTimer
from Project.hardware.CPU import CPU


class CPUMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализируем CPU
        self.cpu = CPU()

        # Инициализируем таймер для обновления данных
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)

        # Инициализируем интерфейс пользователя
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Стилизуем виджеты
        self.setStyleSheet("""
            background-color: #1E1E1E; /* Темный фон */
            color: white; /* Белый цвет текста */
            font-size: 16px; /* Размер шрифта */
        """)

        # Инициализируем метки
        self.labels = {
            'Название процессора': self.create_label(''),
            'Загрузка процессора': self.create_label(''),
            'Тактовая частота процессора': self.create_label(''),
            'Количество активных ядер': self.create_label(''),
            'Температура': self.create_label(''),
            'Напряжение': self.create_label('')
        }

        # Инициализируем флажки для выбора отображаемых меток
        self.checkbox_labels = {
            'Название процессора': QCheckBox('Название процессора', checked=True),
            'Загрузка процессора': QCheckBox('Загрузка процессора', checked=True),
            'Тактовая частота процессора': QCheckBox('Тактовая частота процессора', checked=True),
            'Количество активных ядер': QCheckBox('Количество активных ядер', checked=True),
            'Температура': QCheckBox('Температура', checked=True),
            'Напряжение': QCheckBox('Напряжение', checked=True)
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

        # Добавляем метки в макет
        for label_text, label_widget in self.labels.items():
            layout.addWidget(label_widget)
            label_widget.setStyleSheet("""
                border: 2px solid white; /* Белая рамка */
                padding: 5px;
            """)

        self.setLayout(layout)

        self.setWindowTitle('CPUMonitorApp')
        self.setGeometry(100, 100, 400, 400)

        # Запускаем таймер с интервалом в 1 секунду
        self.timer.start(1000)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 14px;')
        return label

    def update_data(self):
        # Обновляем данные каждую секунду
        for label_text, checkbox in self.checkbox_labels.items():
            if checkbox.isChecked():
                if label_text == 'Название процессора':
                    self.labels[label_text].setText(f'{label_text}: {self.cpu.get_name()}')
                elif label_text == 'Загрузка процессора':
                    self.labels[label_text].setText(f'{label_text}: {self.cpu.get_percent()}%')
                elif label_text == 'Тактовая частота процессора':
                    self.labels[label_text].setText(f'{label_text}: {self.cpu.get_frequency()}')
                elif label_text == 'Количество активных ядер':
                    self.labels[label_text].setText(f'{label_text}: {self.cpu.get_num_active_cores()}')
                elif label_text == 'Температура':
                    self.labels[label_text].setText(f'{label_text}: {self.cpu.get_temperature()}')
                elif label_text == 'Напряжение':
                    self.labels[label_text].setText(f'{label_text}: {self.cpu.get_power()}')
            else:
                self.labels[label_text].clear()  # Очищаем текст лейбла
                self.labels[label_text].show()  # Показываем лейбл, если флаг выбран

    def update_visibility(self):
        # Обновляем видимость меток в соответствии с состоянием флажков
        self.update_data()

    def update_refresh_time(self):
        # Обновляем время обновления
        refresh_time = int(self.refresh_time_combobox.currentText())
        self.timer.setInterval(refresh_time * 1000)  # Переводим секунды в миллисекунды
        self.timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cpu_monitor_app = CPUMonitorApp()
    cpu_monitor_app.show()
    sys.exit(app.exec_())
