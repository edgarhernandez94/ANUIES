import sys
import serial.tools.list_ports
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 160, 511))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.pB_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_1.setEnabled(True)
        self.pB_1.setObjectName("pB_1")
        self.verticalLayout.addWidget(self.pB_1)
        self.pB_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_2.setObjectName("pB_2")
        self.verticalLayout.addWidget(self.pB_2)
        self.pB_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pB_3.setObjectName("pB_3")
        self.verticalLayout.addWidget(self.pB_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.open_map_window)  # Conectar el botón "GPS" a la función open_map_window
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(580, 30, 207, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox_2 = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(580, 170, 160, 351))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textEdit_10 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_10.setObjectName("textEdit_10")
        self.verticalLayout_4.addWidget(self.textEdit_10)
        self.textEdit_6 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_4.addWidget(self.textEdit_6)
        self.textEdit_4 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_4.addWidget(self.textEdit_4)
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_4.addWidget(self.textEdit)
        self.textEdit_5 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_5.setObjectName("textEdit_5")
        self.verticalLayout_4.addWidget(self.textEdit_5)
        self.textEdit_12 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_12.setObjectName("textEdit_12")
        self.verticalLayout_4.addWidget(self.textEdit_12)
        self.textEdit_3 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_4.addWidget(self.textEdit_3)
        self.textEdit_2 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_4.addWidget(self.textEdit_2)
        self.textEdit_11 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_11.setObjectName("textEdit_11")
        self.verticalLayout_4.addWidget(self.textEdit_11)
        self.textEdit_8 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_8.setObjectName("textEdit_8")
        self.verticalLayout_4.addWidget(self.textEdit_8)
        self.textEdit_7 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_7.setObjectName("textEdit_7")
        self.verticalLayout_4.addWidget(self.textEdit_7)
        self.textEdit_13 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_13.setObjectName("textEdit_13")
        self.verticalLayout_4.addWidget(self.textEdit_13)
        self.textEdit_9 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_9.setObjectName("textEdit_9")
        self.verticalLayout_4.addWidget(self.textEdit_9)
        self.textEdit_14 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_14.setObjectName("textEdit_14")
        self.verticalLayout_4.addWidget(self.textEdit_14)
        self.textEdit_15 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_15.setObjectName("textEdit_15")
        self.verticalLayout_4.addWidget(self.textEdit_15)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.readerThread = SerialReaderThread("","")  # Create an instance of SerialReaderThread
        self.readerThread.dataReceived.connect(self.update_data)
        self.connected = False
        self.main_window = MainWindow
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        window_width = MainWindow.frameGeometry().width()
        window_height = MainWindow.frameGeometry().height()
        self.pB_1.clicked.connect(self.open_new_window)
        #self.new_window = None
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(
            20, 20, window_width * 0.2, window_height * 0.8))
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(
            window_width * 0.725, window_height * 0.05, window_width * 0.25, window_height * 0.13))
        
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(
            window_width * 0.725, window_height * 0.28, window_width * 0.2, window_height * 0.67))
    def open_map_window(self):
        self.map_window = MapWindow()
        self.map_window.setWindowModality(QtCore.Qt.ApplicationModal)

        self.map_window.show()
    def open_new_window(self):
        self.new_window = NewWindow(self.main_window)
        self.new_window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.new_window.show()
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            QApplication.quit()
    def update_data(self, data):
        if data:
            data_list = data.split(",")
            self.textEdit_10.setText(data_list[0])
            self.textEdit_6.setText(data_list[1])
            self.textEdit_4.setText(data_list[2])
            self.textEdit.setText(data_list[3])
            self.textEdit_5.setText(data_list[4])
            self.textEdit_12.setText(data_list[5])
            self.textEdit_3.setText(data_list[6])
            self.textEdit_2.setText(data_list[7])
            self.textEdit_11.setText(data_list[8])
            self.textEdit_8.setText(data_list[9])
            self.textEdit_7.setText(data_list[10])
            self.textEdit_13.setText(data_list[11])
            self.textEdit_9.setText(data_list[12])
            self.textEdit_14.setText(data_list[13])
            self.textEdit_15.setText(data_list[14])

            
        else:
            QMessageBox.warning(MainWindow, "Error de conexión", "No se pudo conectar al puerto seleccionado.")
    def read_serial_data(self):
        # Leer los datos recibidos del puerto serie
        data = self.serial_port.readline().decode().strip()
        #print(data)  # Imprimir los datos en la terminal

        # Separar los datos por comas
        data_list = data.split(",")

        # Actualizar los textEdit con los datos recibidos
        self.update_data(data_list)
    def on_pushButton_clicked(self):
        if not self.connected:
            selected_baudrate = self.comboBox_2.currentText()
            selected_port = self.comboBox.currentText()

            if selected_port == "No devices":
                QMessageBox.warning(MainWindow, "No devices", "No se encontraron dispositivos disponibles.")
            else:
                self.readerThread.port = selected_port
                self.readerThread.baudrate = selected_baudrate
                self.readerThread.start()  # Start the SerialReaderThread
                self.connected = True
                self.pushButton.setText("Disconnect")
                QMessageBox.information(MainWindow, "Conexión exitosa",
                                        f"Conectado al puerto {selected_port} a {selected_baudrate} baudrate.")
        else:
            self.readerThread.stop()  # Stop the SerialReaderThread
            self.connected = False
            self.pushButton.setText("Connect")
            QMessageBox.information(MainWindow, "Desconexión exitosa", "Desconectado del puerto COM.")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pB_1.setText(_translate("MainWindow", "Magnetometer"))
        self.pB_2.setText(_translate("MainWindow", "Gyroscope"))
        self.pB_3.setText(_translate("MainWindow", "Accelerometer"))
        self.pushButton_4.setText(_translate("MainWindow", "GPS"))
        self.pushButton.setText(_translate("MainWindow", "Connect"))
        self.label.setText(_translate("MainWindow", "Mag_X:"))
        self.label_2.setText(_translate("MainWindow", "Mag_Y:"))
        self.label_3.setText(_translate("MainWindow", "Mag_Z:"))
        self.label_4.setText(_translate("MainWindow", "Gyro_X:"))
        self.label_12.setText(_translate("MainWindow", "Gyro_Y:"))
        self.label_5.setText(_translate("MainWindow", "Gyro_Z"))
        self.label_11.setText(_translate("MainWindow", "Acce_X:"))
        self.label_6.setText(_translate("MainWindow", "Acce_Y:"))
        self.label_8.setText(_translate("MainWindow", "Acce_Z:"))
        self.label_9.setText(_translate("MainWindow", "Pressure:"))
        self.label_7.setText(_translate("MainWindow", "Temperature:"))
        self.label_13.setText(_translate("MainWindow", "Altitude:"))
        self.label_14.setText(_translate("MainWindow", "Lat:"))
        self.label_10.setText(_translate("MainWindow", "Lon:"))
