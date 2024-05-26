from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QLabel, QApplication
from PyQt5.QtCore import QTimer
from serialreader import SerialReaderThread
import serial
from serial.tools import list_ports


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
        # Add the self.connected attribute
        self.connected = False
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Ajustar proporciones y tamaños de elementos
        window_width = MainWindow.frameGeometry().width()
        window_height = MainWindow.frameGeometry().height()

        # Ajustar el tamaño del widget verticalLayoutWidget
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(
            20, 20, window_width * 0.2, window_height * 0.8))

        # Ajustar el tamaño del widget horizontalLayoutWidget
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(
            window_width * 0.725, window_height * 0.05, window_width * 0.25, window_height * 0.13))

        # Ajustar el tamaño del widget horizontalLayoutWidget_2
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(
            window_width * 0.725, window_height * 0.28, window_width * 0.2, window_height * 0.67))

    def update_data(self, data):
        # Asegurarse de que el arreglo tenga la longitud correcta
        # if len(data) != 14:
        #     return
        print(data)
        # Mostrar cada dato en los textEdit correspondientes
        self.textEdit_10.setText(data[0])
        self.textEdit_6.setText(data[1])
        self.textEdit_4.setText(data[2])
        self.textEdit.setText(data[3])
        self.textEdit_5.setText(data[4])
        self.textEdit_12.setText(data[5])
        self.textEdit_3.setText(data[6])
        self.textEdit_2.setText(data[7])
        self.textEdit_11.setText(data[8])
        self.textEdit_8.setText(data[9])
        self.textEdit_7.setText(data[10])
        self.textEdit_13.setText(data[11])
        self.textEdit_9.setText(data[12])
        self.textEdit_14.setText(data[13])
        self.textEdit_15.setText(data[14])

    def read_serial_data(self):
        # Leer los datos recibidos del puerto serie
        data = self.serial_port.readline().decode().strip()
        #print(data)  # Imprimir los datos en la terminal

        # Separar los datos por comas
        data_list = data.split(",")

        # Actualizar los textEdit con los datos recibidos
        self.update_data(data_list)
        

    def on_pushButton_clicked(self):
        # Acción a realizar cuando se presione el botón
        if not self.connected:
            # Conectar al puerto COM seleccionado
            selected_baudrate = self.comboBox_2.currentText()
            selected_port = self.comboBox.currentText()

            if selected_port == "No devices":
                QMessageBox.information(self, "Conexión exitosa", f"Conectado al puerto {selected_port} a {selected_baudrate} baudrate.")
            else:
                try:
                    self.serial_port = serial.Serial(selected_port, int(selected_baudrate), timeout=1)
                    self.connected = True
                    self.pushButton.setText("Disconnect")
                    QMessageBox.information(MainWindow, "Conexión exitosa", f"Conectado al puerto {selected_port} a {selected_baudrate} baudrate.")
                    self.timer.start(100)  # Iniciar el temporizador para leer datos cada 100 milisegundos
                except serial.SerialException as e:
                    QMessageBox.warning(MainWindow, "Error de conexión", f"No se pudo conectar al puerto {selected_port}.\n\nError: {str(e)}")
        else:
            # Desconectar del puerto COM
            if self.serial_port:
                self.serial_port.close()
            self.connected = False
            self.pushButton.setText("Connect")
            self.timer.stop()  # Detener el temporizador al desconectar del puerto serie
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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.timer = QTimer()  # Create a QTimer instance
        self.ui.timer.timeout.connect(self.ui.read_serial_data)  # Connect the timeout signal to the read_serial_data slot

        # Agregar los valores de baudrate al combobox_2
        baudrates = ["9600", "115200", "230400"]
        self.ui.comboBox_2.addItems(baudrates)

        # Mostrar los puertos COM disponibles en el comboBox
        ports = serial.tools.list_ports.comports()
        if ports:
            port_names = [port.device for port in ports]
            self.ui.comboBox.addItems(port_names)
        else:
            self.ui.comboBox.addItem("No devices")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
