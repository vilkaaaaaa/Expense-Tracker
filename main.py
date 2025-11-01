import sys
import random
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMessageBox, QListWidget
from basewindow import BaseWindow

class MyApp(BaseWindow):
    def __init__(self) -> None:
        super().__init__("Exprense Tracker  ")
        self.init_ui()
        self.show()

    def init_ui(self)-> None:
        layout = QVBoxLayout()
        self.setLayout(layout)





app = QApplication(sys.argv)
window = MyApp()
sys.exit(app.exec_())