class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowState(Qt.WindowFullScreen)
        self.setWindowModality(Qt.ApplicationModal)
        self.map_view = QWebEngineView(self)
        self.setCentralWidget(self.map_view)
        self.back_button = QPushButton("Back", self)
        self.back_button.clicked.connect(self.back_to_main_window)
        layout = QVBoxLayout()
        layout.addWidget(self.back_button)
        layout.addWidget(self.map_view)
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.load_google_maps()
    def load_google_maps(self):
        # Reemplaza 'TU_CLAVE_DE_API' con tu propia clave de API de Google Maps
        api_key = 'AIzaSyDpzjZlUy9R6r4-l5ZMRajrRbvP8gEX_I8'
        latitude = 37.7749  # Reemplaza con la latitud deseada
        longitude = -122.4194  # Reemplaza con la longitud deseada

        html = f'''
            <!DOCTYPE html>
            <html>
            <head>
                <title>Google Maps</title>
                <style>
                    html, body, #map {{
                        height: 100%;
                        margin: 0;
                        padding: 0;
                    }}
                </style>
            </head>
            <body>
                <div id="map"></div>
                <script src="https://maps.googleapis.com/maps/api/js?key={api_key}"></script>
                <script>
                    function initMap() {{
                        var center = {{ lat: {latitude}, lng: {longitude} }};
                        var map = new google.maps.Map(document.getElementById('map'), {{
                            center: center,
                            zoom: 14
                        }});
                    }}
                    initMap();
                </script>
            </body>
            </html>
        '''

        self.map_view.setHtml(html)
    def back_to_main_window(self):
        self.close()
class NewWindow(QMainWindow):
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
        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Valor')
        self.ax.set_title('Gráfica de los primeros tres datos')
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
        self.line_x.set_data(range(len(x)), x)
        self.line_y.set_data(range(len(y)), y)
        self.line_z.set_data(range(len(z)), z)
        self.ax.set_xlim(0, len(x) - 1)
        self.ax.set_ylim(min(min(x, y, z)) - 1, max(max(x, y, z)) + 1)
        self.fig.canvas.draw()
    def back_to_main_window(self):
        self.hide()
        self.main_window.show()
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
    def closeEvent(self, event):
        self.close()  # Cierra la ventana emergente
        MainWindow.show()  # Muestra la ventana principal
class SerialReaderThread(QThread):
    dataReceived = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.serial_port = None
        self.running = False
        self.first_newline_detected = False

    def run(self):
        try:
            self.serial_port = serial.Serial(self.port, self.baudrate)
            self.running = True
            while self.running:
                if self.serial_port.in_waiting:
                    data = self.serial_port.readline().decode().strip()
                    
                    # Si es la primera vez que detectamos un salto de línea
                    if not self.first_newline_detected:
                        self.first_newline_detected = True
                        continue
                    
                    self.dataReceived.emit(data)
        except serial.SerialException:
            pass
        finally:
            if self.serial_port and self.serial_port.is_open:
                self.serial_port.close()

    def stop(self):
        self.running = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    splash = SplashScreen()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.timer = QTimer()
    ui.timer.timeout.connect(ui.read_serial_data)
    baudrates = ["9600", "115200", "230400"]
    ui.comboBox_2.addItems(baudrates)
    ports = serial.tools.list_ports.comports()
    if ports:
        port_names = [port.device for port in ports]
        ui.comboBox.addItems(port_names)
    else:
        ui.comboBox.addItem("No devices")
    splash.show()
    sys.exit(app.exec_())
