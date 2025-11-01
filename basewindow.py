from unittest import case

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox


class BaseWindow(QWidget):
    def __init__(self, header:str) -> None:
        super().__init__()
        with open("style.css", "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        self.setWindowTitle(header)
        self.setWindowIcon(QIcon("icon.ico"))
        self.setFixedSize(600, 400)

    @staticmethod
    def show_modal(header:str, text:str, icon:int = 0) -> None:
        msg = QMessageBox()
        msg.setWindowTitle(header)
        msg.setText(text)
        match icon:
            case 0: msg.setIcon(QMessageBox.Information)
            case 1: msg.setIcon(QMessageBox.Warning)
            case 2: msg.setIcon(QMessageBox.Critical)
            case 3: msg.setIcon(QMessageBox.Question)
            case _: raise Exception("цифрами дебил пиши")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
