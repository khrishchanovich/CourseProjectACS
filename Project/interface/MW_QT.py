import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout
from Project.interface.CPU_QT import CPUMonitorApp
from Project.interface.GPU_QT import GPUMonitorApp
from Project.interface.RAM_QT import RAMMonitorApp
from Project.interface.SSD_QT import SSDMonitorApp
from Project.interface.battery import BatteryMonitorApp


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Создаем QTabWidget для управления вкладками
        tab_widget = QTabWidget(self)

        # Создаем вкладки для каждого из окон
        cpu_tab = QWidget()
        gpu_tab = QWidget()
        ram_tab = QWidget()
        ssd_tab = QWidget()
        battery_tab = QWidget()

        # Добавляем окна мониторинга на соответствующие вкладки
        cpu_layout = QVBoxLayout(cpu_tab)
        cpu_layout.addWidget(CPUMonitorApp())
        cpu_tab.setLayout(cpu_layout)

        gpu_layout = QVBoxLayout(gpu_tab)
        gpu_layout.addWidget(GPUMonitorApp())
        gpu_tab.setLayout(gpu_layout)

        ram_layout = QVBoxLayout(ram_tab)
        ram_layout.addWidget(RAMMonitorApp())
        ram_tab.setLayout(ram_layout)

        ssd_layout = QVBoxLayout(ssd_tab)
        ssd_layout.addWidget(SSDMonitorApp())
        ssd_tab.setLayout(ssd_layout)

        battery_layout = QVBoxLayout(battery_tab)
        battery_layout.addWidget(BatteryMonitorApp())
        battery_tab.setLayout(battery_layout)

        # Добавляем вкладки в QTabWidget
        tab_widget.addTab(cpu_tab, 'CPU')
        tab_widget.addTab(gpu_tab, 'GPU')
        tab_widget.addTab(ram_tab, 'RAM')
        tab_widget.addTab(ssd_tab, 'SSD')
        tab_widget.addTab(battery_tab, 'Battery')

        self.setCentralWidget(tab_widget)

        # Устанавливаем стили для MainWindow
        self.setStyleSheet('''
            QMainWindow {
                background-color: #1E1E1E; /* Темный фон */
                color: white; /* Белый цвет текста */
            }

            QTabWidget::pane {
                border: 2px solid white; /* Белая рамка для вкладок */
            }

            QTabWidget::tab-bar {
                alignment: center; /* Выравнивание вкладок по центру */
            }

            QTabBar::tab {
                background-color: #2F2F2F; /* Цвет фона вкладок */
                color: white; /* Белый цвет текста вкладок */
                min-width: 100px; /* Минимальная ширина вкладок */
                padding: 5px;
            }

            QTabBar::tab:selected {
                background-color: #1E90FF; /* Цвет выделенной вкладки */
            }
        ''')

        self.setWindowTitle('Hardware Monitor')
        self.setGeometry(100, 100, 800, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
