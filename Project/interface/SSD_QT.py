import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTabWidget, QCheckBox, QComboBox
from PyQt5.QtCore import QTimer
import psutil
from Project.hardware.SSD import SSD


class SSDMonitorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.tab_widget = QTabWidget(self)
        self.tabs = []

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_data)

        self.init_ui()

    def init_ui(self):
        self.setStyleSheet("""
            background-color: #1E1E1E;
            color: white;
            font-size: 16px;
        """)

        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid white;
                background-color: #1E1E1E;
            }

            QTabBar::tab {
                background-color: #2E2E2E;
                color: white;
                border: 2px solid #1E1E1E;
                padding: 8px;
            }

            QTabBar::tab:selected {
                background-color: #1E1E1E;
            }
        """)

        main_layout = QVBoxLayout(self)

        # Добавляем флажки для выбора отображаемых меток
        self.checkbox_labels = {
            'Диск': QCheckBox('Диск', checked=True),
            'Загрузка диска': QCheckBox('Загрузка диска', checked=True),
            'Доступно': QCheckBox('Доступно', checked=True),
            'Общее': QCheckBox('Общее', checked=True),
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

        self.setLayout(main_layout)

        partitions = psutil.disk_partitions()

        for partition in partitions:
            disk_info = SSD(partition)

            tab = QWidget()
            layout = QVBoxLayout(tab)

            labels = {
                'Диск': self.create_label(''),
                'Загрузка диска': self.create_label(''),
                'Доступно': self.create_label(''),
                'Общее': self.create_label(''),
            }

            for label_text, label_widget in labels.items():
                layout.addWidget(label_widget)
                label_widget.setStyleSheet("""
                    border: 2px solid white;
                    padding: 5px;
                """)

            tab.setLayout(layout)

            self.tabs.append((tab, labels))
            self.tab_widget.addTab(tab, f'Диск {disk_info.get_name()}')

        main_layout.addWidget(self.tab_widget)

        self.setWindowTitle('SSDMonitorApp')
        self.setGeometry(100, 100, 400, 300)

        self.timer.start(1000)

    def create_label(self, text):
        label = QLabel(text)
        label.setStyleSheet('font-size: 14px;')
        return label

    def update_data(self):
        for tab, labels in self.tabs:
            partition = psutil.disk_partitions()[self.tabs.index((tab, labels))]
            disk_info = SSD(partition)

            for label_text, checkbox in self.checkbox_labels.items():
                if checkbox.isChecked():
                    if label_text == 'Диск':
                        labels[label_text].setText(f'Диск: {disk_info.get_name()}')
                    elif label_text == 'Загрузка диска':
                        labels[label_text].setText(f'Загрузка диска: {disk_info.get_percent()}%')
                    elif label_text == 'Доступно':
                        labels[label_text].setText(f'Доступно: {disk_info.get_available_space()}')
                    elif label_text == 'Общее':
                        labels[label_text].setText(f'Общее: {disk_info.get_total_space()}')
                else:
                    labels[label_text].clear()
                    labels[label_text].show()

    def update_visibility(self):
        self.update_data()

    def update_refresh_time(self):
        refresh_time = int(self.refresh_time_combobox.currentText())
        self.timer.setInterval(refresh_time * 1000)
        self.timer.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ssd_monitor_app = SSDMonitorApp()
    ssd_monitor_app.show()
    sys.exit(app.exec_())
