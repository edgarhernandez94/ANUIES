
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
class MgnWindow(QMainWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Magnetometer")
        self.main_window = main_window
        self.setWindowState(QtCore.Qt.WindowFullScreen)
        self.fig, self.ax = plt.subplots()
        self.line_x, = self.ax.plot([], [], label='X')
        self.line_y, = self.ax.plot([], [], label='Y')
        self.line_z, = self.ax.plot([], [], label='Z')
        self.ax.legend()
        self.ax.set_xlabel('Time')
        self.ax.set_ylabel('Value')
        self.ax.set_title('Magnetometer')
        self.fig.canvas.draw()
        self.back_button = QtWidgets.QPushButton("Back", self)
        self.back_button.clicked.connect(self.back_to_main_window)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.fig.canvas.toolbar)
        layout.addWidget(self.fig.canvas)
        central_widget = QtWidgets.QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    def display_graph(self, data):
        x = data[0]
        y = data[1]
        z = data[2]
        print (x)
        self.line_x.set_data(range(len(x)), x)
        self.line_y.set_data(range(len(y)), y)
        self.line_z.set_data(range(len(z)), z)
        self.ax.set_xlim(0, len(x) - 1)
        self.ax.set_ylim(min(min(x, y, z)) - 1, max(max(x, y, z)) + 1)
        self.fig.canvas.draw()
    def back_to_main_window(self):
        self.close()
        self.main_window.show()