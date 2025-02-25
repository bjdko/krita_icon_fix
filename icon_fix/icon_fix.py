from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

def yoink():
    QApplication.setAttribute(Qt.AA_DontShowIconsInMenus, False)
