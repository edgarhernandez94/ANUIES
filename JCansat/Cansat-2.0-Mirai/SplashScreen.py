from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from cansatgui2 import Ui_MainWindow

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: white;")
        self.setGeometry(0, 0, QtWidgets.QDesktopWidget().screenGeometry().width(),
                          QtWidgets.QDesktopWidget().screenGeometry().height())
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, self.width(), self.height())
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_pixmap = QtGui.QPixmap("mirai.png")
        self.label.setPixmap(self.logo_pixmap)
        self.animation = QPropertyAnimation(self.label, b"geometry")
        self.animation.setDuration(3000)
        self.animation.setStartValue(QtCore.QRect(self.width() / 2, self.height() / 2, 0, 0))
        self.animation.setEndValue(self.label.geometry())
        self.animation.setLoopCount(1)
        self.show()
        QTimer.singleShot(4000, self.close)
    def back_to_main_window(self):
        self.close()